import winsound
from tkinter import *
import threading
from threading  import  Thread
import os
import sys
import pyautogui
from pynput.keyboard import Key, Controller

#import the keyboard
keyboard = Controller()

#Defining some IMP variables 
global frequency ,duration,exit_flag
exit_flag = False

#create  window
window  = Tk()
window.geometry("1000x1000")
window.title("Automatic  Parking System  using ANPR")

#variables for the beep sound 
frequency = 800
duration= 300

#Thread exit event handler to close the thread safely 
exit_event = threading.Event()

#label on the window
title = Label(window, text = "Automatic Parking System Using ANPR ",font=('Arial', 20)).place(x=250,y=50)


#Text grid to show the  results of the detection
text  =  Text(window)
text.place(x=100 ,y=400,width=800,height=200)

#read file and print the output on the output screen

with open('file.txt', 'w') as f:
            print("Output will  be  shown here  ",file=f) 
f.close()  

#black background   for  the window
window.configure(background="black")

#command for button
def runA():
    global exit_flag 
    data2 = "H"
    while exit_flag == False:
        with open('file.txt', 'r') as file:
            data = file.read()
        if(data2 !=  data):
            data2  = data
            text.insert(END,data)
            if(data != "Cannnot recognize the car entry  denied" or "Output will  be  shown here"):
                frequency = 800
                duration= 500
                winsound.Beep(frequency, duration)
        else:
            pass
    sys.exit()


#command to run the program

def run_program():
    os.system("python detect_video.py")

#close the window
def  exit():
    global exit_flag
    exit_flag = True
    print("closing the application : )")
    window.destroy()
    #press the q to exit the running script
    pyautogui.keyDown("ctrl")
    #release the key after the press
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')
    t1.join()


#button
btn = Button(window,text="Start Cam",bd = '5',command=threading.Thread(target=run_program).start,activebackground = "pink", activeforeground = "blue").place(x=430,y=180,height=50,width=150)
btn = Button(window,text="Close App ",bd = '5',command=exit,activebackground = "pink", activeforeground = "blue").place(x=430,y=250,height=50,width=150)




#Running the thread
t1 = Thread(target = runA)
t1.daemon = True
t1.start()



window.mainloop()

