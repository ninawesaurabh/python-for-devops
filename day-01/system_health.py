import psutil

def check_cpu_threshold():
    cpu_threshold = float(input("Enter CPU threshold: "))
    current_cpu = psutil.cpu_percent(interval=1)
    print("Current CPU %:", current_cpu)
    if current_cpu > cpu_threshold:
        print("WARNING")
    else:
        print("OK")


check_cpu_threshold()