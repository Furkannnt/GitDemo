class HomePageData:

    @staticmethod
    def get_test_data(file_path):
        from TestData.getDataFromExcel import read_specific_rows_into_dict
        # Excel dosyasından verileri al
        data = read_specific_rows_into_dict(file_path)

        # Verileri istenilen formata dönüştür
        test_data = []
        for key, value in data.items():
            test_data.append({
                "name": value[1],
                "mail": value[2],
                "password": value[3],
                "gender": value[4]
            })
        return test_data
