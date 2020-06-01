import tkinter as tk
root = tk.Tk()

label = tk.Label(root,text="I am a label widget")
button = tk.Button(root,text="I am a button")

label.pack()
button.pack()
root.mainloop()