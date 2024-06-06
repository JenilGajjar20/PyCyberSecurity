import nmap3
nmap = nmap3.Nmap()

# Scan top Ports
# top_ports = nmap.scan_top_ports('scanme.nmap.org')
# print(top_ports)

# dns-brute scripts
# dns_brute = nmap.nmap_dns_brute_script('scanme.nmap.org')
# print(dns_brute)

# Version detection
version_results = nmap.nmap_version_detection('scanme.nmap.org')
print(version_results)