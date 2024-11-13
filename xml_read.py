import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import os
import glob

def format_xml(xml_file):
    try:
        # 解析XML文件
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        # 將ElementTree轉換為字符串
        xml_str = ET.tostring(root, encoding='utf-8')
        
        # 使用minidom重新格式化XML
        dom = minidom.parseString(xml_str)
        pretty_xml = dom.toprettyxml(indent='    ', encoding='utf-8')
        
        # 移除空白行（這是一個常見問題，minidom會產生過多空行）
        pretty_xml_str = '\n'.join([line for line in pretty_xml.decode('utf-8').split('\n') if line.strip()])
        
        # 添加XML聲明
        if not pretty_xml_str.startswith('<?xml'):
            pretty_xml_str = '<?xml version="1.0" encoding="utf-8"?>\n' + pretty_xml_str
        
        # 寫回文件
        with open(xml_file, 'w', encoding='utf-8') as f:
            f.write(pretty_xml_str)
            
        print(f"Formatted {xml_file}")
        print("Sample of formatted XML:")
        print("-" * 50)
        print(pretty_xml_str)
        print("-" * 50)
            
    except ET.ParseError as e:
        print(f"Error parsing {xml_file}: {str(e)}")
    except Exception as e:
        print(f"Error processing {xml_file}: {str(e)}")

def process_all_xml_files(directory='.'):
    # 獲取指定目錄下的所有XML文件
    xml_files = glob.glob(os.path.join(directory, '*.xml'))
    
    total_files = len(xml_files)
    print(f"Found {total_files} XML files")
    
    # 處理每個XML文件
    for xml_file in xml_files:
        format_xml(xml_file)
        
    print("\nSummary:")
    print(f"Total files processed: {total_files}")

if __name__ == "__main__":
    # 可以指定包含XML文件的目錄，預設為當前目錄
    directory = r'D:\dataset\new'
    process_all_xml_files(directory)