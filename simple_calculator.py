def sum(x,y):
     return x+y
def sub(x,y):
     return x-y
def mul(x,y):
     return x*y
def div(x,y):
     return x/y

print("choose a option:")
print("1.add")
print("2.substract")
print("3.multiply")
print("4.division")

while True:
         choice = input("enter choice(1/2/3/4):")
         if choice in ('1','2','3','4'):
            num1=float(input("enter the first number:"))
            num2=float(input("enter the second number:"))
            if  choice =='1':
               print(num1, "+", num2,"=",sum(num1,num2))
            elif choice =='2':
               print(num1,"-",num2,"=",sub(num1,num2))
            elif choice =='3':
               print(num1,"*",num2,"=",mul(num1,num2))
            elif choice =='4':
               print(num1,"/",num2,"=",div(num1,num2))
            next_calculation=input("try again (yes/no):")
            if next_calculation == 'no':
               break
