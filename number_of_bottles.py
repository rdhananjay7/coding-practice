"""
Given numBottles full water bottles, you can exchange numExchange empty water bottles for one full water bottle.
The operation of drinking a full water bottle turns it into an empty bottle.
Return the maximum number of water bottles you can drink.
Leetcode problem: https://leetcode.com/problems/water-bottles/
"""


def num_of_full_bottles(num_bottles, num_exchange):
    return num_bottles // num_exchange


def get_empty_bottles(num_bottles, num_exchange):
    return num_bottles % num_exchange


class Solution():
    def num_water_bottles(self, num_bottles, num_exchange, empty_bottles=0):
        if num_bottles + empty_bottles < num_exchange:
            return num_bottles

        updated_num_of_bottles = self.num_of_full_bottles(num_bottles + empty_bottles, num_exchange)
        empty_bottles = self.get_empty_bottles(num_bottles + empty_bottles, num_exchange)
        print(updated_num_of_bottles, empty_bottles)
        return num_bottles + self.num_water_bottles(updated_num_of_bottles, num_exchange, empty_bottles)


if __name__ == "__main__":
    solution = Solution()
    print(solution.num_water_bottles(15, 4))
