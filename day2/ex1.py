import re


class CalculatePosition:
    def __init__(self, filename):
        self.filename = filename

    def open_file(self):
        """Opens the file"""
        file = open(self.filename)
        return file

    def convert_file_to_list(self) -> list:
        """takes in a file and returns a list"""
        list_of_positions = []
        file = self.open_file()
        for number in file.readlines():
            # list_of_positions.append(int(re.findall(r"\d+", number).pop()))
            list_of_positions.append(number.strip())
        return list_of_positions

    def split_positions(self) -> list:
        """splits the forward position in its on list and the down position in its own list then the up position"""
        list_of_positions = self.convert_file_to_list()
        forward_list = []
        down_list = []
        up_list = []
        for position in list_of_positions:
            if "forward" in position:
                forward_list.append(int(re.findall(r"\d+", position).pop()))
            elif "down" in position:
                down_list.append(int(re.findall(r"\d+", position).pop()))
            elif "up" in position:
                up_list.append(int(re.findall(r"\d+", position).pop()) * -1)
        return [sum(up_list), sum(down_list), sum(forward_list)]

    def calculate_holizontal_and_depth_position(self):
        """claculates the depth times the forward position"""
        up = self.split_positions()[0]
        down = self.split_positions()[1]
        forward = self.split_positions()[2]
        depth = up + down
        position = depth * forward
        return position


position = CalculatePosition("sample.txt").calculate_holizontal_and_depth_position()
print(position)