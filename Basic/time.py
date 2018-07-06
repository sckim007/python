import sys
import time
import signal
import psutil


start = time.time()
time.sleep(1)
print("took time : ", str(time.time() - start))

class MonitorResource:

    def signal_handler(self, signal, frame):
        print("Signal Handling, Signal = ", signal)
        sys.exit(0)

    def scan_resource(self):
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()[2]
        swap = psutil.swap_memory()[3]
        line = "CPU  : {}%, ".format(cpu)
        line += "MEM  : {}%, ".format(memory)
        line += "SWAP : {}%, ".format(swap)
        sys_dict = dict()
        sys_dict['cpu'] = float(cpu)
        sys_dict['memory'] = float(memory)
        sys_dict['swap'] = float(swap)
 #       print("dictionary : ", sys_dict)
        line += "DISK ["

        disks = psutil.disk_partitions()
        disk_dict = dict()
        for disk in disks:
            if disk.fstype is '':
                break
            disk_name = disk.mountpoint
            disk_usage = psutil.disk_usage(disk.mountpoint)[3]
            line += "{}:{}% ".format(disk_name, disk_usage)
            disk_dict[disk.mountpoint] = disk_usage
        line += "]"
        sys_dict['disk'] = disk_dict
#        print("dictionary : ", sys_dict)

        return sys_dict, line

    def run(self):
        while True:
            result_dict, result_str = self.scan_resource()
            print(">> dictionary : ", result_dict)
            print(">> string     : ", result_str)
            #time.sleep(1)

if __name__ == "__main__":
    mon = MonitorResource()
    signal.signal(signal.SIGINT, mon.signal_handler)
    signal.signal(signal.SIGTERM, mon.signal_handler)
    mon.run()