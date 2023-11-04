print('''a pirate's treasure map
    ___
    ).x)
   (:_(
  
  Finrod




                                                                      



         __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
ejm97  %%%%

       {}           {}
         \  _---_  /
          \/     \/
           |() ()|
            \ + /
ejm 96     / HHH  \
          /  \_/   \
        {}          {}
                           ___________
                ___________)%{}%%%%%%/
               /{}%%%%%%%%/%%/%%%%%%/
              /%%\% _---_/ \/%%%%%%/
             /%%%%\/    /()|%%%%%%/
            /%%%%%|()  /+ /%%%%%%/
           /%%%%%%%\ +/HH%%\%%%%/
          /%%%%%%/%HH/_/%%%\%%%/
 ejm97   /%%%%%%/%%\/%%%%%%{}%/
        /%%%%%{}%%%/
       /
      /
     /
    /
   /''')
print("Welcome to treasure Island.")
print("Your mission is to find the treasure.")

direction = input("You're at a cross road. Where do you want to go? Type left or right. \n").lower()
if direction == "left":
  decision = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  
  if decision == "wait":
    color_door = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color would you choose? \n')
    
    if color_door == "red":
      print("You are burned by fire. Game over.")
    elif color_door == "blue":
      print("You are eaten by beasts. Game ove.")
    elif color_door == "yellow":
      print("Congratulations. You win.")
    else:
      print("Game over.")
      
    

  else:
    print("You are attacked by trout. Game Over.")


else:
  print("You fell in hole. Game over.")
  

