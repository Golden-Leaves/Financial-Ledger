import math
divisor_list = []
def user_number():
    while True:
      print("Please enter the number to show the divisors, enter a number that's not 0")
      Dividend = str(input())
      is_integer = Dividend.isdigit()
      if Dividend == "0" or is_integer == False:
          print("Invalid input")
      elif is_integer == True and Dividend != "0":
          integer_dividend = int(Dividend)
          return integer_dividend
Dividend = user_number()
def Divisor(number):
    divisor_list = [divisor for divisor in range(1, number + 1) if number % divisor == 0]
    return divisor_list
Result = Divisor(Dividend)
print(f"The divisor(s) of {Dividend} are/is : {Result}")
