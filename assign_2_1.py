#1.	Write a program to print 1 to 100 numbers in following table format
number=100
for i in range(1,11):
    for j in range(i,number+1,10):
        print("\t",j,end='')
    print()