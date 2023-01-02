import threading
import subprocess
import TermTk as ttk
import time

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
    global stop
    stop = False
    while stop == False:
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
    global stop
    stop =  False
    while stop == False:
        if readgpio(gpioin) == 1:
            if readgpio(gpioout) == 0:
                while(readgpio(gpioin) == 1):
                    writegpio(gpioout, 1)
                    writegpio(gpioout, 1)
            else:
                while(readgpio(gpioin) == 1):
                    writegpio(gpioout, 0)
                    writegpio(gpioout, 0)

def setl(value):
    resLabel.setText("leds")
    thr1 = threading.Thread(target = workled, args = (value,))
    thr1.start()


def setg(gpin, out):
    resLabel.setText("gpio")
    thr2 = threading.Thread(target = workgpio, args = (gpin, out))
    thr2.start()

def stopthr():
    stop = True

def testled(num):
    t1 = time.time()
    initleds()
    while num > 0:
        if readled(0) == 0:
                writeled(0, 1)
        if readled(0) == 1:
                writeled(0, 0)
        num = num - 1
    t2 = time.time()
    result.setText(str(t2 - t1))

def runtestled(num):
    thr3 = threading.Thread(target = testled, args = (num,))
    thr3.start()


if __name__ == '__main__':
    root = ttk.TTk()
    initgpioTK = ttk.TTkWindow(parent=root, pos=(50,5), size=(50,30), title="Мигание и кнопочка", ayout=ttk.TTkVBoxLayout())

    resLabel = ttk.TTkLabel(text="Выбери режим", maxHeight=5, pos=(0,0))
    initgpioTK.addWidget(resLabel)
    btn0 = ttk.TTkButton(border=True, text="leds", pos=(1,1))
    btn1 = ttk.TTkButton(border=True, text="gpio", pos=(20,1))
    btn2 = ttk.TTkButton(border=True, text="stop", pos=(40,1))
    initgpioTK.addWidget(btn0)
    initgpioTK.addWidget(btn1)
    initgpioTK.addWidget(btn2)

    btn0.clicked.connect(lambda : setl(10))
    btn1.clicked.connect(lambda : setg(10, 13))
    btn2.clicked.connect(lambda : stopthr())

    btnShow = ttk.TTkButton(parent=root, text="Show мигание", pos=(0,0), size=(20,3), border=True)
    btnHide = ttk.TTkButton(parent=root, text="Hide мигание", pos=(0,3), size=(20,3), border=True)

    btnShow.clicked.connect(initgpioTK.show)
    btnHide.clicked.connect(initgpioTK.hide)

    test = ttk.TTkWindow(parent=root, pos=(100,5), size=(50,30), title="Test", ayout=ttk.TTkVBoxLayout())
    result = ttk.TTkLabel(text="Выбери", maxHeight=5, pos=(0,0))
    test.addWidget(result)

    btnShow = ttk.TTkButton(parent=root, text="Show test", pos=(0,6), size=(20,3), border=True)
    btnHide = ttk.TTkButton(parent=root, text="Hide test", pos=(0,9), size=(20,3), border=True)

    btnShow.clicked.connect(test.show)
    btnHide.clicked.connect(test.hide)

    btn3 = ttk.TTkButton(border=True, text="test", pos=(1,1))
    test.addWidget(btn3)
    btn3.clicked.connect(lambda : runtestled(1000))





    


    root.mainloop()
