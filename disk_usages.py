import shutil

def disk_usages():
    usage = shutil.disk_usage("C:/")
    free_space = usage.free/usage.total*100
    return 'Disk usages in GB: {}'.format(usage)+'\n'+'Free space: {} GB'.format(free_space)

print(disk_usages())
