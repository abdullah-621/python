import tkinter as tk
from time import strftime

# Window তৈরি
root = tk.Tk()
root.title("Digital Clock")

# Clock update করার function
def time():
    string = strftime('%H:%M:%S %p')  # ঘন্টা:মিনিট:সেকেন্ড AM/PM
    label.config(text=string)
    label.after(1000, time)  # প্রতি 1000ms (1 সেকেন্ড) পরে update করবে

# Label তৈরি
label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='cyan')
label.pack(anchor='center')

time()  # Clock start
root.mainloop()
