#Inspired from https://www.geeksforgeeks.org/python-program-to-convert-integer-to-roman/
def romanOutput(number):
    #Assign integers and roamn numerals to lists, respectively
    numInt = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]
    rom = ["I", "IV", "V", "IX", "X", "XL",
        "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    #Performs calculations for conversion  
    while number:
        div = number // numInt[i]
        number %= numInt[i]
  
        while div:
            print(rom[i], end = "")
            div -= 1
        i -= 1
  
# Driver code
# Requests input from user to specify integer
if __name__ == "__main__":
    print('Enter in a number')
    number = input()
    print("Roman Numeral is:", end = " ")
    romanOutput(int(number))

    # test to check output
    # number = 4687
    # print("Roman value is:", end = " ")
    # romanOutput(number)