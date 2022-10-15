import vk_api, time, os, logging
from random import randint
from datetime import datetime

#logging.basicConfig(level=logging.DEBUG, filename="vk_log.log",filemode="w")
clear = lambda: os.system('cls')
clear()
level = input("File or text: F/T ")
if level == "F":
    tokenvkfile = input("File with token: ",)
    tokenvkread = open(tokenvkfile,'r')
    tokenvk = tokenvkread.read()
elif level == "T":
    tokenvk = input("Token: ",)
vk=vk_api.VkApi(token=tokenvk)
tmin = input("Time min (sec) ",)
tmax = input("Time max (sec) ",)
while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    randtime = randint(int(tmin), int(tmax))
    vk.method("account.setOnline")
    print(current_time, "Online!") 
    print(current_time,"Next try:", int(randtime/60), "min (sec:",randtime,")")
    time.sleep(randtime)
    clear()
