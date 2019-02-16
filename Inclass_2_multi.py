import multiprocessing
from Inclass_2 import *
import datetime

cores = multiprocessing.cpu_count()
pool = multiprocessing.Pool(processes=cores)
starttime = datetime.datetime.now()
pool.map(fun_600_Boston, range(8))
endtime = datetime.datetime.now()
print(endtime - starttime)