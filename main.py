import rfid
from machine import I2C, Pin
from pico_i2c_lcd import I2cLcd
from time import sleep

I2C_ADDR     = 39
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

sda = Pin(8, Pin.PULL_UP)

scl = Pin(9, Pin.PULL_UP)

i2c = I2C(0, sda=sda, scl=scl, freq=400000)
print(i2c.scan())
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

lcd.move_to(0,0)
lcd.putstr("RFID Card Reader")
lcd.move_to(0,1)
lcd.putstr("By: TheLowSpecPC")
sleep(2)
lcd.clear()

add = Pin(6, Pin.IN, Pin.PULL_DOWN)
sub = Pin(7, Pin.IN, Pin.PULL_DOWN)
bal = Pin(5, Pin.IN, Pin.PULL_DOWN)

num0 = Pin(10, Pin.IN, Pin.PULL_DOWN)
num1 = Pin(11, Pin.IN, Pin.PULL_DOWN)
num2 = Pin(12, Pin.IN, Pin.PULL_DOWN)
num3 = Pin(13, Pin.IN, Pin.PULL_DOWN)
num4 = Pin(14, Pin.IN, Pin.PULL_DOWN)
num5 = Pin(15, Pin.IN, Pin.PULL_DOWN)
num6 = Pin(16, Pin.IN, Pin.PULL_DOWN)
num7 = Pin(17, Pin.IN, Pin.PULL_DOWN)
num8 = Pin(18, Pin.IN, Pin.PULL_DOWN)
num9 = Pin(19, Pin.IN, Pin.PULL_DOWN)

back = Pin(20, Pin.IN, Pin.PULL_DOWN)
enter = Pin(21, Pin.IN, Pin.PULL_DOWN)

def NumPad():
    value = ""
    while True:
        sleep(0.2)
        if num0.value()==1:
            value = value + "0"
            lcd.clear()
            lcd.putstr(value)
            
        elif num1.value()==1:
            value = value + "1"
            lcd.clear()
            lcd.putstr(value)
            
        elif num2.value()==1:
            value = value + "2"
            lcd.clear()
            lcd.putstr(value)
            
        elif num3.value()==1:
            value = value + "3"
            lcd.clear()
            lcd.putstr(value)
            
        elif num4.value()==1:
            value = value + "4"
            lcd.clear()
            lcd.putstr(value)
            
        elif num5.value()==1:
            value = value + "5"
            lcd.clear()
            lcd.putstr(value)
            
        elif num6.value()==1:
            value = value + "6"
            lcd.clear()
            lcd.putstr(value)
            
        elif num7.value()==1:
            value = value + "7"
            lcd.clear()
            lcd.putstr(value)
            
        elif num8.value()==1:
            value = value + "8"
            lcd.clear()
            lcd.putstr(value)
            
        elif num9.value()==1:
            value = value + "9"
            lcd.clear()
            lcd.putstr(value)
        
        elif back.value()==1:
            value = value[0:len(value)-1]
            lcd.clear()
            lcd.putstr(value)
            
        elif enter.value()==1:
            lcd.clear()
            return value
        
while True:
    if add.value()==1:
        lcd.clear()
        val = int(rfid.run("add", NumPad()))
        lcd.clear()
        lcd.putstr("Value Added")
        sleep(1)
        lcd.clear()
        lcd.putstr("Balance: " + str(val))
            
    elif sub.value()==1:
        lcd.clear()
        val = rfid.run("sub", NumPad())
        if val.isdigit() == True:
            lcd.clear()
            lcd.putstr("Value Subtracted")
            sleep(1)
            lcd.clear()
            lcd.putstr("Balance: " + str(int(val)))
        else:
            lcd.clear()
            lcd.putstr(val)
            
    elif bal.value()==1:
        lcd.clear()
        val = int(rfid.run("bal", "0"))
        lcd.clear()
        lcd.putstr("Balance: " + str(val))
