# exercise 2.3: Write a program to prompt the user for hours and rate per hour 
# using input to compute gross pay.

hrs = input("Enter Hours:")
rate = input("Enter Rate per hour:")
pay = str(float(hrs) * float(rate))
print("Pay: " + pay)
