def plusOne(digits: list[int]) -> list[int]:
    sDigits = [str(digit) for digit in digits]

    ival = int("".join(sDigits))
    ival += 1

    sDigits = list(str(ival))

    iDigits = [int(digit) for digit in sDigits]

    return iDigits


if __name__ == "__main__":
    plusOne([1, 2, 3])
