import os

def analyze_logs(file_path):
    print("=" * 50)
    print(f"🚀 DEVOPS LOG ANALYZER: Scanning {file_path}")
    print("=" * 50)
    
    if not os.path.exists(file_path):
        print(f"❌ Error: The file {file_path} does not exist.")
        return

    error_count = 0
    warning_count = 0
    critical_events = []

    # Open and parse the log file line by line
    with open(file_path, 'r') as file:
        for line_num, line in enumerate(file, 1):
            if "ERROR" in line:
                error_count += 1
            elif "WARNING" in line:
                warning_count += 1
            elif "CRITICAL" in line:
                error_count += 1
                critical_events.append(f"Line {line_num}: {line.strip()}")

    # Print the automated analytics report
    print("\n📈 [📊 METRICS SUMMARY]")
    print(f"🔹 Total WARNINGS identified: {warning_count}")
    print(f"🔺 Total ERRORS/CRITICALS identified: {error_count}")
    print("-" * 50)

    if critical_events:
        print("\n🚨 [🔥 CRITICAL EVENTS DETECTED]")
        for event in critical_events:
            print(f"  -> {event}")
    else:
        print("\n✅ System status optimal: No critical events found.")
    print("=" * 50)

# Run the analyzer against your existing log file
analyze_logs("system_logs.txt")
