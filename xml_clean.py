import os
import glob

def delete_xml_files(folder_path):
    # 取得資料夾內所有 .xml 檔案
    xml_files = glob.glob(os.path.join(folder_path, "*.xml"))
    
    # 刪除每一個 .xml 檔案
    for file in xml_files:
        try:
            os.remove(file)
            print(f"已刪除: {file}")
        except Exception as e:
            print(f"無法刪除 {file}: {e}")

# 使用範例：指定資料夾路徑
folder_path = r"D:\dataset\new"
delete_xml_files(folder_path)
