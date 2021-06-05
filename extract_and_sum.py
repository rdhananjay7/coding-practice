"""
Given a String, extract out all the numbers and print sum of all the numbers(Note: its numbers, not digits).
Assume that numbers can be in the range [-2147483648 to 2147483647]

Sample 0:
Input: abc22def42ghi123
Output: 187
Explanation: 22+42+123= 187

Sample 1:
Input: ~@123...33def4u55
Output: 215

Sample 2:
 Input: #@1234567890abc
Output: 1234567890

Sample 3:
Input: 00hello00world000000OK
Output: 0
"""


def extract_and_sum(input_string):
    length = len(input_string)
    idx = 0
    output = 0

    while idx < length:
        char = input_string[idx]
        current_number = ""
        if char.isdigit():
            if idx >= 0 and input_string[idx - 1] == "-":
                current_number += "-"
            current_number += char
            idx += 1
            while idx < length and input_string[idx].isdigit():
                current_number += input_string[idx]
                idx += 1
        idx += 1
        if current_number:
            output += int(current_number)

    return output if float(output) < float("inf") else None


if __name__ == "__main__":
    input_string = "srf2147483647sdfsd7692147214748364721474821sdf"
    result = extract_and_sum(input_string)
    print(result)

"""
Test data
1. "" -> None
2. "abs-2147483648mbjdkhf686872" 
3. "abs-2147483648mbjdkhf-686872" -> Fail
4. "srf2147483647sdfsd-769873"
5. "srf2147483647sdfsd769873srf2147483647sdfsl"
6. "2147483647"
7. "-2147483647"
8. "hjkbsdkfbkjksdhknsj" -> None
9. "JHVJHB(&#nnsjd*%*"
10. "JHVJH324B(&34534#nnsj-132123d*%*"
"""



