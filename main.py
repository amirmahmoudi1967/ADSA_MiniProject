import sys
#from Steps_Project import * 

from .Step1 import run_step1

ARG = str(sys.argv[1])

def main(): 
  if ARG == "1":
    run_step1.run_tournament() 
    run_step1.run_game_points()

if __name__ == "__main__" : 
    main()


