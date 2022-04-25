def solution(roman):
    romanLetters = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    numberTranslation = []
    sortnumb = []
    minusNumb = []
    solution = 0
    index = 0

    for i in roman:
        numberTranslation.append(romanLetters.get(i))
        sortnumb.append(romanLetters.get(i))

    sortnumb.sort()
    sortnumb.reverse()

    while index < len(numberTranslation):
        if numberTranslation[index] != sortnumb[index]:
            minusNumb.append(sortnumb[index])
            index += 1
        else:
            solution += numberTranslation[index]
            index += 1

    if len(minusNumb) != 0:
        l = 0
        m = 1

        while l < len(minusNumb):
            if minusNumb[l] > minusNumb[m]:
                solution -= minusNumb[m]
                solution += minusNumb[l]
            if minusNumb[m] > minusNumb[l]:
                solution -= minusNumb[l]
                solution += minusNumb[m]
            l += 2
            m += 2

    return solution


print(solution("XXI"))
print(solution("CDXXIV"))
print(solution("CDXLVII"))