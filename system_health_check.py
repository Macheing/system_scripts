# import system libraries
import psutil, shutil

def check_disk_usage():
    ''' check free disk space'''
    print()
    print('============== TEST PARAMETERS! ===============')
    check = shutil.disk_usage("C:/")
    free = check.free/check.total*100
    print('Free Disk Space:', free,'GB')
    return free > 30

def check_cpu_usage():
    '''Check if CPU is overloaded.'''
    for i in range(1,30):
        usage = psutil.cpu_percent(interval=i)
        print("CPU Usage:",usage,'%')
        if usage < 75:
            return True
        else:
            return False
    
def health_check():
    '''Check health of system'''
    disk_status = check_disk_usage()
    cpu_status = check_cpu_usage()
    print()
    print('============== TEST OUTCOME! ===============')
    
    if disk_status != True and cpu_status != True:
        return ("ERROR!: Test Fail!\nIs Free Disk Space > 30 GB: {}. \nIs CPU Usage < 75%: {}".format(disk_status,cpu_status))
    else:
        return ("Success!: Test Pass!\nIs Free disk space > 30 GB: {}. \nIs CPU usage < 75%: {}.".format(disk_status,cpu_status))

print(health_check())