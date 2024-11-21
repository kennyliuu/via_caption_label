from PIL import Image, ImageEnhance, ImageFilter
import shutil
import os

# 1. 亮度調整
def brightness_augmentation():
    source_folder = r'D:\dataset\test'
    target_folder = r'D:\dataset\test2'
    
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    start_index = 1
    index = start_index
    brightness_factor = 1.5  # 增加亮度
    
    for filename in os.listdir(source_folder):
        if filename.endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif")):
            image_path = os.path.join(source_folder, filename)
            with Image.open(image_path) as img:
                # 調整亮度
                enhancer = ImageEnhance.Brightness(img)
                img_bright = enhancer.enhance(brightness_factor)
                new_filename = f"{index}.png"
                save_path = os.path.join(target_folder, new_filename)
                img_bright.save(save_path)
                
                # 複製 XML
                xml_filename = os.path.splitext(filename)[0] + ".xml"
                xml_path = os.path.join(source_folder, xml_filename)
                if os.path.exists(xml_path):
                    new_xml_filename = f"{index}.xml"
                    new_xml_path = os.path.join(target_folder, new_xml_filename)
                    shutil.copy(xml_path, new_xml_path)
                
                index += 1
    
    print(f"亮度調整數據擴增完成！")

# 2. 旋轉增強
def rotation_augmentation():
    source_folder = r'D:\dataset\test'
    target_folder = r'D:\dataset\test2'
    
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    start_index = 8
    index = start_index
    rotation_angle = 15  # 旋轉角度
    
    for filename in os.listdir(source_folder):
        if filename.endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif")):
            image_path = os.path.join(source_folder, filename)
            with Image.open(image_path) as img:
                # 旋轉圖片
                img_rotated = img.rotate(rotation_angle, expand=True, fillcolor='white')
                new_filename = f"{index}.png"
                save_path = os.path.join(target_folder, new_filename)
                img_rotated.save(save_path)
                
                # 複製 XML
                xml_filename = os.path.splitext(filename)[0] + ".xml"
                xml_path = os.path.join(source_folder, xml_filename)
                if os.path.exists(xml_path):
                    new_xml_filename = f"{index}.xml"
                    new_xml_path = os.path.join(target_folder, new_xml_filename)
                    shutil.copy(xml_path, new_xml_path)
                
                index += 1
    
    print(f"旋轉擴增完成！")

# 3. 高斯模糊
def gaussian_blur_augmentation():
    source_folder = r'D:\dataset\test'
    target_folder = r'D:\dataset\test2'
    
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    start_index = 12
    index = start_index
    
    for filename in os.listdir(source_folder):
        if filename.endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif")):
            image_path = os.path.join(source_folder, filename)
            with Image.open(image_path) as img:
                # 應用高斯模糊
                img_blur = img.filter(ImageFilter.GaussianBlur(radius=1))
                new_filename = f"{index}.png"
                save_path = os.path.join(target_folder, new_filename)
                img_blur.save(save_path)
                
                # 複製 XML
                xml_filename = os.path.splitext(filename)[0] + ".xml"
                xml_path = os.path.join(source_folder, xml_filename)
                if os.path.exists(xml_path):
                    new_xml_filename = f"{index}.xml"
                    new_xml_path = os.path.join(target_folder, new_xml_filename)
                    shutil.copy(xml_path, new_xml_path)
                
                index += 1
    
    print(f"高斯模糊擴增完成！")

# 4. 飽和度調整
def saturation_augmentation():
    source_folder = r'D:\dataset\test'
    target_folder = r'D:\dataset\test2'
    
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    start_index = 16
    index = start_index
    saturation_factor = 1.5  # 增加飽和度
    
    for filename in os.listdir(source_folder):
        if filename.endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif")):
            image_path = os.path.join(source_folder, filename)
            with Image.open(image_path) as img:
                # 調整飽和度
                enhancer = ImageEnhance.Color(img)
                img_saturated = enhancer.enhance(saturation_factor)
                new_filename = f"{index}.png"
                save_path = os.path.join(target_folder, new_filename)
                img_saturated.save(save_path)
                
                # 複製 XML
                xml_filename = os.path.splitext(filename)[0] + ".xml"
                xml_path = os.path.join(source_folder, xml_filename)
                if os.path.exists(xml_path):
                    new_xml_filename = f"{index}.xml"
                    new_xml_path = os.path.join(target_folder, new_xml_filename)
                    shutil.copy(xml_path, new_xml_path)
                
                index += 1
    
    print(f"飽和度調整擴增完成！")

# 5. 銳化
def sharpness_augmentation():
    source_folder = r'D:\dataset\test'
    target_folder = r'D:\dataset\test2'
    
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    start_index = 20
    index = start_index
    sharpness_factor = 2.0  # 增加銳度
    
    for filename in os.listdir(source_folder):
        if filename.endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif")):
            image_path = os.path.join(source_folder, filename)
            with Image.open(image_path) as img:
                # 調整銳度
                enhancer = ImageEnhance.Sharpness(img)
                img_sharp = enhancer.enhance(sharpness_factor)
                new_filename = f"{index}.png"
                save_path = os.path.join(target_folder, new_filename)
                img_sharp.save(save_path)
                
                # 複製 XML
                xml_filename = os.path.splitext(filename)[0] + ".xml"
                xml_path = os.path.join(source_folder, xml_filename)
                if os.path.exists(xml_path):
                    new_xml_filename = f"{index}.xml"
                    new_xml_path = os.path.join(target_folder, new_xml_filename)
                    shutil.copy(xml_path, new_xml_path)
                
                index += 1
    
    print(f"銳化擴增完成！")

# 可以根據需要調用不同的擴增函數
if __name__ == "__main__":
     brightness_augmentation()
     rotation_augmentation()
     gaussian_blur_augmentation()
     saturation_augmentation()
     sharpness_augmentation()
     pass