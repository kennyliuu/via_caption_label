import os
import xml.etree.ElementTree as ET

# 設定 XML 文件和影像文件資料夾路徑
XML_DIR = r'C:\Users\Liu\Desktop\dataset\behavior'

# 更新 XML 檔案的 filename
def update_xml_filenames(xml_dir, image_dir):
    for xml_file in os.listdir(xml_dir):
        if xml_file.endswith('.xml'):
            xml_path = os.path.join(xml_dir, xml_file)
            
            # 解析 XML 檔案
            tree = ET.parse(xml_path)
            root = tree.getroot()

            # 獲取當前 XML 檔中的 <filename> 標籤
            current_filename = root.find('filename').text

            # 根據 XML 檔名推測對應的影像檔案名稱
            xml_basename = os.path.splitext(xml_file)[0]

            # 查找資料夾中對應的影像文件
            matching_images = [f for f in os.listdir(image_dir) if f.startswith(xml_basename) and f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]

            # 如果找到了影像文件，更新 XML 中的 <filename> 元素
            if matching_images:
                new_filename = matching_images[0]  # 假設只有一個影像匹配
                root.find('filename').text = new_filename

                # 保存更新後的 XML 檔案
                tree.write(xml_path)
                print(f"Updated XML filename for: {xml_file}")

# 執行更新操作
update_xml_filenames(XML_DIR, XML_DIR)
