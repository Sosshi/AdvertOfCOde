class CountIncrease:
    def __init__(self, filename):
        self.filename = filename

    def open_file(self):
        """Opens the file"""
        file = open(self.filename)
        return file

    def convert_file_to_list(self) -> list:
        """takes in a file and returns a list"""
        list_of_numbers = []
        file = self.open_file()
        for number in file.readlines():
            list_of_numbers.append(int(number))
        return list_of_numbers

    def check_increase(self) -> int:
        counter = 0
        list_of_numbers = self.convert_file_to_list()
        for index, number in enumerate(list_of_numbers):
            if index and number > list_of_numbers[index - 1]:
                counter = counter + 1
        return counter


count = CountIncrease("input.txt").check_increase()
print(count)
