import os
import pandas as pd

def fun_600_Boston(num):
    original_path = r'C:\Users\zzliv\Desktop\Target Folder'
    target_path = r'C:\Users\zzliv\Desktop\Boston Folder'

    file_list = os.listdir(original_path)
    original_file = pd.read_csv(original_path + os.sep + file_list[num])
    if original_file[original_file['CITYHCR']=='Boston'].__len__()>600:
        original_file.to_csv(target_path + os.sep + file_list[num])
        os.remove(original_path + os.sep + file_list[num])

if __name__ == '__main__':
    import multiprocessing
    import datetime

    cores = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=cores)
    starttime = datetime.datetime.now()
    pool.map(fun_600_Boston, range(8))
    endtime = datetime.datetime.now()
    print(endtime - starttime)