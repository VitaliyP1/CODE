largest = -1
smallest = -1
while True:
    num1 = input("Enter a number: ")
    num=float(num1)
    if num == "done":
        break
    #elif isinstance(num, string):
        #break
    elif num>largest:
       largest= num
    elif num<smallest:
        smallest= num
    else:
        return num
    print(num)

print("Maximum", largest)