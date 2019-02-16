import numpy as np
import pandas as pd
import itertools

num_packages = 8
delivery_sequence = ['1234-1', '1234-2', '1235-2', '1235-3', '1234-4', '1235-5', '1235-8', '1234-10']
def fun(num_packages,delivery_sequence):
    list_grid = [delivery_sequence[i][:4] for i in range(num_packages)]
    list_number = [int(delivery_sequence[i][5:]) for i in range(num_packages)]
    df = pd.DataFrame({'grid':list_grid,'number':list_number})
    df.insert(2,'movingTime',0)
    for i in range(2):
        list_temp = list(df.groupby('grid'))[i]
        array_temp = list_temp[1]['number'].values - np.hstack((np.array([1]), (list_temp[1]['number'].values[:len(list_temp[1]['number']) - 1])))
        df.loc[df.loc[:, 'grid'] == list_temp[0],'movingTime']=array_temp
    realTime = []
    movingTime = df.iloc[:,2]
    n = 0
    for i in range(num_packages):
        if i == 0 or df.iloc[i,0] == df.iloc[i-1,0]:
            realTime.append(movingTime[i] + 1)
            n = n + 1
        else:
            realTime.append(max(0,movingTime[i]-sum(realTime[i-n:])) + 1)
            n = 1
    return (sum(realTime))

num_days,demands,max_capacity,shipping_cost,price,overnight_cost = 5,[1,2,3,2,1],5,20,1,1
num_days,demands,max_capacity,shipping_cost,price,overnight_cost = 3,[1,1,1],5,3,2,1

def fun_3(num_days,demands,max_capacity,shipping_cost,price,overnight_cost):
    total_demands = sum(demands)
    up_limit = min(total_demands,max_capacity)
    possible_result = list(itertools.product(list(range(0,up_limit+1)), repeat=num_days))
    possible_result = [item for item in possible_result if max(np.cumsum(item) - np.cumsum(demands)) <= 5 and sum(item)==total_demands and min(list(np.cumsum(item)- np.cumsum(demands))) >= 0]
    def fun_cost(item):
        cost = total_demands * price + sum(np.cumsum(item) - np.cumsum(demands)) * overnight_cost + (num_days - item.count(0)) * shipping_cost
        return (cost)
    possible_cost = list(map(fun_cost,possible_result))
    return(min(possible_cost))

hand = 111

from scipy.stats import mode
# Complete the p1_win_count function below.
def p1_win_count(hands):
    def fun_type(hand):
        if set(hand).__len__()==1:
            return 3
        elif  set(hand).__len__()==2:
            return 2
        else:
            return 1
    def find_pair(hand):
        count = {}
        for i in set(hand):
            count[i] = hand.count(i)
        for k, v in count.items():
            if v == max(count.values()):
                return (k)
    def find_alone(hand):
        count = {}
        for i in set(hand):
            count[i] = hand.count(i)
        for k, v in count.items():
            if v != max(count.values()):
                return (k)
    result = 0
    for hand in hands:
        p1 =hand[:3]
        p2 =hand[3:]
        if fun_type(p1)>fun_type(p2):
            result += 1
        elif fun_type(p1) == 3:
            if p1[0] > p2[0]:
                result += 1
        elif fun_type(p1) == 2:
            num_pair_1 = find_pair(p1)
            num_pair_2 = find_pair(p2)
            num_alone_1 =find_alone(p1)
            num_alone_2 = find_alone(p2)
            if num_pair_1 > num_pair_2 or (num_pair_1==num_pair_2 and num_alone_1>num_alone_2):
                result += 1
        else:
            if max(p1) > max(p2) or (max(p1) == max(p2) and sorted(p1)[1]>sorted(p2)[1]) or (max(p1) == max(p2) and sorted(p1)[1]==sorted(p2)[1] and min(p1)>min(p2)):
                result += 1
    return result


# Complete the function below.
side_length, lake_grid, albert_row, albert_column, kuna_row, kuna_column = 7,[[0, 0, 0, 0, 0, 0, 0], [0, 0, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, -1, 0], [-1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 1, 0], [-1, 0, -1, 0, -1, 0, 0], [0, 0, 0, 0, 0, 0, 0]],4,2,2,2
def escape(side_length, lake_grid, albert_row, albert_column, kuna_row, kuna_column):
    lake_grid[kuna_row-1][kuna_column-1] = 1
    points = [[albert_row-1,albert_column-1]]
    i = 0
    status = 1
    def next_step(point):
        if 1 not in lake_grid[point[0]][:] and 1 not in lake_grid[:][point[1]]:
            return (0)
        elif lake_grid[:][point[1]].index(1):
            return (1)
    while status == 1:
        status = next_step(points[i])
        i += 1


    return (status)
df = pd.read_csv()