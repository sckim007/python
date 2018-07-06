# -*- coding: utf-8 -*-
import psutil
import datetime, time
import signal
import sys
import csv
import os


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class ngle_util:
    def __init__(self):
        pass

    def signal_handler(self, signal, frame):
        print('signal_handler : lose nGle Sys Mon')
        sys.exit(0)

    def change_B_to_K(self, ebyte):
        return int(ebyte / 1024)

    def change_B_to_M(self, ebyte):
        return int((ebyte / 1024) / 1024)

    def change_color(self, comm):
        if 80.0 <= comm <= 100.0:
            strComm = bcolors.FAIL + str(comm) + "%" + bcolors.ENDC
        elif 70.0 <= comm <= 79.9:
            strComm = bcolors.WARNING + str(comm) + "%" + bcolors.ENDC
        else:
            strComm = str(comm) + "%"

        return strComm

    def get_date(self, date_when='today'):
        today = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d')

        if date_when == "today":
            date = today
        else:
            date = today

        return date


class view_psutil_members:
    def __init__(self):
        self.ngle = ngle_util()
        self.gpm = get_psutil_members()

    def viewer(self):
        print
        "%s\t%s\t%s\t%d" % (
            self.gpm.get_time(),
            self.ngle.change_color(self.gpm.get_cpu_percent()),
            self.ngle.change_color(self.gpm.get_mem_virtual().percent),
            self.gpm.get_net_port_counter(80, 443, 8080)
        )


class set_file_members:
    def __init__(self):
        self.ngle = ngle_util()
        self.gpm = get_psutil_members()

    def set_file(self):
        file_name = "nGle_sys_{}".format(self.ngle.get_date())
        top_title = [
            "time",
            "cpu_times.user",
            "cpu_times.system",
            "cpu_times.idle",
            "cpu_percent(%)",
            "cpu_percent_per_cpu",
            "mem_virtual.total(Mbyte)",
            "mem_virtual.available(Mbyte)",
            "mem_virtual.used(Mbyte)",
            "mem_virtual.free(Mbyte)",
            "mem_virtual.percent(%)",
            "mem_swap.total(Mbyte)",
            "mem_swap.used(Mbyte)",
            "mem_swap.free(Mbyte)",
            "mem_swap.percent(%)",
            "disk_io.read_count",
            "disk_io.write_count",
            "disk_io.read(Mbyte)",
            "disk_io.write(Mbyte)",
            "net_io.sent(Mbyte)",
            "net_io.recv(Mbyte)",
            "net_io.packets_sent",
            "net_io_counters.packets_recv",
            "net_port_counter(80 443 8080)"
        ]

        if os.path.exists(file_name):
            with open(file_name, "a+") as f:
                writer = csv.writer(f, delimiter='\t', quotechar='\n', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(self.get_psutil())
        else:
            with open(file_name, "a+") as f:
                writer = csv.writer(f, delimiter='\t', quotechar='\n', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(top_title)

    def get_psutil(self):

        items = list()

        items = [
            self.ngle.get_date(),
            self.gpm.get_cpu_times().user,
            self.gpm.get_cpu_times().system,
            self.gpm.get_cpu_times().idle,
            self.gpm.get_cpu_percent(),
            self.gpm.get_cpu_percent_per_cpu(),
            self.ngle.change_B_to_M(self.gpm.get_mem_virtual().total),
            self.ngle.change_B_to_M(self.gpm.get_mem_virtual().available),
            self.ngle.change_B_to_M(self.gpm.get_mem_virtual().used),
            self.ngle.change_B_to_M(self.gpm.get_mem_virtual().free),
            self.gpm.get_mem_virtual().percent,
            self.ngle.change_B_to_M(self.gpm.get_mem_swap().total),
            self.ngle.change_B_to_M(self.gpm.get_mem_swap().used),
            self.ngle.change_B_to_M(self.gpm.get_mem_swap().free),
            self.gpm.get_mem_swap().percent,
            self.gpm.get_disk_io_counters().read_count,
            self.gpm.get_disk_io_counters().write_count,
            self.ngle.change_B_to_M(self.gpm.get_disk_io_counters().read_bytes),
            self.ngle.change_B_to_M(self.gpm.get_disk_io_counters().write_bytes),
            self.ngle.change_B_to_M(self.gpm.get_net_io_counters().bytes_sent),
            self.ngle.change_B_to_M(self.gpm.get_net_io_counters().bytes_recv),
            self.gpm.get_net_io_counters().packets_sent,
            self.gpm.get_net_io_counters().packets_recv,
            self.gpm.get_net_port_counter(80, 443, 8080)
        ]

        return items


class get_psutil_members:
    '''
    https://pythonhosted.org/psutil/
    '''

    def __init__(self):
        pass

    def get_cpu_times(self):
        return psutil.cpu_times()

    def get_cpu_percent(self):
        return psutil.cpu_percent(interval=1)

    def get_cpu_percent_per_cpu(self):
        return psutil.cpu_percent(percpu=True)

    def get_mem_virtual(self):
        return psutil.virtual_memory()

    def get_mem_swap(self):
        return psutil.swap_memory()

    def get_disk_io_counters(self):
        return psutil.disk_io_counters()

    def get_net_io_counters(self):
        return psutil.net_io_counters()

    def get_net_connections(self):
        return psutil.net_connections(kind='inet')

    def get_net_port_counter(self, *args):
        port_counter = 0
        for c in psutil.net_connections(kind='inet'):
            if c.status == "ESTABLISHED":
                if c.laddr[1] in args:
                    port_counter += 1

        return port_counter

    def get_process(self):
        p = psutil.Process()
        return p.name()


if __name__ == "__main__":
    ng = ngle_util()
    signal.signal(signal.SIGINT, ng.signal_handler)

    while True:
        set_file_members().set_file()
        time.sleep(5)

    # while True:
    #   view_psutil_members().viewer()
    #   time.sleep(2)