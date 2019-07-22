start= '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a giant maze.
A sign is hanging from the ivy: "You have one hour. Don't touch the walls".
There is a hallway to your right and to your left.
'''

print(start)

print("type 'left' to go to the left or 'right' to go to the right.") 
user_input= input()
if user_input =="left":
    print("You decide to go left and there is a monster.")

elif user_input== "right":
    print("You choose to go right and there is a meadow.")
