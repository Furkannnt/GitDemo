import openpyxl

def read_specific_rows_into_dict(file_path):
    # Belirtilen dosya yolundan Excel dosyasını yükle
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    # Verilerin depolanacağı sözlük
    data_dict = {}

    # Belirli satırları işlemek için döngü
    for row in sheet.iter_rows(values_only=True):
        first_cell_value = row[0]

        # İlk hücredeki değer "TestCase1" veya "TestCase2" ise satırı işleyip sözlüğe ekle
        if first_cell_value in ["TestCase1", "TestCase2"]:
            row_data = list(row)
            data_dict[first_cell_value] = row_data

    return data_dict

# Dosyanın yolunu belirt
file_path = "C:/Users/PROVEN-LAPTOP/Desktop/pythonGetData.xlsx"
# Verileri sözlükte topla
data = read_specific_rows_into_dict(file_path)
# Sözlüğü yazdır
print(data)
