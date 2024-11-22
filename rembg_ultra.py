import os
import shutil
from rembg import remove
from PIL import Image
import numpy as np
import onnxruntime as ort

# 設置環境變數以解決 OMP 錯誤
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

def process_folder(input_folder, output_folder, keep_original_filename=True, bg_color=(255, 255, 255)):
    """
    批次處理資料夾內的圖片去背，並複製對應的XML檔案
    
    Args:
        input_folder: 輸入資料夾路徑，包含圖片和XML檔案
        output_folder: 輸出資料夾路徑
        keep_original_filename: 是否保留原始檔名，True則不加上'result_'前綴
        bg_color: 背景顏色，預設為白色 (255, 255, 255)
    """
    try:
        # 檢查 ONNX Runtime 的執行設備
        providers = ort.get_available_providers()
        if 'CUDAExecutionProvider' in providers:
            print("使用 GPU 進行處理")
            print(f"可用的執行提供者: {providers}")
        else:
            print("使用 CPU 進行處理")
            print(f"可用的執行提供者: {providers}")
        
        # 確保輸出資料夾存在
        os.makedirs(output_folder, exist_ok=True)
        
        # 取得所有檔案
        files = os.listdir(input_folder)
        
        # 計算總檔案數來顯示進度
        image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        total_files = len(image_files)
        processed_files = 0
        
        print(f"開始處理，共有 {total_files} 個檔案需要處理")
        
        # 處理所有圖片檔案
        for filename in files:
            # 檢查是否為圖片檔案
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                # 圖片完整路徑
                input_path = os.path.join(input_folder, filename)
                
                # 對應的XML檔案名稱
                xml_filename = os.path.splitext(filename)[0] + '.xml'
                xml_input_path = os.path.join(input_folder, xml_filename)
                
                # 如果存在對應的XML檔案
                if os.path.exists(xml_input_path):
                    # 複製XML檔案到輸出資料夾
                    xml_output_path = os.path.join(output_folder, xml_filename)
                    shutil.copy2(xml_input_path, xml_output_path)
                    print(f"複製XML檔案: {xml_filename}")
                
                try:
                    # 讀取圖片並記錄原始尺寸
                    input_image = Image.open(input_path)
                    original_size = input_image.size
                    print(f"處理圖片: {filename}")
                    print(f"原始圖片尺寸: {original_size}")
                    
                    # 關閉 alpha matting 以避免可能的錯誤
                    output_image = remove(
                        input_image,
                        alpha_matting=False,  # 關閉 alpha matting
                        post_process_mask=True
                    )
                    
                    # 檢查並調整輸出圖片尺寸
                    if output_image.size != original_size:
                        print(f"調整圖片尺寸從 {output_image.size} 到 {original_size}")
                        output_image = output_image.resize(original_size, Image.Resampling.LANCZOS)
                    
                    # 創建指定尺寸的背景
                    background = Image.new('RGB', original_size, bg_color)
                    
                    # 確保格式正確
                    if output_image.mode != 'RGBA':
                        output_image = output_image.convert('RGBA')
                    
                    # 合成圖片
                    background = background.convert('RGBA')
                    composite = Image.alpha_composite(background, output_image)
                    
                    # 轉換為RGB
                    rgb_image = composite.convert('RGB')
                    
                    # 再次確認最終輸出尺寸
                    if rgb_image.size != original_size:
                        rgb_image = rgb_image.resize(original_size, Image.Resampling.LANCZOS)
                    
                    # 設定輸出檔名
                    if keep_original_filename:
                        output_filename = filename
                    else:
                        output_filename = f"result_{filename}"
                    
                    # 設定輸出路徑並儲存
                    output_path = os.path.join(output_folder, output_filename)
                    rgb_image.save(output_path, 'PNG', quality=95)
                    
                    # 確認最終檔案尺寸
                    final_image = Image.open(output_path)
                    print(f"最終輸出尺寸: {final_image.size}")
                    
                    # 更新進度
                    processed_files += 1
                    print(f"處理進度: {processed_files}/{total_files}")
                    print("-" * 50)
                    
                except Exception as e:
                    print(f"處理圖片 {filename} 時發生錯誤: {str(e)}")
                    continue
        
        print(f"\n批次處理完成！共處理 {processed_files} 個檔案")
        
    except Exception as e:
        print(f"處理過程中發生錯誤: {str(e)}")

# 使用範例
input_folder = r'C:\dataset\act_useful\val'    # 輸入資料夾路徑
output_folder = r'C:\dataset\val'              # 輸出資料夾路徑

# 執行批次處理
process_folder(
    input_folder=input_folder, 
    output_folder=output_folder,
    keep_original_filename=True  # True表示保留原始檔名，False會加上'result_'前綴
)