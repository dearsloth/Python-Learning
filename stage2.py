# 定義函式
# 型態1:乘法(return)
# def multiply(n1,n2):
#     print(n1*n2)
#     return

# multiply(2,3)   #會直接得到6

# value=multiply(2,3)
# print(value)  # 會生成none


# 型態2:乘法(return "10(預設值)")
# def multiply(n1,n2):
#     print(n1*n2)
#     return "10(預設值)"

# multiply(2,3)   #會直接得到6

# value=multiply(2,3)
# print(value)  # 會生成 "10(預設值)"


# 型態3:乘法(只有return n1*n2, 沒有加入print)
# def multiply(n1,n2):
#     return n1*n2

# # multiply(2,3)   #不會得到值,因為函式中沒有print

# value=multiply(2,3)  #不會得到值,因為函式中沒有print
# print(value)  # 會生成 6

# value1=multiply(2,3)+multiply(4,5)
# print(value1)  # 會生成 26

# =======================================================

# 程式的包裝
# 從a1加到a2
# def calculate(a1,a2):
#     sum=0
#     for n in range(a1,a2+1):
#         sum+=n
#     return sum

# print(calculate(1,10))

# ========================================================

# 參數的預設資料
# def power(base,exp=0):  # 預設開方值為0
#     print(base**exp)

# power(4,2)  # 16
# power(4)   # 1


# 無限/不定 參數資料
# 計算不確定長度之列表的平均數
# def avg(*ns):  # *ns代表Tuple
#     sum=0
#     for n in ns:
#         sum+=n
#     print(sum/len(ns))

# avg(3,4)
# avg(1,4,7)


