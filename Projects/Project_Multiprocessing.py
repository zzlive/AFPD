import multiprocessing
from Projects.Project_Fuzzy import *

if __name__ == '__main__':
    # Multiprocessing
    cores = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=cores)
    n = 92 // cores + 1
    n_list = [i*n for i in range(8)]
    # using 1 by 1 method
    results = pool.map(fun_match,n_list)
    result = pd.concat(results)
    # using process.extract
    results_2 = pool.map(fun_match_2,n_list)
    result_2 = pd.concat(results_2)

    # Export result
    path = r'C:\便捷\工作\Course\MFIN7033 Advanced Financial Programming and Databases\2018 Fall Projects\Fuzzy and multiprocessing\data'
    result.to_csv(os.path.join(path, 'fuzzymatching_output_data.csv'))
    result_2.to_csv(os.path.join(path, 'fuzzymatching_output_data_2.csv'))
