import Tkinter
import tkMessageBox
import RPi.GPIO as GPIO
import time
from w1thermsensor import W1ThermSensor

top = Tkinter.Tk()

def temp():
   #tkMessageBox.showinfo( "Hello Python", "Hello World")
   sensor = W1ThermSensor()

    while True:  
        temperature = sensor.get_temperature()
        print("The temperature is %s celsius" % temperature)
        time.sleep(2)
        
def colorsen():
    s2 = 23
    s3 = 24
    signal = 25
    NUM_CYCLES = 10


    def setup():
      GPIO.setmode(GPIO.BCM)
      GPIO.setup(signal,GPIO.IN, pull_up_down=GPIO.PUD_UP)
      GPIO.setup(s2,GPIO.OUT)
      GPIO.setup(s3,GPIO.OUT)
      print("\n")
  

    def loop():
      temp = 1
      while(1):  

        GPIO.output(s2,GPIO.LOW)
        GPIO.output(s3,GPIO.LOW)
        time.sleep(0.3)
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
          GPIO.wait_for_edge(signal, GPIO.FALLING)
        duration = time.time() - start 
        red  = NUM_CYCLES / duration   
   
        GPIO.output(s2,GPIO.LOW)
        GPIO.output(s3,GPIO.HIGH)
        time.sleep(0.3)
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
          GPIO.wait_for_edge(signal, GPIO.FALLING)
        duration = time.time() - start
        blue = NUM_CYCLES / duration
    

        GPIO.output(s2,GPIO.HIGH)
        GPIO.output(s3,GPIO.HIGH)
        time.sleep(0.3)
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
          GPIO.wait_for_edge(signal, GPIO.FALLING)
        duration = time.time() - start
        green = NUM_CYCLES / duration

        rednew=((red-2)/(500000-2))*(256)
        greennew=((green-2)/(500000-2))*(256)
        bluenew=((blue-2)/(500000-2))*(256)
                
        print("Red:",rednew);
        print("Green:",greennew);
        print("Blue:",bluenew);

    def endprogram():
        GPIO.cleanup()

    if __name__=='__main__':
    
        setup()

        try:
            loop()

        except KeyboardInterrupt:
            endprogram()
        
def moisturesen():
    channel = 17
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel, GPIO.IN)
 
    def callback(channel):
            if GPIO.input(channel):
                print "Water Detected"
            else:
                print "Water not Detected"
 
    GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
    GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change
 
    # infinite loop
    while True:
        time.sleep(1)


B1 = Tkinter.Button(top, text ="Temp", command = temp)

B2 = Tkinter.Button(top, text ="Color", command = colorsen)

B3 = Tkinter.Button(top, text ="Moisture", command = moisturesen)
B1.pack()
B2.pack()
B3.pack()

top.mainloop()

