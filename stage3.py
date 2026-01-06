# txt

# 1. 新建立檔案
# 寫法1
# file=open("./data_stage3/words.txt", mode="w")  # 開啟
# file.write("Hello File")  # 寫入
# file.close() # 關閉

# 寫法2
# with open("./data_stage3/words.txt", mode="w", encoding="utf-8") as file:
#     file.write("Hello File\n中文好棒棒")

# with open("./data_stage3/numbers.txt", mode="w") as file:
#     file.write("3\n6\n9\n12\n15")


# 2. 讀取檔案
# with open("./data_stage3/words.txt", mode="r", encoding="utf-8") as file:
#     print(file.read())

# 霸檔案中的數字,逐行讀取出來,計算總和
# sum=0
# with open("./data_stage3/numbers.txt", mode="r") as file:
#     for line in file:  # 逐行讀取
#         sum+=int(line)
# print(sum)


# 3. 增加內容 (使用 mode="a" 開啟檔案)
# with open("./data_stage3/words.txt", mode="a", encoding="utf-8") as file:
#     file.write("\n這是新加入的內容")


# 4. 修改內容
# with open("./data_stage3/words.txt", mode="r", encoding="utf-8") as file:
#     content = file.read()
# new_content = content.replace("Hello", "Hi")
# with open("./data_stage3/words.txt", mode="w", encoding="utf-8") as file:
#     file.write(new_content)



# =====================================================================================


# json
# import json
# 新建檔案
# new_data = {
#     "Project": "Python Learning",
#     "Stage": 3,
#     "Status": "Completed"
# }
# with open("./data_stage3/project.json", mode="w", encoding="utf-8") as file:
#     json.dump(new_data, file)

# 讀取
# with open("./data_stage3/config.json", mode="r") as file:
#     data=json.load(file)
#     print(data)    # {'name': 'User Name', 'id': 'User ID'}
#     print("name:",data['name'])   # name: User Name

# 修改資料
# data["name"]="Eric"
# print("name:",data['name'])
# 新增一組key-value
# data["Password"] = "User Password"
# 把最新的修改儲存
# with open("./data_stage3/config.json", mode="w") as file:
#     json.dump(data, file)


# =========================================================================


# csv (excel就是把csv部分改成excel)
# import pandas as pd
# 新建
# data = {
#     "Name": ["Eric", "Tom", "Alice"],
#     "Age": [25, 30, 22],
#     "City": ["Taipei", "Tokyo", "London"]
# }
# df = pd.DataFrame(data)
# 加 index=False 是為了不要讓 CSV 多出一欄 0, 1, 2 的索引
# df.to_csv("./data_stage3/employees_info.csv", index=False, encoding="utf-8-sig")


# 讀取
# df = pd.read_csv("./data_stage3/employees_info.csv", encoding="utf-8-sig")
# print(df)           # 顯示完整內容
# print(df.head(2))   # 只看前兩行
# print(df["Name"])   # 只抓取 "Name" 這一欄


# 新增 (一定要加 index=False, header=False)
# new_data = {
#     "Name": ["Bob"],
#     "Age": [28],
#     "City": ["New York"]
# }
# df_new = pd.DataFrame(new_data)
# df_new.to_csv("./data_stage3/employees_info.csv", mode='a', index=False, header=False, encoding="utf-8-sig")


# 修改
# df = pd.read_csv("./data_stage3/employees_info.csv", encoding="utf-8-sig")
# 範例1：將名字是 "Eric" 的那一行，年齡 (Age) 改成 30
# df.loc[df['Name'] == 'Eric', 'Age'] = 30
# 範例2：直接修改第二行、第一欄的資料 (索引從 0 開始)
# df.iloc[1, 0] = 'Cindy'
# 覆寫回去 (mode="w" 是預設)
# df.to_csv("./data_stage3/employees_info.csv", index=False, encoding="utf-8-sig")