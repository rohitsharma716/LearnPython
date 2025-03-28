try:
    x = 5/0
except ZeroDivisionError:
    print("error in division for this number")



try:
    num = int(input("Enter a number :"))
    result = 10/num
except ZeroDivisionError:
    print("cannot divide by zero !")
except ValueError:
    print("enter the valid number")





try:
    x = int("abc")
except Exception as e:
     print("error is:",e)