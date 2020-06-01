import tkinter as tk
root = tk.Tk()

tk.Label(root,text="Enter your password:").pack()
tk.Button(root,text="Search").pack()

v = tk.IntVar()
tk.Checkbutton(root,text="Remember Me",variable=v).pack()
tk.Entry(root,width=30)

v2 = tk.IntVar()
tk.Radiobutton(root,text="Male",variable=v2, value=1).pack()
tk.Radiobutton(root,text="Female",variable=v2,value=2).pack()

var = tk.IntVar()
tk.OptionMenu(root,var,"Select Country","USA","UK","INDIA","Others").pack()
tk.Scrollbar(root,orient='vertical').pack()

root.mainloop()