import platform
import socket
import psutil
import cpuinfo
import GPUtil




def getSystemInfo():
    print("———- System Info ———-")

    hostname = socket.gethostname()
    print(f"Hostname : {hostname}")

    system = platform.system()
    arch = platform.machine()
    kernel = platform.release()
    compiler = platform.python_compiler()

    print(f"System : {system} {arch}")
    print(f"Kernel : {kernel}")
    print(f"Compiler : {compiler}")

    cpu = cpuinfo.get_cpu_info()
    cpu_name = cpu["brand_raw"]
    cpu_cores = psutil.cpu_count(logical=False)
    cpu_threads = psutil.cpu_count(logical=True)
    print(f"CPU : {cpu_name} ({cpu_cores} Cores, {cpu_threads} Threads)")

    ram = psutil.virtual_memory().total / (1024 ** 3)
    print(f"Memory : {ram:.1f} GiB")


    disk = psutil.disk_usage('/')
    disk_total = disk.total / (1024 ** 3)
    print(f"Disk : {disk_total:.1f} GiB")


def getGpuInfo():
    print("\n———- GPU ———-")
    gpus = GPUtil.getGPUs()

    if not gpus:
        print("No information! Probably the GPU is onboard!")
    else:
        for gpu in gpus:
            print(f"GPU : {gpu.name} ({gpu.memoryTotal:.1f} GiB VRAM)")


def getUsageInfo():
    print("\n———- RAM & Disk usage ———-")


    ram = psutil.virtual_memory()
    ram_used = ram.used / (1024 ** 3)
    ram_total = ram.total / (1024 ** 3)
    ram_percent = ram.percent
    print(f"RAM Used : {ram_used:.1f} GiB / {ram_total:.1f} GiB ({ram_percent}%)")


    disk = psutil.disk_usage('/')
    disk_used = disk.used / (1024 ** 3)
    disk_total = disk.total / (1024 ** 3)
    disk_percent = disk.percent
    print(f"Disk Used : {disk_used:.1f} GiB / {disk_total:.1f} GiB ({disk_percent}%)")


if __name__ == "__main__":
    getSystemInfo()
    getGpuInfo()
    getUsageInfo()

