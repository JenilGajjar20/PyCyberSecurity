import random
import logging

logging.basicConfig(filename="firewall.log", level=logging.INFO)


def generate_random_ip():
    return f"192.168.1.{random.randint(0, 20)}"


def check_firewall_rules(ip, port, protocol, rules):
    for rule in rules:
        rule_ip, rule_port, rule_protocol, action = rule
        if rule_ip == ip and rule_port == port and rule_protocol == protocol:
            return action
    return "allow"


def log_action(ip, port, protocol, action):
    logging.info(
        f"IP: {ip}, Port: {port}, Protocol: {protocol}, Action: {action}")


def getUserRules():
    rules = []
    while True:
        ip = input("Enter IP address (or 'done' to finish): ")
        if ip == 'done':
            break
        port = int(input("Enter port number: "))
        protocol = input("Enter protocol (TCP or UDP): ")
        action = input("Enter action (allow/block): ")
        rules.append((ip, port, protocol, action))
    return rules


def main():
    user_rules = getUserRules()
    predefined_rules = [
        ("192.168.1.1", 80, "TCP", "block"),
        ("192.168.1.4", 22, "TCP", "block"),
        ("192.168.1.9", 53, "UDP", "block"),
        ("192.168.1.13", 25, "TCP", "block"),
        ("192.168.1.16", 1194, "UDP", "block"),
        ("192.168.1.19", 21, "TCP", "block"),
        ("192.168.1.22", 67, "DHCP", "block"),
        ("192.168.1.27", 194, "TCP", "block"),
    ]

    firewall_rules = predefined_rules + user_rules

    for _ in range(12):
        ip_address = generate_random_ip()
        port_number = random.randint(0, 2000)
        protocol = random.choice(['TCP', 'UDP'])
        action = check_firewall_rules(
            ip_address, port_number, protocol, firewall_rules)
        log_action(ip_address, port_number, protocol, action)
        random_number = random.randint(0, 9999)
        print(
            f"IP: {ip_address}, Port Number: {port_number}, Protocol: {protocol}, Action: {action}, Random Number: {random_number}")


if __name__ == '__main__':
    main()
