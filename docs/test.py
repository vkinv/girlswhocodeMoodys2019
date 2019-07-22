print("Hello World!")
print("hi, how are you")
name=input("what's your name?")
print(name, "is your name")
answer=input("who inspires you?")
print (answer, "inpspires you!")
value=True
anotherValue=False
yetAnotherValue=True
print("&", value & anotherValue)
print("^", value ^ anotherValue)
print("==", value == yetAnotherValue)
print("or", value or anotherValue)
age=input("how old are you?")
print(age, "is your age")
i=-1
while True:
    i+=1
    if(i>20):
        break
    #1 is odd
    if(i%2 !=0):
        continue
    print(i)
    
