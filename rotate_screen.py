import rotatescreen
import time
rotate = rotatescreen.get_primary_display()
for i in range(13):
    time.sleep(2)
    rotate.rotate_to(i*90 % 360)
