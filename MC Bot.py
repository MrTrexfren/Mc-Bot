import pyautogui
import random
import time

members = []
says = ["Hi!", "hello", "Wanna go to a Movie?"]
done = False
num_of_members = 0

while not done:
   command = False 
   new_member = None
   new_member = input("Add Member: ")

   if new_member == "done":
       command = True
   elif new_member != "done":
       command = False
   if command == True:
       done = True
       for i in range(num_of_members):
           print(members[i])
   elif command == False:
       members.append(new_member)
       num_of_members += 1

while True:
    pyautogui.press("t")
    pyautogui.typewrite(random.choice(says))
    pyautogui.typewrite(" ")
    pyautogui.typewrite(random.choice(members))
    pyautogui.press("enter")
    pyautogui.press("esc")
    time.sleep(2)


    
    
