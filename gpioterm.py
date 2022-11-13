import subprocess
import TermTk as ttk

def initleds():
    subprocess.run(f'echo "none" > /sys/class/leds/orangepi:green:pwr/trigger', shell=True)
    subprocess.run(f'echo "none" > /sys/class/leds/orangepi:red:status/trigger', shell=True)

def writeled(num, value):
    if num == 0:
        subprocess.run(f'echo "{ value }" > /sys/class/leds/orangepi:green:pwr/brightness', shell=True)
    else:
        subprocess.run(f'echo "{ value }" > /sys/class/leds/orangepi:red:status/brightness', shell=True)

def readled(num):
    if num == 0:
        t = subprocess.run(f'cat /sys/class/leds/orangepi:green:pwr/brightness', shell=True, stdout=subprocess.PIPE)
        return(int(t.stdout.decode('utf-8')))
    else:
        t = subprocess.run(f'cat /sys/class/leds/orangepi:red:status/brightness', shell=True, stdout=subprocess.PIPE)
        return(int(t.stdout.decode('utf-8')))

def initgpio(gpio,type):
    subprocess.run(f'echo "{ gpio }" > /sys/class/gpio/export', shell=True)
    subprocess.run(f'echo "{ type }" > /sys/class/gpio/gpio{ gpio }/direction', shell=True)

def writegpio(gpio, num):
    subprocess.run(f'echo "{ num }" > /sys/class/gpio/gpio{ gpio }/value', shell=True)

def readgpio(gpio):
    t = subprocess.run(f'cat /sys/class/gpio/gpio{ gpio }/value', shell=True, stdout=subprocess.PIPE)
    return(int(float(t.stdout.decode('utf-8'))))

def workled(num):
    initleds()
    initgpio(num, "in")
    i = 1
    while(i==1):
        if readgpio(num) == 1:
            if readled(0) == 0:
                while(readgpio(num) == 1):
                    writeled(0, 1)
                    writeled(1, 1)
            else:
                while(readgpio(num) == 1):
                    writeled(0, 0)
                    writeled(1, 0)

def workgpio(gpioin, gpioout):
    initgpio(gpioin, "in")
    initgpio(gpioout, "out")
    i = 1
    while(i==1):
        if readgpio(gpioin) == 1:
            if readgpio(gpioout) == 0:
                while(readgpio(gpioin) == 1):
                    writegpio(gpioout, 1)
                    writegpio(gpioout, 1)
            else:
                while(readgpio(gpioin) == 1):
                    writegpio(gpioout, 0)
                    writegpio(gpioout, 0)
if __name__ == '__main__':
    workled(7)