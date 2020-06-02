#Basic gui w/label & button

import tkinter as tk
root = tk.Tk()

label = tk.Label(root)
label["text"]="I am a label widget"		#using keys
button = tk.Button(root)
button.configure(text="I am a button")	#using configure

label.pack()							#add label to gui
button.pack()							#add button to gui
root.mainloop()