from picamera import PiCamera, Color
from time import sleep

camera = PiCamera()
camera.resolution = (1280, 720)
camera.framerate = 15
camera.start_preview(alpha=200)

#for i in range(100):
#    camera.annotate_text = "Brightness: %s" % i
#    camera.brightness = i
#    sleep(0.1)
#    
#camera.brightness = 50

#for i in range(100):
#    camera.annotate_text = "Contrast: %s" % i
#    camera.contrast = i
#    sleep(0.1)

#camera.contrast = 50

for effect in camera.IMAGE_EFFECTS:
    camera.image_effect = effect
    camera.annotate_text = "Effect: %s" % effect
    sleep(5)

#for awb_mode in camera.AWB_MODES:
#    camera.awb_mode = awb_mode
#    camera.annotate_text = "awb_mode: %s" % awb_mode
#    sleep(5)


#camera.annotate_background = Color('blue')
#camera.annotate_foreground = Color('yellow')
#camera.annotate_text_size = 50
#camera.annotate_text = "Hello world!"
#camera.exposure_mode = 'sports'
#camera.image_effect = 'oilpaint'
sleep(5)
camera.capture('/home/pi/Desktop/small.jpg')
#for i in range(5):
#    sleep(5)
#    camera.capture('/home/pi/Desktop/image%s.jpg' % i)
camera.stop_preview()