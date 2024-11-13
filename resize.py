from PIL import Image
import shutil
import os
import xml.etree.ElementTree as ET

# 定義來源資料夾和目標資料夾
source_folder = r'C:\Users\Liu\Desktop\dataset\nknuxml'
target_folder = r'C:\Users\Liu\Desktop\dataset\resize'

# 如果目標資料夾不存在，創建它
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# 縮小比例
scale = 0.3

# 起始編號
start_index = 882

# 紀錄圖片處理的數量
index = start_index

# 遍歷來源資料夾中的所有檔案
for filename in os.listdir(source_folder):
    if filename.endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif")):
        # 打開圖片
        image_path = os.path.join(source_folder, filename)
        with Image.open(image_path) as img:
            # 計算新的大小
            new_size = (int(img.width * scale), int(img.height * scale))
            # 縮放圖片
            img_resized = img.resize(new_size, Image.ANTIALIAS)
            # 構造新的圖片檔名，從882開始遞增
            new_filename = f"{index}.jpg"
            # 保存縮小後的圖片到目標資料夾
            save_path = os.path.join(target_folder, new_filename)
            img_resized.save(save_path)

            # 檢查是否存在對應的 XML 檔案（假設 XML 檔案與圖片檔案名稱一致，但副檔名不同）
            xml_filename = os.path.splitext(filename)[0] + ".xml"
            xml_path = os.path.join(source_folder, xml_filename)
            if os.path.exists(xml_path):
                # 構造新的 XML 檔名
                new_xml_filename = f"{index}.xml"
                new_xml_path = os.path.join(target_folder, new_xml_filename)

                # 複製 XML 文件到目標資料夾，不需要改變標註內容
                shutil.copy(xml_path, new_xml_path)

            # 更新編號
            index += 1

print("所有圖片及其對應的 XML 檔案已成功縮小並保存到目標資料夾，檔名從 882 開始。")
