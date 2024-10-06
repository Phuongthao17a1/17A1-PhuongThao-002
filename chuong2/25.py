from xml.dom import minidom

# Tải file XML và in ra tên các phần tử
def load_and_parse_xml(file_name):
    try:
        # Phân tích file XML
        dom = minidom.parse(file_name)

        # Lấy danh sách các phần tử
        elements = dom.getElementsByTagName('')  # '' để lấy tất cả các phần tử

        # In ra tên của từng phần tử
        for element in elements:
            print(f'Tên phần tử: {element.tagName}')

    except Exception as e:
        print(f'Có lỗi xảy ra: {e}')

# Gọi hàm để tải và phân tích file XML
load_and_parse_xml('sample.xml')