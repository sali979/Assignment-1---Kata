#Inspired from https://www.tutorialspoint.com/roman-to-integer-in-python
class conversion(object):
    # Assigns a dictionary for roman numeral to int conversion
   def intOutput(self, s):
      rom = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
      i = 0
      numInt = 0
      # Performs calculations for conversion
      while i < len(s):
         if i+1<len(s) and s[i:i+2] in rom:
            numInt+=rom[s[i:i+2]]
            i+=2
         else:
            #print(i)
            numInt+=rom[s[i]]
            i+=1
      return numInt
ob1 = conversion()
# test output 
# print(ob1.intOutput('IV'))
# Requests input from user to specify roman numeral
romInp = input('Enter in a roman Numeral: ')
# Prints the conversion confirmation
print( 'The Roman numeral has been converted from ' + romInp + ' to: ' )
#Outputs conversion of eithe lower or upper RN
print(ob1.intOutput(romInp.upper()))
