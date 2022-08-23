from functions import math_operations as mo
from random import randint as rnd


def main():

    list_of_numbers = [rnd(1, 29) for _ in range(0, 9)]
    # list_of_tuples = [(rnd(0, 10), rnd(21, 39)) for _ in range(0, 9)]

    a = list(map(mo.square_root, list_of_numbers))

    for i in range(0, len(list_of_numbers)):
        print(
            f"\nsqrt({list_of_numbers[i]}) ~ {a[i]}"
        )


if __name__ == "__main__":
    main()
