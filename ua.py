import os

from fake_useragent import UserAgent

def logo():
    print(r"""
 _   _                _                    _
| | | |___  ___ _ __ / \   __ _  ___ _ __ | |_
| | | / __|/ _ \ '__/ _ \ / _` |/ _ \ '_ \| __|
| |_| \__ \  __/ | / ___ \ (_| |  __/ | | | |_
 \___/|___/\___|_|/_/   \_\__, |\___|_| |_|\__|
                          |___/
  ____                           _
 / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __
| |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
| |_| |  __/ | | |  __/ | | (_| | || (_) | |
 \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|
    """)


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

ua = UserAgent()

clear()
logo()
a = int(input("Сколько штук UserAgent'ов хотите ?: "))

g = open("/storage/emulated/0/ua.txt", "w+")
for _ in range(a):
    g.write(f"{ua.random}\n")

g.close()

clear()
logo()
print("UserAgent'ы созданы и храняться в /storage/emulated/0/ua.txt !")
