"""
LeetCode Medium #1138 Alphabet Board Path
https://leetcode.com/problems/alphabet-board-path/
"""


class NewLocation:

    def __init__(self, direction=None, character=None, row=None, index=None):
        self.direction = direction
        self.character = character
        self.row = row
        self.index = index


class Solution:
    board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]

    def alphabet_board_path(self, target: str) -> str:

        result = []
        current_character = self.board[0][0]
        current_row = 0
        index = 0

        for target_char in target:
            if target_char == current_character:
                result.append("!")
            else:
                while current_character != target_char:
                    updated_position = self.get_next_poistion(current_character, current_row, index, target_char)
                    current_character = updated_position.character
                    current_row = updated_position.row
                    index = updated_position.index
                    result.append(updated_position.direction)
                result.append("!")

        return "".join(result)

    def get_next_poistion(self, current_letter, current_row, index, target_letter):
        new_location = NewLocation()

        if target_letter in self.board[current_row]:
            new_location.direction = self.get_right_left(current_row, current_letter, target_letter)
            new_location.row = current_row
            if new_location.direction == 'L':
                new_location.index = index - 1
            else:
                new_location.index = index + 1
            new_location.character = self.board[current_row][new_location.index]
        else:
            new_location.direction = self.get_up_down(current_row, index, current_letter, target_letter)
            if new_location.direction == 'U':
                new_location.row = current_row - 1
            elif new_location.direction == 'L':
                new_location.row = current_row
            else:
                new_location.row = current_row + 1
            new_location.index = self.board[current_row].index(current_letter) if new_location.direction == "U" or new_location.direction == "D" else self.board[current_row].index(current_letter) - 1
            new_location.character = self.board[new_location.row][new_location.index]

        return new_location

    def get_right_left(self, current_row, current_letter, target_letter):

        for char in self.board[current_row]:
            if char == target_letter:
                return "L"

            if char == current_letter:
                return "R"

    def get_up_down(self, current_row, current_index, current_letter, target_letter):
        row = 0
        while row < len(self.board):
            if target_letter in self.board[row]:
                return "U"
            if current_letter in self.board[row]:
                # when you are moving down and looking for z
                # you should take left if you are not in the first column (i.e. index = 0)
                if current_row == 4 and current_index > 0:
                    return "L"
                return "D"
            row += 1

    def get_row_index(self, target_letter):
        for idx in range(len(self.board)):
            if target_letter in self.board[idx]:
                return idx


if __name__ == "__main__":
    solution = Solution()
    # target = "leet"
    target = "zdz"
    result = solution.alphabet_board_path(target)
    print(result)