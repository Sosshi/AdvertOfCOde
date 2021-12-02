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

    def list_of_sum_of_three_consecutive_numbers_in_a_list(self) -> list:
        """Sums up three consecutive numbers and returns a list of the sums"""
        list_of_numbers = []
        loop_over_list = self.convert_file_to_list()
        for index, number in enumerate(loop_over_list):
            if index > 1:
                list_of_numbers.append(
                    sum([loop_over_list[index - 1], loop_over_list[index - 2], number])
                )
        return list_of_numbers

    def check_increase(self) -> int:
        counter = 0
        list_of_numbers = self.list_of_sum_of_three_consecutive_numbers_in_a_list()
        for index, number in enumerate(list_of_numbers):
            if index and number > list_of_numbers[index - 1]:
                counter = counter + 1
        return counter


list_of_numbers = CountIncrease("input.txt").check_increase()

print(list_of_numbers)