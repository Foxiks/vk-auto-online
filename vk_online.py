import vk_api, time, os
from random import randint
from datetime import datetime

clear = lambda: os.system('cls') # Для Linux cls меняется на clear!
clear()
level = input("Тип ввода токена (Файл/Ввод в терминал) F/T ")
if level == "F":
    tokenvkfile = input("Путь к файлу с токеном: ",)
    tokenvk = open(tokenvkfile,'r')
elif level == "T":
    tokenvk = input("Токен: ",)
vk=vk_api.VkApi(token=tokenvk.read())
tmin = input("Время минимум (сек) ",)
tmax = input("Время максимум (сек) ",)
while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    randtime = randint(int(tmin), int(tmax))
    vk.method("account.setOnline")
    print(current_time, "Онлайн обновлён!") 
    print(current_time,"Следующий запрос через", int(randtime/60), "мин (сек:",randtime,")")
    time.sleep(randtime)
    clear()