def sqrt(number):
    if number == 0:
        return 0

    if not number:
        return None

    start = 0
    end = number

    while start <= end:

        middle = (start + end) // 2

        mid_square = middle * middle

        if mid_square == number:
            return middle

        elif mid_square < number:
            start = middle + 1
            square_root = middle

        else:
            end = middle - 1

    return square_root


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
print("Pass" if (69 == sqrt(4761)) else "Fail")
print("Pass" if (84 == sqrt(7056)) else "Fail")
print("Pass" if (1 == sqrt(2)) else "Fail")

# 0 input
print("Pass" if (0 == sqrt(0)) else "Fail")

# Large Input
print("Pass" if (1000 == sqrt(1000000)) else "Fail")
