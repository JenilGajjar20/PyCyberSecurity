import sys
import threading
from queue import Queue
from netaddr import IPNetwork
from scapy.all import ICMP, IP, sr1
from rich.console import Console
from rich.table import Table

console = Console()


def ping_host(host, live_hosts, lock):
    try:
        response = sr1(IP(dst=str(host))/ICMP(), timeout=0.1, verbose=0)
        if response is not None:
            with lock:
                live_hosts.append(str(host))
                console.log(f"[green]Host {host} is online.[/green]")
    except Exception as e:
        console.log(f"[red]Error pinging {host}: {e} [/red]")


def worker(queue, live_hosts, lock, total_hosts, scanned_hosts):
    while not queue.empty():
        host = queue.get()
        with lock:
            scanned_hosts[0] += 1
            print(f"Scanning: {scanned_hosts[0]}/{total_hosts[0]}", end="\r")
        ping_host(host, live_hosts, lock)
        queue.task_done()


def ping_sweep(network, netmask, num_threads=10):
    live_hosts = []
    lock = threading.Lock()
    queue = Queue()
    total_hosts = [0]
    scanned_hosts = [0]

    ip_network = IPNetwork(network + '/' + netmask)
    console.log(f"[blue]ip network: {ip_network}[/blue]")

    for host in ip_network.iter_hosts():
        queue.put(host)
        total_hosts[0] += 1

    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(
            target=worker, args=(queue, live_hosts, lock, total_hosts, scanned_hosts))
        thread.start()
        threads.append(thread)

    queue.join()
    for thread in threads:
        thread.join()

    return live_hosts, list(ip_network.iter_hosts())


if __name__ == '__main__':
    if len(sys.argv) != 3:
        console.log(
            "[red]Usage: python ping_sweeper.py <network> <netmask>[/red]")
        sys.exit(1)

    network = sys.argv[1]
    netmask = sys.argv[2]

    console.log(f"[blue]network: {network}[/blue]")
    console.log(f"[blue]netmask: {netmask}[/blue]")

    live_hosts, all_hosts = ping_sweep(network, netmask)
    console.log("[green]Completed\n[/green]")

    table = Table(show_header=True, header_style="bold green")
    table.add_column("Live Hosts: ", justify="left")
    for host in live_hosts:
        table.add_row(host)

    console.print(table)
    console.log(
        f"[blue]Total Hosts Scanned: {len(all_hosts)} [/blue]")
    console.log(f"[green]Total Live Hosts: {len(live_hosts)} [/green]")
