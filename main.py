# First Program

#Define variables for first and last name and ask question 
First_Name = str(input("What is your first name? "))
Last_Name = str(input("What is  your last name? "))

#Print out variables in reverse order
print(Last_Name,First_Name)

# Second Program

#The EOZ (Even, Odd, Zero) basically is just a way to check for even/odd numbers because of how even numbers can't have a remainder in this situation (more down below). The number variable is defined and asks you to input a number.
Number = int(input("Input a number: "))
EOZ = Number % 2

#If it is equal to 0, print out a 0
if Number == 0:
  print("It is a 0")

#If the remainder is over a 0, it is odd because even numbers don't have remainders when divided by two.
elif EOZ > 0:
  print("It is odd")

#If nothing else, it's even
else:
  print("It is even")

# Third Program

#Input variables asking for between 1-365
day = int(input("What day of the year is it (Between 1 and 365)? "))

#Millions of lines of code to determine all of the months and where each day fits into it. It checks between two numbers for each months (I.E. March is between 60 and 90) and then it prints out the month, then the day minus all of the other days in the months prior. Also, you can see the months in the print part of each block.
if day >= 1 and day <= 31:
  print("January, ",day)

elif day >= 32 and day <= 59:
  print("February, ",day - 32)

elif day >= 60 and day <= 90:
  print("March, ",day - 59)

elif day >= 91 and day <= 120:
  print("April, ",day - 90)

elif day >= 121 and day <= 151:
  print("May, ",day - 120)

elif day >= 152 and day <= 181:
  print("June, ",day - 151)

elif day >= 182 and day <= 212:
  print("July, ",day - 181)

elif day >= 213 and day <= 243:
  print("August, ",day - 212)

elif day >= 244 and day <= 273:
  print("September, ",day - 243)

elif day >= 274 and day <= 304:
  print("October, ",day - 273)

elif day >= 305 and day <= 334:
  print("November, ",day - 304)

elif day >= 335 and day <= 365:
  print("December, ",day - 334)

# Fourth Program

#I didn't use variables for efficiency. We only needed the number 5 so I thought it would be pointless to use a variable and set it to 5 when I could just write 5.
for x in range(5 + 1):
    for y in range(5, 0 + x, -1):
        print(y, end = ' ')
    print()
#This block of code just creates the 5 lines and puts them into the reverse order pattern.

# Fifth Program

#Variable so people can input the number for the rows in the pattern.
row_number = int(input("Pick a number to put into the pattern: "))

#The same thing as last program, but the #5's were replaced by row_number so that it isn't a set number, but an inputtable number.
for x in range(row_number + 1):
    for y in range(row_number, 0 + x, -1):
        print(y, end = ' ')
    print()