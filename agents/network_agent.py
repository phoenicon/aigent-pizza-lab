import psutil
import json
import time

def get_system_metrics():
    data = {
        "cpu": psutil.cpu_percent(),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage("/").percent,
        "network_sent": psutil.net_io_counters().bytes_sent,
        "network_recv": psutil.net_io_counters().bytes_recv
    }
    return data

while True:
    metrics = get_system_metrics()
    print(json.dumps(metrics))
    time.sleep(2)
