import tkinter as tk
root = tk.Tk()
root.geometry("300x200")
radio1=tk.radiobutton(root,text="option 1",value=1)
radio2=tk.radiobutton(root,text="option 2",value=2)
radio1.pack()
radio2.pack()
root.mainloop()
