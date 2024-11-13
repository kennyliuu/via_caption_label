import xml.etree.ElementTree as ET
import os
import glob

def modify_caption_in_xml(xml_file):
    try:
        # 解析XML文件
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        # 找到object/caption元素
        object_elem = root.find('object')
        if object_elem is not None:
            caption_elem = object_elem.find('caption')
            if caption_elem is not None:
                # 獲取原始caption文本
                original_caption = caption_elem.text
                
                # 替換文本中的"man"為"person"
                # 使用前後空格確保替換完整單詞
                modified_caption = original_caption.replace(' man ', ' person ')
                # 處理句首的情況
                modified_caption = modified_caption.replace('A man ', 'A person ')
                modified_caption = modified_caption.replace('The man ', 'The person ')
                
                # 只有當caption有變化時才更新和輸出
                if modified_caption != original_caption:
                    # 更新caption文本
                    caption_elem.text = modified_caption
                    
                    # 保存修改後的XML
                    tree.write(xml_file, encoding='utf-8', xml_declaration=True)
                    print(f"Modified {xml_file}")
                    print(f"Original caption: {original_caption}")
                    print(f"Modified caption: {modified_caption}")
                    print("-" * 50)
                    return True
                return False
            else:
                print(f"Warning: No caption element found in object for {xml_file}")
                return False
        else:
            print(f"Warning: No object element found in {xml_file}")
            return False
            
    except ET.ParseError as e:
        print(f"Error parsing {xml_file}: {str(e)}")
        return False
    except Exception as e:
        print(f"Error processing {xml_file}: {str(e)}")
        return False

def process_all_xml_files(directory='.'):
    # 獲取指定目錄下的所有XML文件
    xml_files = glob.glob(os.path.join(directory, '*.xml'))
    
    # 統計信息
    total_files = len(xml_files)
    modified_files = 0
    
    print(f"Found {total_files} XML files")
    
    # 處理每個XML文件
    for xml_file in xml_files:
        if modify_caption_in_xml(xml_file):
            modified_files += 1
        
    print("\nSummary:")
    print(f"Total files processed: {total_files}")
    print(f"Files actually modified: {modified_files}")

if __name__ == "__main__":
    # 可以指定包含XML文件的目錄，預設為當前目錄
    directory = r'D:\dataset\2man'
    process_all_xml_files(directory)