class Solution:

    def sum_of_multiples(self, input_range):
        result = 0

        for number in range(input_range):
            if self.is_multiple_of_number(number, 3) or self.is_multiple_of_number(number, 5):
                result += number
        return result

    @staticmethod
    def is_multiple_of_number(number, is_multiple_of):
        return number % is_multiple_of == 0


if __name__ == "__main__":
    range_ = 1000
    solution = Solution()
    sum_of_multiples = solution.sum_of_multiples(range_)
    print(sum_of_multiples)
