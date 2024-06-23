print("Welcome to my choose your own adventure game!")

name = input("What is your name? ")
print("Hello, " + name + "!")

ans = input("You are on a crowded street, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if ans == 'left':
  ans = input("You have come to a river, you can walk around or swim across. Type walk to walk around and swim to swim across: ")

  if ans == 'swim':
    print("You swam across and were eaten by an alligator.")
  elif ans == 'walk':
    print("You walked for many miles, ran out of water and lost the game.")
  else:
    print("Not a valid option. You lose.")


elif ans == 'right':
    ans = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

if ans == 'back':
    print("You go back and lose.")
elif ans == 'cross':
    ans = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")

    if ans == 'yes':
      print("You talked to the stranger and they gave you gold. You WIN!")
    elif ans == 'no':
      print("You ignored the stranger and they attacked you. You LOSE!")
    else:
      print("Not a valid option. You lose.")


else:
  print("Invalid option, you lose.")

print("Thanks for playing", name)