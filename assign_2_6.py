#6.	Write a program to dynamically accept range ( two integers ) and print table chart for given range.
int_1 = int(input("enter from what number you want table : "))
int_2 = int(input("enter till what number you want table : "))

for i in range(1,11):
    for j in range(int_1,int_2+1):
        print("\t",i*j,end="")
    print()