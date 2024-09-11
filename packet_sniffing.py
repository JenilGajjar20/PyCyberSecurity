from scapy.all import sniff, IP


def detectIntrusion(packet):
    print("Captured packet: ", packet.summary())
    suspicious_ip = '192.168.1.100'
    print("IP: ", IP)
    if IP in packet:
        print("Packet source: ", packet[IP].src)
        if packet[IP].src == suspicious_ip:
            print(f"Alert! suspicious activity detected from {suspicious_ip}")


sniff(prn=detectIntrusion, count=5)
