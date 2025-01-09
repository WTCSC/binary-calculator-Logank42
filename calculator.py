def binary_calculator(bin1, bin2, operator):

    if bin2 == "00000000" and operator == "/": #Checks if your trying to divide by 0
        return "NaN"

    for x in bin1: #Checks the first number for anything other than 1 and 0
        if x not in "10":
            return "Error"
    for x in bin2: #Checks the second number for anything other than 1 and 0
        if x not in "10":
            return "Error"

    num1 = bin_to_dec(bin1)
    num2 = bin_to_dec(bin2)

    if num1 < num2 and operator == "-": #Checks if your going into the negative
        return "Overflow"

    elif num1 + num2 > 255 and operator == "+": #Checks if your going higher than 255
        return "Overflow"
    
    elif (num1 * num2) > 255 and operator == "*": #Checks if your going higher than 255
        return "Overflow"

    elif operator == "+": #Addition
        decresult = num1 + num2
        binresult = dec_to_bin(decresult)
        return binresult.zfill(8) #Fills any non filled in numbers with an eight character cap

    elif operator == "-": #Subtraction
        decresult = num1 - num2
        binresult = dec_to_bin(decresult)
        return binresult.zfill(8)

    elif operator == "/": #Division
        decresult = num1 // num2
        binresult = dec_to_bin(decresult)
        return binresult.zfill(8)

    elif operator == "*": #Multipulication
        decresult = num1 * num2
        binresult = dec_to_bin(decresult)
        return binresult.zfill(8)


def bin_to_dec(num): #Converts the binary into decimal

            result = 0
            for place, diget in enumerate(num[::-1]):
                result += int(diget) * (2**place)
            return result

def dec_to_bin(num): #Converts the decimal into binary

    result = "" if num > 0 else "0"
    while num > 0:
        result = str(num % 2) + result
        num //= 2
    return result