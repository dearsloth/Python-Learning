# 包含數字運算，字串運算，List，Tuple，Set，Dictionary


# 數字運算
A1 = 100//3   # 整除 33
A2 = 100/3   # 33.3333...

B1 = 2**3  #2的3次方 8

C1 = 7%3  #7除以3的餘數 1

# ===================================================

# 字串運算
s1 = "Hell\"o"  # 跳脫 Hell"o 
s2 = "Hello"+"World" # Hello World
s3 = "Hello" "World" #HelloWorld

s4 = "Hello\nWorld" # 換行
s5 = """Hello
World"""  # 換行

s6 = "Hello"*3 + "World"  # HelloHelloHelloWorld

s = "Hello"
#print(s[0])   # H
#print(s[1:3])  # el
#print(s[:3])  # Hel
#print(s[2:])  # llo

# ==================================================

# 有序可變動列表 List
score = [90, 88, 63, 70, 100]
#print(score[1])  # 列表中的index 1  88
#print(len(score))  # 列表長度 5

# 直接修改score列表index 0 的值
score[0] = 77   
#print(score)  # [77, 88, 63, 70, 100]
score[1:4] = []  
#print(score)  # [77, 100]
score = score + [87, 88]  
#print(score)  # [77, 100, 87, 88]

# 修改原本列表 index 0 的值, 並另存成score1
score1 = score.copy()
score1[0] = 80
#print(score1)  # [80, 88, 63, 70, 100]

# 巢狀列表
data = [[1,2,3],[4,5,6]]
#print(data[0])  # [1, 2, 3]
#print(data[0][1])  # 2
#print(data[0][0:2])  # [1, 2]



# 有序不可變動列表 Tuple
data = (3,4,5)
#data[0] = 10 # 錯誤:Tuple的資料不可變動

# ==============================================================

# 集合的運算
a1 = {3,4,5}
#print(3 in a1)  # True
#print(3 not in a1)  # False
a2 = {4,5,6,7}

a3 = a1&a2  # 交集:取兩個集合中,相同的部分 
#print(a3)  #{4, 5}

a4 = a1|a2  # 聯集:取兩個集合中所有資料,但不重複
#print(a4)  # {3, 4, 5, 6, 7}

a5 = a1-a2  # 差集:從a1中,減去與a2重疊的部分
#print(a5)  # {3}

a6 = a1^a2 # 反交集:取兩個集合中,不重疊的部分
#print(a6)  # {3, 6, 7}

a = set("Hello")  # 拆解字串成集合,且不重複內容
#print(a)  # {'l', 'e', 'o', 'H'}

# ==============================================================

# 字典的運算
dic = {"apple":"蘋果", "bug":"蟲蟲"}
#print(dic)  # {'apple': '蘋果', 'bug': '蟲蟲'}
#print(dic["apple"])  # 蘋果
#print("apple" in dic)  # True
#print("蘋果" in dic)  # False (只針對key值)
#print("蘋果" in dic["apple"])  # True

dic["apple"] = "小蘋果"
#print(dic)  # {'apple': '小蘋果', 'bug': '蟲蟲'}

del dic["apple"]  #刪除鍵值對
#print(dic)  # {'bug': '蟲蟲'}

dic1 = {x:x**2 for x in [1,2,3]}  # 從列表中產生字典
print(dic1)  # {1: 1, 2: 4, 3: 9}
