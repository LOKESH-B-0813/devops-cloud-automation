# target_file can be your 'just.txt' file for testing
#target_file = "DevOps_Logbook.txt"

#print(f"Opening and reading {target_file}...")

# Opening the file in 'r' (Read) mode
#with open(target_file, "r") as file:
 #   content = file.read()
  #  print("\n--- File Content Start ---")
   # print(content)
   # print("--- File Content End ---\n")

target_file = "/home/lokesh-b/Desktop/devops-cloud-automation/DevOps_Logbook.txt"

with open(target_file, "r") as file:
    content = file.read()

# New Automation Logic: Scan the text for keywords
keyword = "Path"

if keyword in content:
    print(f"🎯 Analysis Alert: Found the concept '{keyword}' inside your logbook!")
else:
    print(f"❌ '{keyword}' was not found in the file.")
