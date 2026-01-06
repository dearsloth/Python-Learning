# 流程控制(包含if, while, for等)

# 判斷式
# x=input("請輸入數字:")  # 取得字串形式的使用者輸入
# x=int(x)  # 將字串轉為數字型態
# if x>100:
#     print("大於 100")
# elif x==100:
#     print("等於 100")
# else:
#     print("小於等於 100")

# 四則運算
# n1 = int(input("請輸入數字一:"))
# n2 = int(input("請輸入數字二:"))
# op = input("請輸入運算: +, -, *, /")
# if op=="+":
#     print(n1+n2)
# elif op=="-":
#     print(n1-n2)
# elif op=="*":
#     print(n1*n2)
# elif op=="/":
#     print(n1/n2)
# else:
#     print("輸入錯誤")

# ==================================================

# while 迴圈
# n = 1
# sum = 0
# while n<=3:
#     print(n)
#     sum=sum+n
#     n+=1
# print("總和:",sum)



# for迴圈
# for x in [2,4,6]:
#     print(x)   # 2  4  6

# for x in "Hello":
#     print(x)   # H  e  l  l  o

# for x in range(5):
#     print(x)  # 0  1  2  3  4

# for x in range(5, 10):
#     print(x)  # 5  6  7  8  9

# 1加到10
# sum=0
# for x in range(11):
#     sum+=x
# print(sum)

# ====================================================

# break 用法
# n=0
# while n<=5:
#     if n==3:
#         break  # 一旦達成n==3,整個while會完全被終止
#     print(n)
#     n+=1
# print("合計(不含3):",n)


# continue 用法
# sum=0
# for x in range(10):
#     if x%2==0:  # x除以2的餘數為0(x為偶數)
#         continue  # 跳過
#     print(x)
#     sum+=x
# print("總和:",sum)
    

# else 用法
# sum = 0
# for x in range(11):
#     sum+=x
# else:
#     print(sum)
    

# 找出整數平方根 (如:輸入9 得到3; 輸入11 得到"沒有整數平方根")
# n=int(input("輸入一個正整數:"))
# for i in range(n+1):
#     if i*i==n:
#         print("整數平方根為:",i)
#         break
# else:
#     print("沒有整數平方根")
