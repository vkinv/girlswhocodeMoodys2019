# --- Define your functions below! ---
from random import*
def pick_a_greeting(name):
  greetings=["Hello","Hey","Hi","Hola","What's up","salutations"]
  rand=Random()
  greet=rand.choice(greetings) +", " +name +"!"
  return greet


# --- Put your main program below! ---



def game():
  print("Want to play a game?")
  answer=input()
  if answer== "yes":
    print("okay, think of a number between 1 and 10.")
    answer=input()
    print("How did you know?")
    print (answer+", is the answer!")
    
def main():
  print(" I am a chatbot. My name is Kevin, what is yours?")
  name=input()
  greet=pick_a_greeting(name)
  print(greet)
  print (name+", is such a lovely name!")
  print("How are you on this wonderful day?")
  answer=input()
  print(answer+", I am feeling that way too.")

  while True:
    game()
    answer = input(" (what will you say?) ")
    print("That's sounds really cool!")
    print("Want to hear a ghost joke?")
    response=input()
    if response=="yes":
      print("That's the spirit")
    else:
      print("Fine, be boring.")
    print("Well I wish I could stay but I have to go now friend. I enjoyed our chat.")
    farewell=input()
    if farewell=="goodbye" or "bye":
      print( "See you again next time.")
      break
    if farewell != "goodbye"or"bye":
      print("Have a wonderful day!")
      break

    
    
 

  
  


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()


