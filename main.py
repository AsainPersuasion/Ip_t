import threading
import tkinter
from tkinter import *
from pythonping import ping
import datetime

root = Tk()

start_ping_pressed = 0

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

##function to write a string top .txt file
def Write_To_Text(fileName, info):

    with open(fileName + ".txt", "a") as f:
        f.write("\n"+info)

    f.close()

##function which pings an ip
def Target_Online(Ip):

    resp = [ping(Ip, count=1, timeout = 1),ping(Ip, count=1, timeout = 1),ping(Ip, count=1, timeout = 1),ping(Ip, count=1, timeout = 1)]
    offline = 0

    for x in range(4):

        if "Request" in str(resp[x]):
            offline += 1

    if offline < 4:
        return True
    else:
        return False



def Ping_Tracker(lable):
    targetIp = "192.168.1.73"
    amount_of_consetuive_disconnects = 0
    amount_of_censetuive_connects = 0
    while True:
        if Target_Online(targetIp) == True and amount_of_consetuive_disconnects == 0 :
            result = "Connected to device at " +str(datetime.datetime.now())
            lable.config(text=result)
            Write_To_Text("text", result)
            amount_of_consetuive_disconnects+=1
            amount_of_censetuive_connects = 0

        if Target_Online(targetIp) == False and amount_of_censetuive_connects == 0:
            result = "Disconnected to decive at " + str(datetime.datetime.now())
            lable.config(text=result)
            Write_To_Text("text", result)
            amount_of_censetuive_connects+=1
            amount_of_consetuive_disconnects = 0

def Start_Pinging(lable):
    counter_thread  = threading.Thread(target=Ping_Tracker, args = (lable,))
    counter_thread.start()


def Main_Screen():

    newWindow = tkinter.Toplevel(root,width=600, height=300)
    display_lable = Label(newWindow, borderwidth=5, text="test")
    ip_lable = Label(newWindow, text="Please enter your targets IP ")
    ip_input = Entry(newWindow)
    start_attack_button = Button(newWindow, text="Press to start pinging your target", command=lambda: Start_Pinging(display_lable))

    display_lable.place(x=200, y=50)
    ip_lable.place(x=120,y=100)
    ip_input.place(x=310,y=100)
    start_attack_button.place(x=200,y=150)
    # args = (ip_input, display_lable,)


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
        Main_Screen()
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

    Main_Screen()

    # root.mainloop()











