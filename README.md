# Python 基礎語法實作紀錄

這個專案紀錄了我學習 Python 基礎語法的過程，包含核心資料型態的運作與邏輯控制的練習。

## 📂 檔案清單與內容說明

### 1. 核心基礎運算 (`operations_list_tuple.py`)
此檔案涵蓋了 Python 最基礎且重要的資料操作，包含：

#### 數字運算 (Numbers)
* 包含整除 (`//`)、次方 (`**`)、以及取餘數 (`%`) 的實作。
* 範例：`100 // 3` 得到整數商；`2 ** 3` 計算乘冪。

#### 字串處理 (Strings)
* **跳脫字元：** 處理字串內的引號。
* **字串拼接與重複：** 使用 `+` 與 `*` 進行字串組合。
* **切片技術 (Slicing)：** 利用 `[start:end]` 擷取子字串，如 `s[1:3]`。

#### 資料結構實作 (Data Structures)
* **List (列表):** 實作有序且可變動的資料集，包含索引修改、範圍刪除與 `copy()` 複製技術。
* **Tuple (元組):** 了解其「不可變動 (Immutable)」的特性。
* **Set (集合):** 深入練習集合運算：
    * 交集 (`&`)、聯集 (`|`)、差集 (`-`)、反交集 (`^`)。
* **Dictionary (字典):** * 練習鍵值對 (Key-Value) 的增刪查改。
    * 實作 **字典推導式 (Dictionary Comprehension)**：`{x:x**2 for x in [1,2,3]}`。

---

### 2. 流程控制邏輯 (`conditionals_loops.py`)
* **條件判斷:** `if`, `elif`, `else` 邏輯分支。
* **迴圈結構:** `while` 條件迴圈與 `for` 迭代迴圈。
* **進階控制語法:** `break`, `continue`, `else (與迴圈搭配)`。

---

### 3. 函式與參數設定 (`definedfunctions.py`)
* **函式回傳值 (return) 的差異:** 在 Python 中，return 決定了函式執行完後要「交回」什麼資料
  - 無 return 或僅 return: 函式預設會回傳 None。
  - 自定義 return: 可以回傳固定值、計算結果或表達式。
  - 重點: print() 只是將結果顯示在螢幕上，而 return 才能讓函式外的人取得數值並進一步運算。
* **參數的預設值:** 可以為參數設定預設資料，當呼叫函式時漏掉該參數，程式會自動補位
  - 範例: `power(base, exp=0)`，若不傳入 `exp`，則預設為 0 次方。
* **不定長度參數:** 使用 `*ns `(以 Tuple 形式接收) 來處理數量不確定的輸入資料。
  - 應用場景: 當你不知道使用者會輸入多少個數字（例如計算平均值）時非常實用。

---

### 4. 檔案讀寫(`fileIO.py`)
* **純文字檔案 (.txt):** 
  - 寫入 (w)：建立新檔案或覆寫現有內容。
  讀取 (r)：讀取全文或使用 `for` 迴圈逐行讀取進型運算（如數字加總）。
  - 追加 (a)：在不刪除舊資料的情況下，於檔案末端新增內容。
  - 修改：透過 `read()` 載入記憶體後，使用 `replace()` 字串替換再寫回。
* **JSON 資料格式:** 
  - 序列化 (dump)：將 Python 字典 (Dict) 轉換並儲存為 JSON 檔案。
  - 反序列化 (load)：將 JSON 檔案讀取為 Python 字典，方便進行 Key-Value 操作。
  - 動態更新：直接在 Dict 中修改或新增鍵值對，並重新儲存。
* **CSV 與 Excel 表格:** 
  - DataFrame 操作：將資料轉換為表格物件，方便篩選特定欄位。
  - 追加資料：學習在 `to_csv` 時使用 `mode='a'` 並關閉 `header` 以免標題重複。
  - 精準修改：利用 `.loc` (標籤定位) 或 `.iloc` (索引定位) 針對特定儲存格進行修改。
  - Excel 相容：只需將 `csv` 相關指令替換為 `excel` (需安裝 `openpyxl`) 即可無縫接軌。

---

## 🚀 如何執行
確保環境已安裝 Python 3.x，在終端機輸入：

```bash
# 執行基礎運算單元
python operations_list_tuple.py

# 執行流程控制單元
python conditionals_loops.py

# 執行函式與參數單元
python definedfunctions.py

# 執行檔案讀寫
python fileIO.py
```
