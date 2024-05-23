import sys
from scapy.all import ICMP, IP, sr1
from netaddr import IPNetwork


def ping_sweep(network, netmask):
    live_hosts = []
    total_hosts = 0
    scanned_hosts = 0

    ip_network = IPNetwork(network + '/' + netmask)
    print("ip network: ", ip_network)

    for host in ip_network.iter_hosts():
        total_hosts += 1
        scanned_hosts += 1
        print(f"Scanning: {scanned_hosts}/{total_hosts}", end="\r")
        # print("hosts: ", host)
        response = sr1(IP(dst=str(host))/ICMP(), timeout=0.1, verbose=0)
        # print("response: ", response)
        if response is not None:
            live_hosts.append(str(host))
            print(f"Host {host} is online.")

    return live_hosts


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python ping_sweeper.py <network> <netmask>")
        sys.exit(1)

    network = sys.argv[1]
    netmask = sys.argv[2]

    print("network: ", network)
    print("netmask: ", netmask)

    live_hosts = ping_sweep(network, netmask)
    print("Completed\n")
    print(f"Live Hosts: {live_hosts}")
