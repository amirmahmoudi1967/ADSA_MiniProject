import sys, os
from Steps_Project import * 
from termcolor import colored 
#https://pypi.org/project/termcolor/


def menu(): 
  print("\t\t\t<<  Menu of the Mini-problem of ADSA  >>")
  print("\n[1] Step 1 : To organize the tournament")
  print("[2] Step 2 : Professor Layton < Guybrush Threepwood < You ")
  print("[3] Step 3 : I dont see him, but i can give proofs he vents !")
  print("[4] Step 4 : Secure the last tasks")
  print("[9] Clear the console.")
  print("[0] Exit the program.")


def step1_menu():

  print("[1] : Running a simulation of a tournament.")
  print("[2] : Running a simulation of a random game of the tournament.")
  print("[0] : Exit the step 1 and return to the main menu of the program.\n")
  
  option_step1 = int(input("Enter your option of Step 1 : "))
  os.system("clear")

  while option_step1 != 0:
    
    if option_step1 == 1: 
      Run_Step1.run_tournament()
      break

    elif option_step1 == 2: 
      Run_Step1.run_game_points()
      break

    elif option_step1 == 0: 
      os.system("clear")
      menu()
    
    else: 
     print("\nInvalid option. Please try again !")      
      


print(colored("\t\t\tWelcome to our program for the ADSA Mini-Project of Among Us :", "red",attrs =['blink']))
print(colored("\nDone by LAHBABI Yassine & MAHMOUDI Amir","grey","on_white"))
print("\nESILV - DIA 4\n")

menu()
option = int(input("Enter your option : "))
os.system("clear")


while option !=0:
  
  if option == 1: 
    print("\nOption 1 has been called successfully.\n")
    step1_menu()
  
  elif option == 2: 
    print("\nOption 2 has been called successfully.\n") 
    Run_Step2.test_has_seen()
  
  elif option == 3: 
    print("\nOption 3 has been called successfully.\n")
    Run_Step3.run_Pathfinding_graph()
  
  elif option == 4: 
    print("\nOption 4 has been called successfully.\n")
    Run_Step4.run_hamilton()
  
  elif option == 9: 
    os.system("clear")
    print("\n Console cleared successfully.\n")

  else: 
    print("\nInvalid option. Please try again !")

  
  print()
  menu()
  option = int(input("Enter your option : "))   
  os.system("clear")

print("\nThanks for using this program. Goodbye.")





#def main2(): 

    #Run_Step1.run_tournament() 
    #Run_Step1.run_game_points()
    #Run_Step2.test_has_seen()
    #Run_Step3.run_Pathfinding_graph()
    #Run_Step4.run_hamilton()
    #test



