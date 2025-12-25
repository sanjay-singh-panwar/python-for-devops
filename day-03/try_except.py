print("Hello")

try: 
    a= input("Enter a number:")
    b = int(input("Enter a second num:"))
    print(a/b)
    for i in range(1,11):
        print(f"{a} x {i} = {a*i}")
except ValueError:
    print("Invalid value...")

except ZeroDivisionError:
    print("can't devide by 0")

except TypeError:
    print("wrong data type")



