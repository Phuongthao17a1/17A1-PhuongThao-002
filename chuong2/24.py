from xml.dom import minidom

# Tải file XML
def load_and_parse_xml(file_name):
    try:
        # Phân tích file XML
        dom = minidom.parse(file_name)

        # Lấy tên công ty
        company_name = dom.getElementsByTagName('name')[0].firstChild.nodeValue
        print(f'Tên công ty: {company_name}')

        # Lấy thông tin về nhân viên
        staff_list = dom.getElementsByTagName('staff')
        for staff in staff_list:
            staff_id = staff.getAttribute('id')
            staff_name = staff.getElementsByTagName('name')[0].firstChild.nodeValue
            staff_salary = staff.getElementsByTagName('salary')[0].firstChild.nodeValue

            print(f'Nhân viên ID: {staff_id}, Tên: {staff_name}, Lương: {staff_salary}')

    except Exception as e:
        print(f'Có lỗi xảy ra: {e}')

# Gọi hàm để tải và phân tích file XML
load_and_parse_xml('sample.xml')