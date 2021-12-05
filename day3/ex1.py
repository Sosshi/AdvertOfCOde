import pandas as pd


class FindBits:
    def __init__(self, filename):
        self.filename = filename

    def open_file(self):
        """Opens the file"""
        file = open(self.filename)
        return file

    def convert_to_list(self) -> list:
        """takes in a file and returns a list"""
        list_of_positions = []
        file = self.open_file()
        for number in file.readlines():
            list_of_positions.append(list(number.strip()))
        return list_of_positions

    def convert_to_pandas(self):
        """Converts the list to pandas dataframe"""
        return pd.DataFrame(self.convert_to_list())

    def count_most_common_numbers(self) -> list:
        df = self.convert_to_pandas()
        list_of_most_common_numbers = []
        for column in df:
            list_of_most_common_numbers.append(
                self.count(self.count(df.columns[column]))
            )

        return list_of_most_common_numbers

    def count(self, series_list) -> int:
        count_zeros = 0
        count_ones = 0
        if type(series_list) != type(2):
            for number in series_list:
                if number == 1:
                    count_ones = count_ones + 1
                else:
                    count_zeros = count_zeros + 1
        else:
            return "nothing"
        if count_zeros > count_ones:
            return count_zeros

        else:
            return count_ones


check = FindBits("sample.txt").count_most_common_numbers()
print(check)