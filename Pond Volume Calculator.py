from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value_one = float(sa_one.get())
        value_two = float(sa_two.get())
        value_three = float(h.get())
        volume.set('{:.2f} CF'.format((value_three/3)*(value_one + value_two + (value_one*value_two)**0.5)))
    except ValueError:
        pass
    
### Main Window - root
    
root = Tk()
root.title("Pond Volume Calculator") #Based on AutoCAD 3CD Conic approximation
root.geometry('300x250')

### Pond Volume Frame

mainframe = ttk.Frame(root, padding="3 3 12 12", borderwidth = 5, relief = 'ridge')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

sa_one = StringVar()
sa_two = StringVar()
h = StringVar()
volume = StringVar()

saone_entry = ttk.Entry(mainframe, width=7, textvariable=sa_one)
saone_entry.grid(column=2, row=1, sticky=(W, E, N, S))

satwo_entry = ttk.Entry(mainframe, width=7, textvariable=sa_two)
satwo_entry.grid(column=2, row=2, sticky=(W, E, N, S))

height_entry = ttk.Entry(mainframe, width=7, textvariable=h)
height_entry.grid(column=2, row=3, sticky=(W, E, N, S))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=4, sticky=W)
ttk.Label(mainframe, textvariable=volume).grid(column=2, row=4, sticky=W)

ttk.Label(mainframe, text="Surface Area One").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="Surface Area Two").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="Height").grid(column=3, row=3, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

saone_entry.focus()
root.bind('<Return>', calculate)

### Second Frame

secondframe = ttk.Frame(root, padding="3 3 12 12", borderwidth = 5, relief = 'ridge', bg = 'red')
secondframe.grid(column=1, row=0, sticky=(N, W, E, S))
root.columnconfigure(1, weight=1)

ttk.Label(secondframe, text = 'HERE',).grid(column=0, row = 0, sticky=E)


root.mainloop()
