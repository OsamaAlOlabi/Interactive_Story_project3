print('''
*******************************************************************************
                                       .hMM                 NMh.                                    
                                      -NMMM.               `MMMN:                                   
                                     `NMMMMy               yMMMMN`                                  
                                     +MMMMMMs-:/+ossso+/:-sMMMMMM+                                  
                                     oMMMMMMMNMMMMMMMMMMMNMMMMMMMo                                  
                                     -MMMMMMMMMMMMMMMMMMMMMMMMMMM:                                  
                                    -hMMMMMMMMMMMMMMMMMMMMMMMMMMMh-                                 
                                  `sNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNs`                               
                                 .dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd.                              
                                `dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm`                             
                                yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy                             
                               -MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM-          o                 
                               oMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMo         oM.                
                               sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy        oMM:         `      
                               oMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMs      `oMMN+     `-/y/      
                               -MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM:     `yMMy-:  `/sdNMs       
                                hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd     `hMMs`   `sMMMMo        
                                .mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN-    .dMMo   `/dMMmho         
                                 -mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm-    `mMM+  `/dMMmo`           
                                  .hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh.     /MMN `/dMMmo`   `+yysso+/.
                                    /mMMMMMMMMMMMMMMMMMMMMMMMMMMMm/       .NMMsdMMNo`  `./ymMMNh+-` 
                                     `/hNMMMMMMMMMMMMMMMMMMMMMNd/`         /MMMMMs.``-ohNMNdo:`     
                                        .+hMMMMMMMMMMMMMMMMMh+.          `:dMMNMMNmmNMMNy/.         
                                        .smMMMMMMMMMMMMMMMMMms-         :dMMNo./shddho:`            
                                      :hMMMMMMMMMMMMMMMMMMMMMMMh:     :dMMNo`                       
                                    .hMMMMMMMMMMMMMMMMMMMMMMMMMMMh. :dMMNs`                         
                                   +MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdMMNs`                           
                                 `yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMs`                             
              `                 `hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd`                             
      `.:+shmN-                 hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh                             
    /dNNMMMMMm                 oMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMo                            
     .dMMMMMMo                .MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM-                           
    :dMMNdMMM.                yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh                           
   sMMNo``-sh                .MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM.                          
  sMMm-     `                +MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMo                          
 +MMN-                       hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh                          
`NMM+                        dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm                          
+MMm                         mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN                          
dMMs                         NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN                          
NMM/                         MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM`                         
MMM:                        .MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM.                         
NMM/                        :MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM:                         
hMMs                        +MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM+                         
/MMN`                       oMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMs                         
`mMMs                       sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy                         
 :NMM+                      sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy                         
  /NMMo`                    +MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMo                         
   -mMMd/`               `.:yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM-                         
    `oNMMmy/-````````-/oydNMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh                          
      `/hNMMMNmmdmmNMMMMNNho:-dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd.                          
         `:+syhdddhhyo+:.     `oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNo`                           
                                `/hNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNh+`                             
                                    -/shmNMMMMMMMMMMMMMMMMMMMNmhs+-`                                
                                          `.-://+++++++//:-.`                     
*******************************************************************************
''')


# Highlighting Important Messages
def border_msg(msg):
    count = len(msg) + 2  # dash will need +2 too
    dash = "-" * count

    print(f"+{dash}+")
    print(f"| {msg} |")
    print(f"+{dash}+")


# Username
user_name = input("What is your name?\n")

# Welcome Message
print(f"Welcome to hell lord {user_name}.\nThere is one rule here, SURVIVE.")

# Keep track if the game ended or not (Game still on = True, Game ended = False)
game_state = True

# Game notes put in a dictionary
event_notes = { 0: "Invalid choice. Please type a number from the list",

                1: 'Dang, no one ever has thought of doing that!\n'
                    'Congratiolations, you have escaped hell.\n'
                    'Oh god, you should\'ve seen the look on your face.\n'
                    'ofcourse you didn\'t escape, no one ever does.\n'
                    'You tripped and fell on your head.\n'
                    'You DIED!\n',

               2: "You have slain every demon in Hell.\nCongratiolations you are now the DEVIL",

               3: "Did you really think you could outrun demons?. A demon has picked up the sword and "
                    "thrusted it through your heart. "
                    "\nThe demon got a huge promotion and became the DEVIL.\n",

                4:  "You walk by the sword without picking it up, fighting every urge in your body to do so.\n"
                    "You reach the gate and you knock 3 times. The gate opens unleashing a horde of demons.\n"
                    "You try to run away, but it's too late, they devour your soul.\n"}

# Game choices put in a dictionary
event_choices = {1: "\nYou have just arrived to the Devil's facility in AREA 51.\n"
                    "What do you want to do?:\n"
                    "(1)- Walk inside\n(2)- Run away and leave hell",

                 2: "You open the door to see a locked gate infront of you and you find a sword laid down on the floor.\n"
                    "You notice a note near the sword that says \"This cursed sword, is forged from the devil himself.\"\n"
                    "What do you do?:\n"
                    "(1)- Pick up the sword\n"
                    "(2)- Knock on the locked gate",

                 3: "Once you pick it up you feel your whole body is being filled with power, dark power.\n"
                    f"The gate opens, and a hundreds of demons start running towards you screaming lord {user_name}.\n"
                    "What do you do?:\n"
                    "(1)- Fight them all\n"
                    "(2)- Throw the sword away and run."}


# Main game code in here
def welcome_to_hell():
    global event_choices
    global  event_notes
    global game_state


    # if game state is TRUE keep playing, if FALSE stop the game
    while game_state == True:

        print(event_choices[1])
        user_input = input("> ")

        if user_input == "1":
            while True:
                print(event_choices[2])
                user_input = input("> ")

                if user_input == "1":
                    while True:
                        print(event_choices[3])
                        user_input = input("> ")
                        if user_input == "1":
                            print(event_notes[2])
                            game_state = False
                            repeat()
                            break
                        elif user_input == "2":
                            print(event_notes[3])
                            game_state = False
                            repeat()
                            break
                        else:
                            print(event_notes[0])

                elif user_input == "2":
                    while True:
                        print(event_notes[4])
                        game_state = False
                        repeat()
                        break
                else:
                    print(event_notes[0])

        elif user_input == "2":
            print(event_notes[1])
            game_state = False
            repeat()
        else:
            print(event_notes[0])

# MARK: - Game Repeat Function
def repeat():
    global game_state

    while game_state == False:

        border_msg('The game has ended. Would you like to play again? "Y" or "N"')

        user_input = input("> ")

        if user_input == "y":
            game_state = True
            welcome_to_hell()
        elif user_input == "n":
            print("Game Over")
            exit()
            break
        else:
            print("Choose Y or N")


welcome_to_hell()
