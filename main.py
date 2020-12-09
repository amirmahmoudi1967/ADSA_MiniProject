import sys
import curses 
from Steps_Project import * 


menu = ['Step 1 : To organize the tournament','Step 2 : Professor Layton < Guybrush Threepwood < You','Step 3 : I dont see him, but i can give proofs he vents !','Step 4 : Secure the last tasks','Exit']


def print_menu(stdscr, selected_row_idx):
  stdscr.clear()
  h, w = stdscr.getmaxyx()
  for idx, row in enumerate(menu):
    x = w//2 - len(row)//2 
    y = h//2 - len(menu)//2 + idx 
    if idx == selected_row_idx: 
      stdscr.attron(curses.color_pair(1))
      stdscr.addstr(y,x,row)
      stdscr.attroff(curses.color_pair(1))
    else : 
      stdscr.addstr(y,x,row)
  stdscr.refresh()


def print_center(stdscr,text):
  stdscr.clear()
  h,w = stdscr.getmaxyx()
  x = w//2 - len(text)//2
  y = h//2 
  stdscr.addstr(y,x,text)
  stdscr.refresh()


def main(stdscr):

  #turn off cursor blinking
  curses.curs_set(0)

  #color scheme for selected row
  curses.init_pair(1,curses.COLOR_BLACK,curses.COLOR_WHITE)

  #specify the current selected row
  current_row = 0 
 
  #print the menu
  print_menu(stdscr, current_row)

  while 1 : 
    key = stdscr.getch()
    if key == curses.KEY_UP and current_row > 0: 
      current_row -= 1 
    elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
      current_row += 1 
    elif key == curses.KEY_ENTER or key in [10,13]:
      #print_center(stdscr,"You selected'{}'".format(menu[current_row]))
      stdscr.getch()
      if current_row == len(menu)-5:
        Run_Step3.run_Pathfinding_graph()
      if current_row == len(menu)-4:
        Run_Step2.test_has_seen()
      if current_row == len(menu)-3:
        Run_Step3.run_Pathfinding_graph()
      if current_row == len(menu)-2:
        Run_Step4.run_hamilton()
      if current_row == len(menu)-1:
        break
    print_menu(stdscr,current_row)

curses.wrapper(main)




#def main2(): 

    #Run_Step1.run_tournament() 
    #Run_Step1.run_game_points()
    #Run_Step2.test_has_seen()
    #Run_Step3.run_Pathfinding_graph()
    #Run_Step4.run_hamilton()
    #test



#if __name__ == "__main__" : 
 #   main()