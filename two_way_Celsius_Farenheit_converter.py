#1/7/2024
import tkinter
print("Enter either 'c' or 'f'")
UnitChoice = input("°C or °F: ").lower()  # The unit that you want to convert
Temperature = float(input("Enter temperature: "))  
if UnitChoice.lower() == "c":
    Temperature = (Temperature * 9/5) + 32
    print(f" ==> {Temperature} °F")
elif UnitChoice.lower() == "f":
    Temperature = (Temperature - 32) * 5/9
    print(f"==> {Temperature} °C")
else:
    print("Please type in 'c' or 'f' ")
