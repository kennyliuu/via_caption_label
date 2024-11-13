import os
from PIL import Image
import imghdr
from pathlib import Path

def check_images(folder_path):
    """
    檢查資料夾中的圖片:
    1. 找出 RGBA 圖片
    2. 找出副檔名為 png 但實際不是 png 的圖片
    """
    folder_path = Path(folder_path)
    
    # 儲存結果
    rgba_images = []
    wrong_format_images = []
    
    print(f"開始檢查資料夾: {folder_path}")
    print("-" * 50)
    
    # 遍歷所有 png 檔案
    for img_path in folder_path.glob('*.png'):
        try:
            # 檢查實際檔案類型
            actual_type = imghdr.what(img_path)
            
            # 檢查是否為 RGBA
            with Image.open(img_path) as img:
                if img.mode == 'RGBA':
                    rgba_images.append(img_path.name)
                
            # 檢查實際格式是否為 PNG
            if actual_type != 'png':
                wrong_format_images.append({
                    'name': img_path.name,
                    'actual_type': actual_type
                })
                
        except Exception as e:
            print(f"處理 {img_path.name} 時發生錯誤: {str(e)}")
    
    # 輸出結果
    print("\n檢查結果:")
    print("-" * 50)
    
    if rgba_images:
        print("\nRGBA 圖片:")
        for img in rgba_images:
            print(f"- {img}")
        print(f"共 {len(rgba_images)} 張 RGBA 圖片")
    else:
        print("\n沒有發現 RGBA 圖片")
    
    if wrong_format_images:
        print("\n副檔名為 .png 但實際不是 PNG 的圖片:")
        for img in wrong_format_images:
            print(f"- {img['name']} (實際類型: {img['actual_type']})")
        print(f"共 {len(wrong_format_images)} 張格式不符的圖片")
    else:
        print("\n沒有發現格式不符的圖片")
    
    return rgba_images, wrong_format_images

if __name__ == "__main__":
    # 指定要檢查的資料夾路徑
    folder_path = r"D:\dataset\new"
    
    # 執行檢查
    rgba_list, wrong_format_list = check_images(folder_path)