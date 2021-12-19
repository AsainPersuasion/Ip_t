from pythonping import ping
import datetime


##function to write a string top .txt file
def WriteToTxt(fileName, info):

    with open(fileName + ".txt", "a") as f:
        f.write("\n"+info)

    f.close()


##function which pings an ip
def TargetOnline(Ip):

    resp = [ping(Ip, count=1, timeout = 1),ping(Ip, count=1, timeout = 1),ping(Ip, count=1, timeout = 1),ping(Ip, count=1, timeout = 1)]
    offline = 0

    for x in range(4):

        if "Request" in str(resp[x]):
            offline += 1

    if offline < 4:
        return True
    else:
        return False

    print(offline)

def email():
    pass




##192.168.1.254 Real target IP
##192.168.1.158 target Ip
##targetIp = "192.168.1.254"
targetIp = "192.168.1.158"
amoutOfconsetuiveConnects=0
amoutOfconsetuiveDisconnects=0

if __name__ == '__main__':

    targetIp = input("Welcome to Ip Tracker\nPlease enter your Target's Ip: ")


    while True:


        if TargetOnline(targetIp) == True and amoutOfconsetuiveConnects == 0 :
            result = "Connected to device at " +str(datetime.datetime.now())
            print(result)
            WriteToTxt("text", result)
            amoutOfconsetuiveConnects+=1
            amoutOfconsetuiveDisconnects = 0


        if TargetOnline(targetIp) == False and amoutOfconsetuiveDisconnects == 0:
            result = "Disconnected to decive at " + str(datetime.datetime.now())
            print(result)
            WriteToTxt("text", result)
            amoutOfconsetuiveDisconnects+=1
            amoutOfconsetuiveConnects = 0
