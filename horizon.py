from PIL import Image
import shutil
import os

# 定義來源資料夾和目標資料夾
source_folder = r'C:\Users\Liu\Desktop\dataset\nknuxml'
target_folder = r'C:\Users\Liu\Desktop\dataset\resize'

# 如果目標資料夾不存在，創建它
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# 起始編號
start_index = 882
index = start_index

# 遍歷來源資料夾中的所有檔案
for filename in os.listdir(source_folder):
    if filename.endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif")):
        # 打開圖片
        image_path = os.path.join(source_folder, filename)
        with Image.open(image_path) as img:
            # 保存水平翻轉的版本
            img_flipped = img.transpose(Image.FLIP_LEFT_RIGHT)
            new_filename = f"{index}_flip.jpg"
            save_path = os.path.join(target_folder, new_filename)
            img_flipped.save(save_path)
            
            # 處理對應的 XML 文件（如果存在）
            xml_filename = os.path.splitext(filename)[0] + ".xml"
            xml_path = os.path.join(source_folder, xml_filename)
            if os.path.exists(xml_path):
                # 複製 XML 文件
                new_xml_filename = f"{index}_flip.xml"
                new_xml_path = os.path.join(target_folder, new_xml_filename)
                shutil.copy(xml_path, new_xml_path)
            
            # 更新編號
            index += 1

print(f"水平翻轉數據擴增完成！所有圖片從編號 {start_index} 開始。")