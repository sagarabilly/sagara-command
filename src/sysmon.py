"""
TYPE : COMMAND LINE

----------SERVER SYSTEM----------
------CONFIG & STATUS CHECK------
=----64Bit UTF08 PYTHON 3.12----=
"""

import os
import platform
import re
import psutil
import socket
import uuid
import logging
import time

from argparse import ArgumentParser
from datetime import datetime


# ------------------------------------------------------------------------
def get_kernel_info():
    return {
        # Released": platform.uname().release,
        "system_name": platform.uname().system,
        "node_name": platform.uname().node,
        "machine": platform.uname().machine,
        "version": platform.uname().version,
    }


def get_memory_info():
    return {
        "total_memory": psutil.virtual_memory().total / (1024.0**3),
        "available_memory": psutil.virtual_memory().available / (1024.0**3),
        "used_memory": psutil.virtual_memory().used / (1024.0**3),
        "memory_percentage": psutil.virtual_memory().percent,
    }


def get_cpu_info():
    return {
        "physical_cores": psutil.cpu_count(logical=False),
        "total_cores": psutil.cpu_count(logical=True),
        "processor_speed": psutil.cpu_freq().current,
        "cpu_usage_per_core": dict(
            enumerate(psutil.cpu_percent(percpu=True, interval=1))
        ),
        "total_cpu_usage": psutil.cpu_percent(interval=1),
    }


def get_disk_info():
    partitions = psutil.disk_partitions()
    disk_info = {}
    for partition in partitions:
        partition_usage = psutil.disk_usage(partition.mountpoint)
        disk_info[partition.mountpoint] = {
            "total_space": partition_usage.total / (1024.0**3),
            "used_space": partition_usage.used / (1024.0**3),
            "free_space": partition_usage.free / (1024.0**3),
            "usage_percentage": partition_usage.percent,
        }
    return disk_info


def get_network_info():
    net_io_counters = psutil.net_io_counters()
    return {
        "bytes_sent": net_io_counters.bytes_sent,
        "bytes_recv": net_io_counters.bytes_recv,
    }


def get_load_average():
    load_avg_1, load_avg_5, load_avg_15 = psutil.getloadavg()
    return {
        "load_average_1": load_avg_1,
        "load_average_5": load_avg_5,
        "load_average_15": load_avg_15,
    }


def get_disk_io_counters():
    io_counters = psutil.disk_io_counters()
    return {
        "read_count": io_counters.read_count,
        "write_count": io_counters.write_count,
        "read_bytes": io_counters.read_bytes,
        "write_bytes": io_counters.write_bytes,
        "read_time": io_counters.read_time,
        "write_time": io_counters.write_time,
    }


def get_net_io_counters():
    io_counters = psutil.net_io_counters()
    return {
        "bytes_sent": io_counters.bytes_sent,
        "bytes_recv": io_counters.bytes_recv,
        "packets_sent": io_counters.packets_sent,
        "packets_recv": io_counters.packets_recv,
        "errin": io_counters.errin,
        "errout": io_counters.errout,
        "dropin": io_counters.dropin,
        "dropout": io_counters.dropout,
    }


def get_system_uptime():
    boot_time_timestamp = psutil.boot_time()
    current_time_timestamp = time.time()
    uptime_seconds = current_time_timestamp - boot_time_timestamp
    uptime_minutes = uptime_seconds // 60
    uptime_hours = uptime_minutes // 60
    uptime_days = uptime_hours // 24
    uptime_str = f"{int(uptime_days)} days, {int(uptime_hours % 24)} hours, {int(uptime_minutes % 60)} minutes, {int(uptime_seconds % 60)} seconds"
    return {"uptime": uptime_str}


# -----------------------------------INFO SUMMARY-------------------------------
def serversyst_info():
    global info
    info = {}
    try:
        info["Hostname"] = socket.gethostname()
        info["Ip-address"] = socket.gethostbyname(socket.gethostname())
        info["Mac-address"] = ":".join(re.findall("..", "%012x" % uuid.getnode()))
        info["Platform"] = platform.system()
        info["Platform-release"] = platform.release()
        info["Platform-version"] = platform.version()
        info["Architecture"] = platform.machine()
        info["Processor"] = platform.processor()
        info["RAM"] = str(round(psutil.virtual_memory().total / (1024.0**3))) + " GB"
        return info
    except Exception as e:
        logging.exception(e)
    pass


# ---------------------------------COMMAND LINE ASSEMBLY---------------------------
def command_line(run_on_execute=True):
    if run_on_execute == True:
        cli_parser = ArgumentParser(
            description="""A Simple Server System Check [by: Sagara_Billy]. 
                                    \n Please use --info to get all the system summary"""
        )
        cli_parser.add_argument(
            "-i",
            "--info",
            action="store_true",
            required=False,
            help="showing the system information summary",
        )
        cli_parser.add_argument(
            "-m",
            "--memory",
            action="store_true",
            required=False,
            help="showing memory status",
        )
        cli_parser.add_argument(
            "-c",
            "--cpu",
            action="store_true",
            required=False,
            help="showing cpu status",
        )
        cli_parser.add_argument(
            "-d",
            "--disk",
            action="store_true",
            required=False,
            help="showing disk status",
        )
        cli_parser.add_argument(
            "-b",
            "--boot",
            action="store_true",
            required=False,
            help="showing boot uptime status",
        )
        cli_parser.add_argument(
            "-la",
            "--loadaverage",
            action="store_true",
            required=False,
            help="showing load average status",
        )
        cli_parser.add_argument(
            "-n",
            "--network",
            action="store_true",
            required=False,
            help="showing network status",
        )
        cli_parser.add_argument(
            "-k",
            "--kernel",
            action="store_true",
            required=False,
            help="showing kernel status",
        )

        args = cli_parser.parse_args()

    return (
        args.info,
        args.memory,
        args.cpu,
        args.disk,
        args.boot,
        args.loadaverage,
        args.network,
        args.kernel,
    )


def show(info):
    print("-------------------------------------------------------------")
    lines = [f"{key}: {value}" for key, value in info.items()]
    return print("\n".join(lines))


# ------------------------------------MAIN CALL----------------------------------
if __name__ == "__main__":
    info, mem, cpu, disk, boot, loadaverage, network, kernel = command_line(
        run_on_execute=True
    )
    print(f"----- Server System Check on {datetime.now()} -----")

    # LAZY PROGRAMMING >_<
    if info:
        info = serversyst_info()
        show(info)
    if mem:
        mem = get_memory_info()
        show(mem)
    if cpu:
        cpu = get_cpu_info()
        show(cpu)
    if disk:
        disk = get_disk_info()
        show(disk)
        disk2 = get_disk_io_counters()
        show(disk2)
    if boot:
        boot = get_system_uptime()
        show(boot)
    if loadaverage:
        loadaverage = get_load_average()
        show(loadaverage)
    if network:
        network1 = get_network_info()
        show(network1)
        network2 = get_net_io_counters()
        show(network2)
    if kernel:
        kernel = get_kernel_info()
        show(kernel)
