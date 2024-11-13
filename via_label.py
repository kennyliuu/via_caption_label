import json
import xml.etree.ElementTree as ET
import os
from PIL import Image  # 用於獲取圖片尺寸
import re  # 用於處理文件名中的多餘部分

# 載入 VIA 的 JSON 標註文件
via_json_file = r'D:\dataset\new\new.json'  # 替換成你的 JSON 文件名稱和路徑
with open(via_json_file, 'r') as f:
    data = json.load(f)

# 設定輸出文件夾，將路徑改為你的目標路徑
output_folder = r'D:\dataset\new'
os.makedirs(output_folder, exist_ok=True)  # 確保目標文件夾存在

# 確保只檢查 _via_img_metadata 內的圖片數據
if '_via_img_metadata' in data:
    img_metadata = data['_via_img_metadata']
else:
    print("未找到圖片數據。確認 JSON 文件是否正確。")
    img_metadata = {}

# 清理文件名的函數，只保留文件名的主體部分和擴展名
def clean_filename(filename):
    # 這裡假設文件名應該是形如 "1.png" 的格式，去除多餘的數字
    match = re.match(r'([a-zA-Z0-9_]+\.png)', filename)  # 匹配正確的圖片文件名
    if match:
        cleaned_filename = match.group(1)
    else:
        cleaned_filename = filename  # 如果沒有匹配到，則返回原文件名
    print(f"清理過的文件名: {cleaned_filename}")  # 打印清理後的文件名進行檢查
    return cleaned_filename

# 開始轉換每張圖片的標註
for image_filename, image_data in img_metadata.items():
    # 清理文件名
    cleaned_image_filename = clean_filename(image_filename)
    
    # 檢查是否存在 'file_attributes'
    if 'file_attributes' not in image_data:
        print(f"跳過圖片 {cleaned_image_filename}，因為沒有 'file_attributes'。")
        continue  # 如果沒有 'file_attributes'，跳過該圖片

    # 嘗試從 file_attributes 中獲取圖片尺寸
    image_width = image_data['file_attributes'].get('image_width')
    image_height = image_data['file_attributes'].get('image_height')

    # 如果沒有圖片尺寸，從圖片本身提取
    image_path = os.path.join(r'D:\dataset\new', cleaned_image_filename)  # 替換為圖片的實際存放路徑
    print(f"嘗試打開圖片: {image_path}")  # 打印出要嘗試打開的圖片路徑

    if not os.path.exists(image_path):
        print(f"圖片文件不存在：{image_path}")
        continue  # 如果文件不存在，跳過該圖片

    if image_width is None or image_height is None:
        try:
            with Image.open(image_path) as img:
                image_width, image_height = img.size
                print(f"從圖片中檢測到尺寸：{cleaned_image_filename}，寬度: {image_width}, 高度: {image_height}")
        except Exception as e:
            print(f"無法讀取圖片尺寸：{cleaned_image_filename}，錯誤：{e}")
            continue  # 如果圖片無法打開，跳過該圖片

    # 創建 XML 根節點
    annotation = ET.Element('annotation')
    
    # 添加 folder 節點
    folder = ET.SubElement(annotation, 'folder')
    folder.text = 'extract_captions'
    
    # 添加 filename 節點
    filename = ET.SubElement(annotation, 'filename')
    filename.text = cleaned_image_filename

    # 添加 size 節點
    size = ET.SubElement(annotation, 'size')
    
    # 添加圖片寬度和高度
    width = ET.SubElement(size, 'width')
    width.text = str(image_width)
    
    height = ET.SubElement(size, 'height')
    height.text = str(image_height)
    
    depth = ET.SubElement(size, 'depth')
    depth.text = '3'  # 假設圖片有3個顏色通道 (RGB)

    # 處理 caption 描述，去除不必要的空格
    captions = image_data['file_attributes'].get('caption', [])
    if not captions:
        print(f"圖片 {cleaned_image_filename} 沒有 'caption' 描述。")
        continue  # 如果沒有 'caption'，跳過該圖片的標註

    # 合併 caption 並去除字元之間的多餘空格
    combined_caption = ''.join(captions)  # 使用 ''.join() 而不是 ' '.join()
    obj = ET.SubElement(annotation, 'object')
    name = ET.SubElement(obj, 'name')
    name.text = 'caption'
    caption_text = ET.SubElement(obj, 'caption')
    caption_text.text = combined_caption

    # 將 XML 樹結構轉換為字符串並保存到文件
    output_file = os.path.join(output_folder, os.path.splitext(cleaned_image_filename)[0] + '.xml')
    tree = ET.ElementTree(annotation)
    tree.write(output_file, encoding='utf-8', xml_declaration=True)

print(f"所有圖片的 XML 標註文件已保存到: {output_folder}")
