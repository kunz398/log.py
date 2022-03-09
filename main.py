import datetime as dt

def createLog(message):
    todaysDate_Time = str(dt.datetime.today().strftime('%Y-%B-%d %I:%M:%S %p'))
    f = open("log.log", "a+")
    f.write(todaysDate_Time + "\t" + message + " \n")
    f.close()

if __name__ == '__main__':
    createLog("Message")

 ### 2022-March-09 06:35:26 PM        Messages
 
  
