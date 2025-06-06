#Luhn algorithm
def verify_card_number(card_number):
    reversed_card_number = card_number[::-1] #Luhn algorithm begins from the rightmost number, reversed the number for convienience
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    odd_digits = reversed_card_number[::2]
    even_digits = reversed_card_number[1::2]
    
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)
        
    for digit in even_digits:
        number = int(digit) * 2
        
        if number >= 10:
            number = (number//10) + (number % 10)
            
        sum_of_even_digits += number
    total = sum_of_even_digits + sum_of_odd_digits
    return total % 10 == 0 #Checks if the sum of odd and even is a multiple of 10


def main():
    while True:
      print("Enter the card number (include hyphens '-' if there are some) (Type 'q' to quit the program)")
      user_card_number = input().lower()
      if user_card_number == 'q':
        return
      card_translation = str.maketrans({'-' : '', ' ': ''})
      translated_card_number = user_card_number.translate(card_translation)
      if not translated_card_number.isdigit():
          print("Invalid card number")
          
      if verify_card_number(translated_card_number) == True:
          print("Valid credit card number")
          
      else:
          print("Invalid credit card number")
if __name__ == "__main__":
    main()
