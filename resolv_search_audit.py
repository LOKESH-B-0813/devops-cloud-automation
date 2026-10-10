# resolv_search_audit.py - Extracts search domains configured in /etc/resolv.conf
search_domains = []
with open("/etc/resolv.conf", "r") as f:
    for line in f:
        if line.startswith("search"):
            search_domains.extend(line.split()[1:])
print(f"Configured DNS Search Domains: {search_domains or 'None (Default)'}")
