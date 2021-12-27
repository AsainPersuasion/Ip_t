import threading
import tkinter
from tkinter import *



root = Tk()

def Write_To_Txt(file_name, info):
    pass

def Read_To_Txt(file_name):
    file_info = []
    file_name = file_name + ".txt"
    f = open(file_name, "r")


    while True:
        line_info = f.readline()

        if line_info != "":
            file_info.append(line_info.split(","))
        else:
            break

    return file_info

def Counter(label):
    i=0

    while True:
        i = i+1
        label.config(text=str(i))



def main_screen():

    newWindow = tkinter.Toplevel(root,width=600, height=300)
    display_lable = Label(newWindow, borderwidth=5, text="test")
    ip_lable = Label(newWindow, text="Please enter your targets IP ")
    ip_input = Entry(newWindow)
    start_attack_button = Button(newWindow, text="Press to start pinging your target")

    display_lable.place(x=200, y=50)
    ip_lable.place(x=120,y=100)
    ip_input.place(x=310,y=100)
    start_attack_button.place(x=200,y=150)

    counter_thread  = threading.Thread(target=Counter, args=(display_lable,))
    counter_thread.start()

    root.mainloop()


def Login_Checker(username_needed, loggin_info):
    username_location = None

    if username_needed == True:
        for x in range(len(loggin_info[0])):
            if username_input.get() == loggin_info[0][x]:
                username_needed = False
                username_location = x
                print("User name is cimplete")

    if username_needed == False:
        if password_input.get() == loggin_info[1][username_location]:
            print("Pswd is corrects")
            global access_to_system
            access_to_system = True

    if access_to_system == True:
        print("Welcome to the system")
        main_screen()
    else:
        print("access dineied")


if __name__ == '__main__':



    # username_input = Entry(root, width=50, borderwidth=5)
    # password_input = Entry(root, width=50, borderwidth=5)
    # enter_button = Button(root, text="Press to enter", command= lambda: Login_Checker(True, Read_To_Txt("userinfo")))
    #
    # username_input.grid(row=0, column=0)
    # password_input.grid(row=1, column=0)
    # enter_button.grid(row=2, column=0)

    main_screen()
    #
    # root.mainloop()











