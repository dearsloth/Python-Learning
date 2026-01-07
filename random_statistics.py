# 亂數與統計模組

# 亂數模組 random module
import random
# 隨機選取
lista=[1,4,5,7,8,10]
data = random.choice(lista)  # 隨機取一個
# print(data)

data1 = random.sample(lista,3)  # 隨機取三個
# print(data1)   # [7, 5, 10]

random.shuffle(lista)  # 隨機調換順序(洗牌)
# print(lista)

data2 = random.random()  # 0.0 ~ 0.1 之間的隨機亂數
# print(data2)  # 0.6681262819613584

data3 = random.uniform(60, 100) # 60 ~ 100 之間的隨機亂數
# print(data3)  # 89.9256557907774

data4 = random.normalvariate(100, 10)  # 取得常態分佈亂數(平均數100, 標準差10, 得到的資料多數會落在90~110之間)
# print(data4)  # 104.06883026385897


# ============================================================================================================


# 統計模組 statistics moudle
import statistics as stat
listb = [1,4,5,8,9,11,100]

data = stat.mean(listb)  # 取平均數
# print(data)  # 19.714285714285715


data = stat.median(listb)  # 取中位數
# print(data)  # 8

data = stat.stdev(listb)  # 取標準差
# print(data)  # 35.560813103350554
