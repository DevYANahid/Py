a = int(input("Enter Your First Number : ")); 
b = int(input("Enter Your Second Number : ")); 
c = int(input("Enter Your Third Number : ")); 

if (a>=b and a>=c):
    print("first Number is largest");
elif (b>=c):
    print("second Number is largest");
else :
    print("third Number is largest"); 


num = int(input("Enter Your Number : "));

rem = num % 2

if(rem==0):
    print("number is Even");
else :
    print("ODD")  




def convertor(Usd_vel):
    INR_vel = Usd_vel * 83
    print(Usd_vel, "USD =" , INR_vel, "INR");

convertor(int(input("enter USD = ")));


def ADD(num):
    EVEN_NUM = num % 2
    if(EVEN_NUM==0):
        print(num, "is Even" );
    else:
        print(num, "is ADD");
    
ADD(int(input("enter a number =")));
