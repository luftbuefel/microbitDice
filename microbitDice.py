import random
from microbit import *
image1 = Image("00000:"
               "00000:"
               "00900:"
               "00000:"
               "00000")
image2 = Image("00000:"
               "00900:"
               "00000:"
               "00900:"
               "00000")
image3 = Image("90000:"
               "00000:"
               "00900:"
               "00000:"
               "00009")
image4 = Image("00000:"
               "09090:"
               "00000:"
               "09090:"
               "00000")
               
image5 = Image("90009:"
               "00000:"
               "00900:"
               "00000:"
               "90009")
               
image6 = Image("09090:"
               "00000:"
               "09090:"
               "00000:"
               "09090")
                    
diceImages = [image1, image2, image3, image4, image5, image6]


def getRandomImage():
    #pick random number from 0 to 5
    randomRoll = random.randint(0, len(diceImages)-1)
    return diceImages[randomRoll]
    
#show an image when you start the program
display.show(getRandomImage())

# rolling = False
while True:
    gesture = accelerometer.current_gesture()
    if gesture == "shake":# and rolling ==False:
        # rolling = True
        # for i in range(10):
        display.show(getRandomImage())
        #sleep controls the speed of the rolling dice animation
        sleep(100)
        # rolling = False
