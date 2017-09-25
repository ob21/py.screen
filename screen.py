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

root.update()

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

print(str(width) + "x" + str(height))

half_width = width/2
half_height = height/2

print(str(half_width) + "x" + str(half_height))

frame1 = Frame(root, width=half_width, height=half_height, bg="red")
frame1.grid(row=0, column=0)

hour = Label(frame1, text=strftime('%H h %M'), fg="white", font=("Arial bold", 200), bg="black")
hour.grid(row=0, column=0)

frame2 = Frame(root, width=half_width, height=half_height, bg="blue")
frame2.grid(row=0, column=1)

# meteo = Label(frame2, text="meteo", fg="white", font=("Arial bold", 200), bg="black")
# meteo.grid(row=0, column=1)

frame3 = Frame(root, width=half_width, height=half_height, bg="green")
frame3.grid(row=1, column=0)

jour = Label(frame3, text="jour", fg="white", font=("Arial bold", 50), bg="black")
jour.grid(row=1, column=0)

def update():
    hour.config(text=strftime('%H:%M'), fg="white", font=("Arial bold", 300), bg="black")
    root.after(1000, update)

update()

root.mainloop()
