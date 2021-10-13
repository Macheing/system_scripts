
import psutil

def cpu_usage(time_interval):
    usage = psutil.cpu_percent(time_interval)
    return "CPU usage per time interval of {} is: {:.2f} %.".format(time_interval,usage)

for i in range(1,11):
    print(cpu_usage(i))
    
