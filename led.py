from gpiozero import LED
from time import sleep

# Initialise the LED @ Pin 14
led=LED(14)

# Infinte loop
# Turn the LED ON and OFF with a 1 second delay
while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
    
