# Welcom to Ip info.
# This File Created By => "SpYrX" .
# You can Text Me on Telegram!
# This file created in 2022-07-16 00:15:39
import os
try:
    import requests, pyfiglet
    from time import *
    from colorama import Fore, Back, Style
    from datetime import *
except ModuleNotFoundError:
    print(Fore.GREEN + "I’m sorry but The Module is not find, so I’m Going To Download It")
    os.system("pip install requests")
    os.system("pip install pyfiglet")
    os.system("pip install time")
    os.system("pip install colorama")
    os.system("pip install datetime")
    print(Back.RED + "Ok The Module are downloaded!")
    os.system("clear")
    time.sleep(1)
Mylogo = pyfiglet.figlet_format("SpYrX")
print(Fore.RED + Mylogo)
sleep(2)
os.system("clear")
Logo = Fore.BLUE + """────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████████──██████████████──────────────────██████████──██████──────────██████──██████████████──██████████████─
─██░░░░░░██──██░░░░░░░░░░██──────────────────██░░░░░░██──██░░██████████──██░░██──██░░░░░░░░░░██──██░░░░░░░░░░██─
─████░░████──██░░██████░░██──────────────────████░░████──██░░░░░░░░░░██──██░░██──██░░██████████──██░░██████░░██─
───██░░██────██░░██──██░░██────────────────────██░░██────██░░██████░░██──██░░██──██░░██──────────██░░██──██░░██─
───██░░██────██░░██████░░██──██████████████────██░░██────██░░██──██░░██──██░░██──██░░██████████──██░░██──██░░██─
───██░░██────██░░░░░░░░░░██──██░░░░░░░░░░██────██░░██────██░░██──██░░██──██░░██──██░░░░░░░░░░██──██░░██──██░░██─
───██░░██────██░░██████████──██████████████────██░░██────██░░██──██░░██──██░░██──██░░██████████──██░░██──██░░██─
───██░░██────██░░██────────────────────────────██░░██────██░░██──██░░██████░░██──██░░██──────────██░░██──██░░██─
─████░░████──██░░██──────────────────────────████░░████──██░░██──██░░░░░░░░░░██──██░░██──────────██░░██████░░██─
─██░░░░░░██──██░░██──────────────────────────██░░░░░░██──██░░██──██████████░░██──██░░██──────────██░░░░░░░░░░██─
─██████████──██████──────────────────────────██████████──██████──────────██████──██████──────────██████████████─
────────────────────────────────────────────────────────────────────────────────────────────────────────────────
----------------------------------
Auther => SpYrX
Teleram => @spyrc
Channel on Telegram = > @HHSPX
----------------------------------
"""
print(Fore.BLUE + "Hi welcom to IP-INFO TOOL.")
choice = Fore.GREEN + """ Choose 1 or 2
[1] GET MY IP AND INFORMATION?
[2] WRITE THE IP AND GET INFORMAYION?
"""
print(Logo)
print(choice)
resp = input("choose: ")
if resp == "1":
    url = requests.get("https://ipinfo.io/json")
    z = url.json()['ip']
    x = url.json()['city']
    v = url.json()['region']
    c = url.json()['country']
    n = url.json()['loc']
    m = url.json()['org']
    a = url.json()['timezone']
    Time = datetime.now()
    print(Fore.BLUE + F"""
    Your IP : {z}
    Location : {n}
    Country : {c}
    City : {x}
    Region {v}
    ICP : {m}
    Timezone : {a}
    Time now : {Time}""")
elif resp == "2":
    Target = input(Fore.GREEN + "Please Write The IP-Addres: ").strip()
    req = requests.get("http://ip-api.com/json/"+Target).json()
    country = req['country']
    city = req['city']
    region = req['regionName']
    lat = req['lat']
    location = req['lon']
    timezone = req['timezone']
    internet = req["as"]
    Time = datetime.now()
    print(Fore.GREEN + f"""
    Target : {Target}
    Location : {location} : {lat}
    Country : {country}
    City : {city}
    Region : {region}
    ICP : {internet}
    Timezone : {timezone}
    Time now : {Time}
    """)
