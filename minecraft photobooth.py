from mcpi.minecraft import Minecraft
#from picamera import PiCamera
from time import sleep
mc = Minecraft.create()
#camera = PiCamera()

mc.postToChat("Find the photobooth")


while True:
    x, y, z = mc.player.getPos()


    sleep(3)

    if x >= -49 and x < -47 and y >= 21.5 and y < 22.5 and z >= 75.0 and z < 76:
        mc.postToChat("You are in the photobooth")
        sleep(1)
        mc.postToChat("Smile!")
        sleep(1)
        #camera.start_preview()
        #sleep(2)
       # camera.rotation = 180
        #camera.capture("/home/pi/Desktop/pi club/Minecraft photobooth/selfie")
        #camera.stop_preview()
       
sleep(3)
 

                                                                                                                                                                                                                                                        
