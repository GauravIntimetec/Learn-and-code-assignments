def kaprekar(number):
    num = str(number)
    count = 0
    if len(num) - len(set(num)) > 1:
        print("please enter a valin number with atleast 2 unique digit")
    else:
        next_num = None
        while next_num != 0:
            Asc = "".join(sorted(str(number).zfill(4)))
            Dsc=  "".join(sorted(str(number).zfill(4),reverse=True))
            # print(Asc, Dsc)
            count+=1
            next_num = int(Dsc) - int(Asc)
            number = next_num
            if(number == 6174):
                # print(number)
                print("this is kaprekars const.")
                break
    if count!=0:
        return count

number1 = int(input("Enter a number: "))
print(kaprekar(number1))
