import vk_api, time, os, logging, random
from random import randint
from datetime import datetime

#logging.basicConfig(level=logging.DEBUG, filename="vk_log.log",filemode="w")
#clear = lambda: os.system('cls')
#clear()
level = input("File or text (Token 1 (PC)): F/T ")
if level == "F":
    tokenvkfile1 = input("File with token: ",)
    tokenvkread1 = open(tokenvkfile1,'r')
    tokenvk1 = tokenvkread1.read()
elif level == "T":
    tokenvk1 = input("Token: ",)
newtoken = input("File or text (Token 2 (Phone)): F/T ")
if newtoken == "F":
    tokenvkfile2 = input("File with token: ",)
    tokenvkread2 = open(tokenvkfile2,'r')
    tokenvk2 = tokenvkread2.read()
elif newtoken == "T":
    tokenvk2 = input("Token: ",)
tmin = input("Time min (sec) ",)
tmax = input("Time max (sec) ",)
while True:
    currenttoken = random.randint(1, 2)
    if currenttoken == 1:
        tokenvk = tokenvk1
        infotoken = "Token 1"
    elif currenttoken == 2:
        tokenvk = tokenvk2
        infotoken = "Token 2"
    vk=vk_api.VkApi(token=tokenvk)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    randtime = randint(int(tmin), int(tmax))
    vk.method("account.setOnline")
    print(current_time, "Online!", infotoken) 
    print(current_time,"Next try:", randtime/60, "min. sec:",randtime,)
    time.sleep(randtime)
    #clear()