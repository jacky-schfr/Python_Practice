binary = [1, 1, 1, 1, 0, 1, 1, 0, 1]
decimal = 0
binaryrev = list(reversed(binary))

for n in range(len(binaryrev)):
    if binaryrev[n] == 1:
        decimal = decimal + 2 ** n


def binary_decimal(binary):
    binaryrev = list(reversed(binary))
    dec = 0
    for n in range(len(binaryrev)):
        if binaryrev[n] == 1:
            dec = dec + 2 ** n
    return dec


dezimal = binary_decimal(binary)

print(binary_decimal(binary))
