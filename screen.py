from tkinter import *
from time import strftime

class FullScreenApp(object):

    def __init__(self, master, **kwargs):
        self.master = master
        self._geom = '200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth(), master.winfo_screenheight()))
        master.bind('<Escape>', self.toggle_geom)
        master.bind('q', self.quit)
        master.overrideredirect(1)

    def toggle_geom(self, event):
        geom = self.master.winfo_geometry()
        print("toggle resize")
        self.master.geometry(self._geom)
        self._geom = geom

    def quit(self, event):
        print("exit")
        sys.exit()

root = Tk()
app = FullScreenApp(root)

root.title("my app")

root.config(bg="brown4")

root.w = Label(root, text='hello world ! ' + strftime('%H:%M:%S'), fg="black", font=("Helvetica", 40), bg="red")
root.w.pack()

root.mainloop()
