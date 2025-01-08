def binary_calculator(bin1, bin2, operator):

    if bin2 == "00000000" and operator == "/":
            return "NaN"
    for x in bin1 and bin2:
        if x != "1" or x != "0":
            return "Error"
        else:
            result = 0
            for place, diget in enumerate(bin1[::-1]):
                result += int(diget) * (2**place)
            return str(result)
            if bin2 == "0" and operator == "/":
                return "NaN"
