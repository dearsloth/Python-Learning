# pandas module
import pandas as pd

# 建立 series 
data = pd.Series([20, 10, 15, 30], index=["a", "b", "c", "d"])

# print("最大值:", data.max())
# print("總和:", data.sum())
# print("標準差:", data.std())
# print("中位數:", data.median())
# print("平均數:", data.mean())
# print("最大的2個值:", data.nlargest(2))
# print("最小的3個值:", data.nsmallest(3))

# print("資料型態:", data.dtype)
# print("資料數量:", data.size)
# print("資料索引:", data.index)

# print(data[1])  # 取第2筆資料
# print(data["c"])  # 取索引為c的資料

data20 = data == 20  # 看每個值是否等於20 (布林值)
# print(data20)


data = pd.Series(["蘋果", "Orange", "BANANA"])

# print(data.str.lower())  # 轉為小寫, 中文不影響
# print(data.str.len())  # 計算每個字串長度
# print(data.str.cat(sep=","))  # 串接所有字串並在字串間加入","
# print(data.str.contains("O"))  # 判斷各字串中是否包含大寫"O" (布林值)
# print(data.replace("蘋果","apple"))  # 把"蘋果"取代為"apple"

# =========================================================

# 建立 DataFrame
df=pd.DataFrame({
    "Id":[1,2,3],
    "Name":["Liz","Asa","Sana"]
}, index=["a", "b", "C"])

# print(df)

# print("資料數量:", df.size)  # 6
# print("資料型狀(列, 欄):", df.shape)  # (3,2)
# print("資料索引:", df.index)  # Index(['a', 'b', 'C'], dtype='object')

# print(df["Name"])  # [姓名]欄位所有內容
# print(df.iloc[0])  # 取第一行的值
# print(df.iloc[0,1])  # 取第一行, 第二欄的值
# print(df.loc["b"])  # 取得索引為b的資料
# print(df.loc[df["Id"]==2,"Name"])  # 取[Id]為2的姓名值

#print(df["Name"].str.upper())  # 把所有姓名轉成大寫


# 建立新欄位
df["Score"]=[90,100,80]  
# ascending=False: 分數越高，排名越前（1, 2, 3...）
# method="min" 代表如果有同分，排名會是一樣的（例如兩個人並列第二，就不會有第三名，下一個是第四名）
df["Rank"]=df["Score"].rank(ascending=False, method="min").astype(int)

# 依照 Rank 欄位排序
df = df.sort_values(by="Rank")
# 依照 Name 欄位由小到大 (A -> Z) 排序
df = df.sort_values(by="Name")
# 如果要 Z -> A 倒著排
df = df.sort_values(by="Name", ascending=False)

# print(df)


# =========================================================


# 篩選
# Series
data = pd.Series([20, 10, 15, 30])
condition = data>18
# print(condition)   # True  False  False  True
filteredData = data[condition]
# print(filteredData)  # 20  30 

data = pd.Series(["蘋果", "Orange", "BANANA"])
condition = data.str.contains("a")
# print(data[condition])  # Orange


# DataFrame
df=pd.DataFrame({
    "Id":[1,2,3],
    "Name":["Liz","Asa","Sana"],
    "Score":[90,100,80]
})
condition = df["Score"]>85
# print(df[condition])
# print(df["Name"][condition])
# print(df[df["Name"]=="Liz"])