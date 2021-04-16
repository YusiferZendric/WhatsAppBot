import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(.3)
chrome = pt.locateOnScreen("chrome.png", confidence=.6)
pt.click(chrome)
sleep(.3)
position1 = pt.locateOnScreen("smiley.png", confidence=.6)
x = position1[0]
y = position1[1]


# gets message
def get_message():
    global x, y

    position = pt.locateOnScreen("smiley.png", confidence=.7)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y)
    pt.moveTo(x + 99, y - 48)
    pt.tripleClick()
    pt.rightClick()
    cpy_button = pt.locateOnScreen("copy.png", confidence=.6)
    sleep(.2)
    pt.moveTo(cpy_button, duration=.1)
    sleep(.2)
    pt.click()
    #
    whatsapp_message = pyperclip.paste()


    print("Message received: " + whatsapp_message)

    return whatsapp_message


# posts
def post_response(message):
    global x, y
    position = pt.locateOnScreen("smiley.png", confidence=.7)
    x = position[0]
    y = position[1]
    pt.moveTo(x + 200, y + 20)
    pt.click()
    pt.typewrite(message)
    pt.typewrite("\n")
    pt.typewrite("nice")


def process_response(message):

    if "?" in str(message).lower():
        question_list_of_answer = ["Don't ask me any questions", "i don't know", "mujhe nahi pata", "main thodi der main bataonga", "abhi thodi der rooku bata rha hu", "wait for a while i will tell you soon!!", 'abhi thoda rukiye main aapko thodi der main batata hoon??', "ok wait my master aditya will tell you soon?"]
        return random.choice(question_list_of_answer)
    elif "👌" in str(message).lower():
        return "👌👌👌 nice!!"


# Check for new messages
def check_for_new_message():
    # greendot = pt.locateOnScreen("greendot.png", confidence=.6)
    # gx = greendot[0]
    # gy = greendot[1]
    # pt.click(gx-60, gy)

    pt.moveTo(x + 80, y - 40)
    while True:
        try:
            position = pt.locateOnScreen("greendot.png", confidence=.67)
            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100, 0)
                pt.click()
                sleep(.5)


                processed_message = process_response(get_message())
                post_response(processed_message)


                sleep(2)
            else:
                print("no new message till now")
                sleep(5)

        except(Exception):
            print("There are no new message till now!!")



if __name__ == '__main__':
    check_for_new_message()


