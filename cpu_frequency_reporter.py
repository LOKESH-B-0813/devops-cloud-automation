# cpu_frequency_reporter.py - Extracts processor model and clock frequency from /proc/cpuinfo
def get_cpu_summary():
    model = "Unknown"
    freq = "Unknown"
    with open("/proc/cpuinfo", "r") as f:
        for line in f:
            if "model name" in line and model == "Unknown":
                model = line.split(":")[1].strip()
            elif "cpu MHz" in line and freq == "Unknown":
                freq = line.split(":")[1].strip()
    return model, freq

cpu_model, cpu_mhz = get_cpu_summary()
print(f"CPU Model     : {cpu_model}")
print(f"Base Clock MHz: {cpu_mhz} MHz")
