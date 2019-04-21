import RPi.GPIO as GPIO
import time



class Path_finder:
    def __init__(self, interpreter):
        self.interpreter = interpreter
        self.line_mode = False  # False = weiße linie auf dunklem hintergrung, True = gegenteil
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(20, GPIO.IN)  # rechts
        GPIO.setup(16, GPIO.IN)  # links

    def change_direction(self, chanel):
        sensor_rechts = 20
        sensor_links = 16
        if chanel == sensor_rechts:
            print("trigger rechts")
            # rechtes Rad stop
            self.interpreter.execute_wheel_command(int('100', 2))
            self.interpreter.execute_wheel_command(int('001', 2))
        if chanel == sensor_links:
            print("trigger links")
            self.interpreter.execute_wheel_command(int('000', 2))
            self.interpreter.execute_wheel_command(int('101', 2))

    def start_automodus(self):
        self.follow_line = True
        if not self.line_mode:
            GPIO.add_event_detect(20, GPIO.RISING, callback=self.change_direction)
            GPIO.add_event_detect(16, GPIO.RISING, callback=self.change_direction)
        else:
            GPIO.add_event_detect(20, GPIO.FALLING, callback=self.change_direction)
            GPIO.add_event_detect(16, GPIO.FALLING, callback=self.change_direction)
        self.interpreter.execute_wheel_command(int('001', 2))
        self.interpreter.execute_wheel_command(int('101', 2))
