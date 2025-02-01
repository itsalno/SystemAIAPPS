import platform
import socket
import psutil
import cpuinfo
import GPUtil


class SystemInfo:

    def __init__(self):
        self.hostname = socket.gethostname()
        self.system = platform.system()
        self.arch = platform.machine()
        self.kernel = platform.release()
        self.compiler = platform.python_compiler()

    def getSystemInfo(self):
        print("———- System Info ———-")
        print(f"Hostname : {self.hostname}")
        print(f"System : {self.system} {self.arch}")
        print(f"Kernel : {self.kernel}")
        print(f"Compiler : {self.compiler}")

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

    def getGpuInfo(self):
        print("\n———- GPU ———-")
        gpus = GPUtil.getGPUs()

        if not gpus:
            print("No information! Probably the GPU is onboard!")
        else:
            for gpu in gpus:
                print(f"GPU : {gpu.name} ({gpu.memoryTotal:.1f} GiB VRAM)")

    def getUsageInfo(self):
        print("\n———- RAM & Disk Usage ———-")

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
    system_info = SystemInfo()
    system_info.getSystemInfo()
    system_info.getGpuInfo()
    system_info.getUsageInfo()
