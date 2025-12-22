import psutil 

def system_health():
    
    # take threshold values from user
    cpu_threshold =float(input("Enter a cpu threshold: "))
    disk_threshold =float(input("Enter a disk threshold: "))
    memory_threshold =float(input("Enter a memory threshold: "))

    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"cpu_usage:{cpu_usage}")
    disk_usage = psutil.disk_usage('/')
    print(f"disk usage :{disk_usage.percent}")
    memory_usage = psutil.virtual_memory()
    print(f"memory usage:{memory_usage.percent}")

    if cpu_usage > cpu_threshold:
        print("cpu high , email send")
    else:
        print("cpu is safe")

    if disk_usage.percent > disk_threshold:
        print("disk high , email send")
    else:
        print("disk is safe")

    if memory_usage.percent > memory_threshold:
        print("Memory high , email send")
    else:
        print("Memory is safe")

system_health()