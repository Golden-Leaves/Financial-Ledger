hex_dict = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
}
def decimal_to_hexadecimal(number):
    global hex_dict
    remainder_list = []
    hexadecimal_number = ""
    current_quotient = number
    while abs(current_quotient) != 0:
        if abs(current_quotient) <= 15:
            remainder_list.append(current_quotient)
            break
        elif current_quotient == 0:
            remainder_list.append(current_quotient)
            break
        else:
            number_remainder = current_quotient % 16
            current_quotient = (current_quotient - number_remainder) / 16
            print(current_quotient)
            remainder_list.append(number_remainder)
    for number in remainder_list:
        hexadecimal_number += hex_dict[number]
    return hexadecimal_number

def main():

    print(decimal_to_hexadecimal(34514213351))
    
if __name__ == "__main__":
    main()