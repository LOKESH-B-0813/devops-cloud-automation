from collections import Counter

# Simulated server logs
raw_logs = [
    "2026-08-06 10:00:01 SERVICE=nginx STATUS=OK",
    "2026-08-06 10:01:15 SERVICE=postgresql STATUS=FAILED",
    "2026-08-06 10:02:00 SERVICE=redis STATUS=OK",
    "2026-08-06 10:03:22 SERVICE=postgresql STATUS=FAILED",
    "2026-08-06 10:04:10 SERVICE=docker STATUS=FAILED",
    "2026-08-06 10:05:00 SERVICE=postgresql STATUS=FAILED",
]

def analyze_failed_services(log_entries):
    failed_services = []
    
    for entry in log_entries:
        if "STATUS=FAILED" in entry:
            # Extract service name by parsing key-value pairs
            parts = entry.split()
            for part in parts:
                if part.startswith("SERVICE="):
                    service_name = part.split("=")[1]
                    failed_services.append(service_name)
                    
    # Count occurrences of each failed service
    failure_counts = Counter(failed_services)
    
    return failure_counts

if __name__ == "__main__":
    results = analyze_failed_services(raw_logs)
    print("Failure Summary Report:")
    for service, count in results.items():
        print(f" - {service}: {count} failure(s)")
