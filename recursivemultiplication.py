num1= int(input("Frst number: "))
num2= int(input("Sec number: "))

def mul(num1, num2):
    if num1<0 and num2<0:
        return (mul(abs(num1), abs(num2)))
    if num2<0:
        return( mul(num2, num1))
    if num2==0:
        return 0
    else:
        return (num1+ mul(num1, num2-1))

print(mul(num1, num2))
