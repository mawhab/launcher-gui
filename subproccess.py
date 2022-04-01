import subprocess
from tkinter import *
import os
import signal

class gui:
    def __init__(self): # initialize gui
        self.root = Tk()
        self.root.geometry('100x350') # size of window
        self.root.title('Launcher') # title
        self.root.eval('tk::PlaceWindow . center') # align window to center of screen

        # creating buttons
        self.localization = Button(self.root, text='Launch Localization', command=self.launch_localization_cb)
        self.control = Button(self.root, text='Launch control', command=self.launch_control_cb)
        self.calibrate = Button(self.root, text='Calibrate odrive', command=self.calibrate_cb)
        self.idle = Button(self.root, text='Set odrive to idle', command=self.set_idle_cb)
        self.speed = Text(self.root, height=1, width=10)
        self.set_speed = Button(self.root, text='Send speed to odrive', command=self.set_speed_cb)

        # packing buttons
        self.localization.pack()
        self.control.pack()
        self.calibrate.pack()
        self.idle.pack()
        self.speed.pack()
        self.set_speed.pack()
        
    def launch_localization_cb(self): # creates procces that launches localization
        # self.localization_process = subprocess.Popen('roslaunch localization localization.launch', shell=True)
        self.localization_process = subprocess.Popen('python localization.py', shell=True, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
        # for linux: 
        # self.localization_process = subprocess.Popen('python localization.py', shell=True, preexec_fn=os.setsid)
        self.localization.config(text='Stop localization', command=self.stop_localization_cb)

    def stop_localization_cb(self): # stops the localization proccess
        # for linux:
        # os.killpg(os.getpgid(self.localization_process.pid), signal.SIGTERM)
        self.localization_process.send_signal(signal.CTRL_BREAK_EVENT)
        self.localization_process.kill()
        self.localization.config(text='Launch Localization', command=self.launch_localization_cb)

    def launch_control_cb(self): # creates procces that launches control
        # self.control_process = subprocess.Popen('roslaunch control control.launch', shell=True)
        self.control_process = subprocess.Popen('python control.py', shell=True, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
        # for linux: 
        # self.control_process = subprocess.Popen('python control.py', shell=True, preexec_fn=os.setsid)
        self.control.config(text='Stop control', command=self.stop_control_cb)

    def stop_control_cb(self):# stops the control proccess
        # for linux:
        # os.killpg(os.getpgid(self.control_process.pid), signal.SIGTERM)
        self.control_process.send_signal(signal.CTRL_BREAK_EVENT)
        self.control_process.kill()
        self.control.config(text='Launch control', command=self.launch_control_cb)

    def calibrate_cb(self): # runs calibration script
        # subprocess.run('python {PATH}', shell=True)
        subprocess.run('python calibrate.py', shell=True)

    def set_idle_cb(self): # runs idle script
        # subprocess.run('python {PATH}', shell=True)
        subprocess.run('python idle.py', shell=True)

    def set_speed_cb(self): # runs set speed script
        data = int(self.speed.get("1.0", "end-1c"))
        # subprocess.run(f'python (PATH) {data}', shell=True)
        subprocess.run(f'python speed.py {data}', shell=True)

g = gui()

g.root.mainloop()