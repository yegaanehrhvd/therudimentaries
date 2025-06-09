#BinarytoDecimalConverter
def binary_to_decimal(n):
    if not isinstance(n, str):
        raise ValueError("Enter the binary number in the form of a string!")
    decimal = 0
    length = len(n)
    for i in range(length):
        bit = int(n[i])
        power = length - i - 1
        decimal += bit * (2**power)
    print(f"The decimal number is {decimal}")
    return decimal

binary_to_decimal("1101")