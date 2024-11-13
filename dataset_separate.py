import os
import shutil
import random
from glob import glob

def split_dataset(source_dir, train_ratio=0.7, val_ratio=0.15, test_ratio=0.15):
    """
    將資料夾中的圖片和對應的XML檔案按照指定比例分配到訓練、驗證和測試集
    
    Parameters:
        source_dir (str): 源數據資料夾路徑
        train_ratio (float): 訓練集比例
        val_ratio (float): 驗證集比例
        test_ratio (float): 測試集比例
    """
    
    # 確保比例合計為1
    assert abs(train_ratio + val_ratio + test_ratio - 1.0) < 1e-5, "比例總和必須為1"
    
    # 建立目標資料夾
    dataset_types = ['train', 'val', 'test']
    for dtype in dataset_types:
        os.makedirs(os.path.join(source_dir, dtype), exist_ok=True)
    
    # 獲取所有圖片文件
    image_files = []
    for ext in ['*.jpg', '*.jpeg', '*.png']:
        image_files.extend(glob(os.path.join(source_dir, ext)))
    
    # 隨機打亂文件順序
    random.shuffle(image_files)
    
    # 計算每個數據集的文件數量
    total_files = len(image_files)
    train_count = int(total_files * train_ratio)
    val_count = int(total_files * val_ratio)
    
    # 分割數據集
    train_files = image_files[:train_count]
    val_files = image_files[train_count:train_count + val_count]
    test_files = image_files[train_count + val_count:]
    
    # 將文件移動到對應資料夾
    splits = {
        'train': train_files,
        'val': val_files,
        'test': test_files
    }
    
    for split_name, files in splits.items():
        for img_path in files:
            # 處理圖片文件
            filename = os.path.basename(img_path)
            new_img_path = os.path.join(source_dir, split_name, filename)
            shutil.copy2(img_path, new_img_path)
            
            # 處理對應的XML文件
            xml_filename = os.path.splitext(filename)[0] + '.xml'
            xml_path = os.path.join(source_dir, xml_filename)
            if os.path.exists(xml_path):
                new_xml_path = os.path.join(source_dir, split_name, xml_filename)
                shutil.copy2(xml_path, new_xml_path)
    
    # 打印數據集統計信息
    print(f"數據集分割完成！")
    print(f"訓練集: {len(train_files)} 文件")
    print(f"驗證集: {len(val_files)} 文件")
    print(f"測試集: {len(test_files)} 文件")

# 使用示例
if __name__ == "__main__":
    # 設置源數據資料夾路徑
    source_directory = r"D:\dataset\2man"
    
    # 設置分割比例（訓練集:驗證集:測試集 = 70:15:15）
    split_dataset(source_directory, train_ratio=0.6, val_ratio=0.2, test_ratio=0.2)