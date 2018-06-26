# Add your Python code here. E.g.
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
    return diceImages[random.randint(0,len(diceImages))]

while True:
    gesture = accelerometer.current_gesture()
    if gesture == "shake":
        #pick random number from 1 to 6
        randomRoll = random.randint(0, len(diceImages))
        display.show(randomRoll)
        display.show(diceImages[randomRoll])
        # microbit.sleep(1000)
        

display.show(getRandomImage())
