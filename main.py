import os
import keyboard


def clear():
    os.system("cls")
    print("""\033[37m\
 
                             /$$                                                        
                            | $$                                                        
                            | $$        /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$ 
                            | $$       |____  $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$
                            | $$        /$$$$$$$| $$  \ $$| $$  \ $$| $$$$$$$$| $$  \__/
                            | $$       /$$__  $$| $$  | $$| $$  | $$| $$_____/| $$      
                            | $$$$$$$$|  $$$$$$$|  $$$$$$$|  $$$$$$$|  $$$$$$$| $$      
                            |________/ \_______/ \____  $$ \____  $$ \_______/|__/      
                                                 /$$  \ $$ /$$  \ $$                    
                                                |  $$$$$$/|  $$$$$$/                    
                                                 \______/  \______/                     
    """
    )
    print("                         ")
    print("\033[37m                                                   (MADE by dannw)")
    print("                         ")
    print("                         ")
    print("                         ")
    print("                         ")
    print("                         ")


clear()
state = False

def handler():
    global state
    if state:
        toggle_internet(arg=False)
        print("\033[31mLag switch:", "Disabled")
        state = False
    else:
        toggle_internet(arg=True)
        print("\033[32mLag switch:", "Enabled")
        state = True

def toggle_internet(arg):   
    if arg == True:
        os.system('ipconfig /release')
        clear()
    else:
        os.system('ipconfig /renew')
        clear()



def hotkey_data():
    try: 
        file = open("key.meow", "r")
        hotkey = file.readline()
    except:
        file = open("key.meow", "w")
        print("Press the key you want to use as a bind...")
        event = keyboard.read_event()
        event = event.name
        hotkey = event
        print(f"Read hotkey as {hotkey}")
        file.write(event)
        file.close()
        print("Created file successfully, if you want to change the file, delete key.meow")
    return hotkey
hotkey = hotkey_data()

while True:
    event = keyboard.read_event()
    event = event.name
    if event == hotkey:
        handler()