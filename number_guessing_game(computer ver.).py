import random
def main():
    print("Welcome to the number guessing game!")
    print("The computer will try to guess your number, the number which the computer has the most attempt on wins." + "\n")
    print("*Note: It may take a while if the number range is large.")
    while True:
      try:
            print("Type 'quit' to quit the program.")
            attempts = 0 #Minor vocab nuiance, retry counts the times it guessed INCORRECTLY, while attempts counts the number of times it guessed
            player_number_range_lowest = int(input("Enter the lowest number in your desired range(whole): "))
            player_number_range_highest = int(input("Enter the highest number in your desired range(whole): "))
            player_number = int(input(f"Enter a whole number within  {player_number_range_lowest}-{player_number_range_highest} (inclusive): "))
            
            if player_number_range_highest == "quit" or player_number_range_lowest == "quit" or player_number == "quit":
                return
            
            if player_number_range_lowest < 0 or player_number_range_highest < 0:
                print("Error: Number most not be negative.")
                continue
        
            if  player_number_range_lowest > player_number_range_highest:
                print("Error: The lowest number must be less than or equal to the highest number.")
                continue
            
            if player_number < player_number_range_lowest or player_number > player_number_range_highest:
                print(f"Error: The number must be within the range {player_number_range_lowest}-{player_number_range_highest}.")
                continue
            
            number_list = [number for number in range(player_number_range_lowest,player_number_range_highest + 1, 1)]
            # middle_index = len(number_list) // 2 
            # middle_number = number_list[middle_index]
            # current_number = middle_number
            current_number = number_list[len(number_list) // 2]
            
            
            # while current_number != player_number:
            #     if current_number < player_number:
            #         current_number = random.randint(current_number + 1, player_number_range_highest) #current_number is clearly not the desired number, hence +1
                
            #     elif current_number > player_number:
            #         current_number = random.randint(player_number_range_lowest, current_number - 1) #current_number is clearly not the desired number, hence -1
    
            #     attempts += 1
            if current_number == player_number: #In case the number is litreally in the middle already lol
                pass
            else:
                while current_number != player_number:
                    if current_number < player_number:
                        current_number_index = number_list.index(current_number)
                        highest_number_index = number_list.index(player_number_range_highest)
                        middle_number_index = (current_number_index + highest_number_index) // 2
                        current_number = number_list[middle_number_index]
                        
                    elif current_number > player_number:
                        current_number_index = number_list.index(current_number)
                        lowest_number_index = number_list.index(player_number_range_lowest)
                        middle_number_index = (current_number_index + lowest_number_index) // 2
                        current_number = number_list[middle_number_index]
                        
                    attempts += 1
            
            attempts += 1
            print(f"Your number is {player_number}!")
            print(f"It took the computer {attempts} attempts to find your number!")

              
          

      except ValueError:
          print("Invalid input, please enter a whole number.")
      except MemoryError:
          print("The computer ran out of memory, your number was too large to compute.")
      except IndexError:
          print("IndexError, this is not your fault, please try again.")
if __name__ == "__main__":
    main()