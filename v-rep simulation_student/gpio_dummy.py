import numpy as np

gpio_pin = np.arange(1,41, dtype='uint8')
gpio_pin_state = np.zeros((40))
gpio_pin = np.column_stack((gpio_pin,gpio_pin_state))
gpio_pin_setting = np.zeros(40, dtype='uint8')

class GPIO:
    def __init__(self):
        self.enable = 0
        self.LOW = 0
        self.HIGH = 1
        self.OUT = 'out'
        self.IN = 'in'
        self.BOARD = "GPIO as board"     
    
    def setmode(self, mode):
        if mode != "GPIO as board":
            raise "Please set GPIO as Board"
        else:
            self.enable = 1
    
    def setup(self,pin,setting):
        if setting == 'in':
            mode = 2
        elif setting == 'out':
            mode = 1
        else:
            raise "select IN or OUT"

        gpio_pin_setting[pin-1] = mode
        return 0
           
    def output(self, pin, value):
        if not self.enable:
            raise "Please set GPIO as Board or BCM"
        if not gpio_pin_setting[pin-1] == 1:
            raise "Please set the pin output"
            
        gpio_pin[pin-1][1] = bool(value)
        f = open("./datafile/control.txt", 'w')
        for p, v  in gpio_pin:
            f.write(str(int(p))+' '+str(v)+'\n')            
        f.close()
            
    def input(self, pin):
        if not gpio_pin_setting[pin-1] == 2:
            raise "Please set the pin input"
        f=open("./datafile/control_read.txt", 'r')
        line = f.readlines()
        try:
            value = float(line[pin-1].strip('\n'))
        except:
            value = 0
        return value
        
    def cleanup(self):
        f = open("./datafile/control.txt", 'w')
        for p, v  in gpio_pin:
            f.write(str(int(p))+' '+'0'+'\n')            
        f.close()              
    
    class pin:
        def __init__(self, name):
            self.name = name
    
    class PWM:
        def __init__(self, pin, cycle):
            self.pin = pin-1
            self.cycle = cycle
            self.enable = 0
            self.duty = 0
            
        def start(self, duty):
            if not gpio_pin_setting[self.pin] == 1:
                raise "Please set the pin output"
            self.enable = 1
            if duty >= 0 and duty <= 100:
                self.duty = duty
                gpio_pin[self.pin][1] = round(duty*0.01,4)
                f = open("./datafile/control.txt", 'w')
                for p, v in gpio_pin:
                    f.write(str(int(p))+' '+str(v)+'\n')                
                f.close()
            else:
                raise "duty must be 0 ~ 100"
                
        def ChangeDutyCycle(self, duty):
            if self.enable == 1:
                if duty >= 0 and duty <= 100:
                    self.duty = duty
                    gpio_pin[self.pin][1] = round(duty*0.01,4)
                    f = open("./datafile/control.txt", 'w')
                    for p, v in gpio_pin:
                        f.write(str(int(p))+' '+str(v)+'\n')     
                    f.close()
                else:
                    raise "duty must be 0 ~ 100"
            else:
                raise "pin is not started."