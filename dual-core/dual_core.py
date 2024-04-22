from machine import PWM, SPI #, I2C, PWM, SPI
import time
import os
import gc
import _thread
gc.enable()

sLock = _thread.allocate_lock()

def lprint(file,text):
    #global slock
    #sLock.acquire()
    t = time.localtime()
    logwrite = ("{} {} {},{:02d}:{:02d}.{:02d},{}\r\n".format(t[0], t[1], t[2],t[3], t[4], t[5], text))
    with open("test%s.csv"%(file), "a") as f:
        f.write(logwrite)
    #sLock.release()

#test1
lprint('Core0','create a file')
lprint('Core0','add text')

print('works as expected')
time.sleep(1)
lprint('Core0','some more')
lprint('Core0','Done')

print('Done file Core 0')
time.sleep(1)
_thread.start_new_thread(lprint, ['Core1','create a file'])
time.sleep(1)
_thread.start_new_thread(lprint, ['Core1','add text'])

print('Works')
time.sleep(1)
_thread.start_new_thread(lprint, ['Core1','some more'])
time.sleep(1)
_thread.start_new_thread(lprint, ['Core1','Done'])

print('Done file Core 1')
time.sleep(1)