
###Creating the GTIN-8

D1 = int(input("Please input the first digit: "))
D2 = int(input("Please input the second digit: "))
D3 = int(input("Please input the third digit: "))
D4 = int(input("Please input the fourth digit: "))
D5 = int(input("Please input the fifth digit: "))
D6 = int(input("Please input the sixth digit: "))
D7 = int(input("Please input the seventh digit: "))

num1 = D1*3
num2 = D2*1 
num3 = D3*3 
num4 = D4*1
num5 = D5*3
num6 = D6*1
num7 = D7*3

numSub = num1+num2+num3+num4+num5+num6+num7
x = numSub

print("The answer is" , numSub)

if(numSub % 10):
    numSub = numSub + ( 10 - numSub % 10)
D8 = numSub - x
print("The eigth digit is" , D8)
print("So the resulting GTIN-8 is:" ,D1,D2,D3,D4,D5,D6,D7,D8)

###Validating the GTIN-8

print("We now have to validate the GTIN-8 created previously")

num1a = D1*3
num2a = D2*1 
num3a = D3*3 
num4a = D4*1
num5a = D5*3
num6a = D6*1
num7a = D7*3
num8a = D8*1

n = num1a+num2a+num3a+num4a+num5a+num6a+num7a+num8a
print(n)

if n % 10 == 0:
    print("The GTIN-8 produced is valid.")
else:
    print("The GTIN-8 is not valid.")



    
