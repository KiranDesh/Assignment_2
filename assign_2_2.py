#2.	Write a program which will accept ‘N’ number from user and print 1 through ‘N’ numbers 
#in table format in batch of 100’s .e.g if user enters 1000 
#then create 10 tables of 10X10 size ( 1 through 100, 101 through 200, 201 through 300 …. So on )

number = int(input("Enter till what number you want tablular format: "))
for i in range(1,11):
    for j in range(i,number+1,10):
        print("\t",j,end='')
    print()

    
    