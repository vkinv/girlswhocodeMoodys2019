start= '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a giant maze.
A sign is hanging from the ivy: "You have one hour. Don't touch the walls".
There is a hallway to your right and to your left.
'''

print(start)

print("type 'left' to go to the left or 'right' to go to the right.") 
user_input= input()
while user_input != "left" and user_input != "right":
    print("type 'left' to go to the left or 'right' to go to the right.")
    user_input= input()
if user_input =="left":
    print("You decide to go left and there is a monster.Do you want to go back or fight?")
    print("type 'fight' to stay or 'back' to go the right")
    user_input=input()
if user_input =="fight":
    print("You died.")
if user_input== "back":
    print("You tripped over a rock on the way back and you died.")
elif user_input == "right":
     print("You choose to go right and there is a meadow.Do you want to pick a flower?")
     print("type 'pick' to pick a rose or 'don't pick' to not pick a flower.")
     user_input=input()

if user_input =="pick" :
    print("You picked a deadly rose and it killed you.")

if user_input =="don't pick":
    print("It turns out the flowers were poisonous and you safely found an exit.")
