import os
from pillow_heif import register_heif_opener
from PIL import Image
import numpy as np

def convert_heic_to_png(folder_path, start_index=1, delete_original=False):
    # 註冊 HEIF 圖片開啟器
    register_heif_opener()
    
    # 確保資料夾路徑存在
    if not os.path.exists(folder_path):
        print(f"錯誤: 找不到資料夾 '{folder_path}'")
        return
    
    # 計數器
    converted = 0
    failed = 0
    deleted = 0
    
    # 獲取所有 HEIC 文件
    heic_files = [f for f in os.listdir(folder_path) 
                  if f.lower().endswith(('.heic', '.heif'))]
    
    print(f"找到 {len(heic_files)} 個 HEIC 檔案")
    
    # 遍歷所有 HEIC 文件
    current_index = start_index
    for filename in heic_files:
        try:
            # 構建輸入文件路徑
            input_path = os.path.join(folder_path, filename)
            
            # 生成新的文件名（從指定數字開始）
            new_filename = f"{current_index}.png"
            output_path = os.path.join(folder_path, new_filename)
            
            # 檢查是否存在同名文件
            while os.path.exists(output_path):
                print(f"警告: {new_filename} 已存在，嘗試下一個數字")
                current_index += 1
                new_filename = f"{current_index}.png"
                output_path = os.path.join(folder_path, new_filename)
            
            # 開啟並轉換圖片
            image = Image.open(input_path)
            image.save(output_path, 'PNG')
            
            print(f"成功轉換: {filename} -> {new_filename}")
            converted += 1
            
            # 如果指定要刪除原始檔案
            if delete_original:
                try:
                    os.remove(input_path)
                    print(f"已刪除原始檔案: {filename}")
                    deleted += 1
                except Exception as e:
                    print(f"刪除檔案失敗 {filename}: {str(e)}")
            
            current_index += 1
            
        except Exception as e:
            print(f"轉換失敗 {filename}: {str(e)}")
            failed += 1
    
    # 輸出統計信息
    print(f"\n轉換完成!")
    print(f"成功轉換: {converted} 個檔案")
    print(f"轉換失敗: {failed} 個檔案")
    if delete_original:
        print(f"成功刪除: {deleted} 個原始檔案")
    print(f"最後使用的數字: {current_index - 1}")

def get_yes_no_input(prompt):
    """獲取使用者的是/否輸入"""
    while True:
        response = input(prompt).strip().lower()
        if response in ['y', 'yes', '是', 'y是']:
            return True
        if response in ['n', 'no', '否', 'n否']:
            return False
        print("請輸入 yes/no 或 是/否")

def main():
    # 獲取用戶輸入
    folder_path = r"D:\dataset\1"
    
    try:
        start_index = int(input("請輸入起始數字 (直接按Enter使用1): ").strip() or "1")
        if start_index < 1:
            print("起始數字必須大於0，使用預設值1")
            start_index = 1
    except ValueError:
        print("輸入無效，使用預設值1")
        start_index = 1
    
    # 詢問是否要刪除原始檔案
    delete_original = get_yes_no_input("是否要刪除原始HEIC檔案? (yes/no): ")
    
    # 如果選擇刪除，再次確認
    if delete_original:
        confirm_delete = get_yes_no_input("⚠️ 確定要刪除原始檔案嗎？此操作無法復原 (yes/no): ")
        if not confirm_delete:
            delete_original = False
            print("將保留原始檔案")
    
    # 執行轉換
    convert_heic_to_png(folder_path, start_index, delete_original)

if __name__ == "__main__":
    main()