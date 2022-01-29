import os
import sys
import tkinter as tk

class Application(tk.Frame):
    
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        
        self.config()
        self.pack(expand=True, anchor=tk.CENTER, fill=tk.BOTH)


main_window = Application()
win_top = main_window.master
win_top.title('USB测试工具')
# win_top.iconbitmap(os.path.join(sys.path[0], FOLDER_IMAGES, 'app.ico'))
win_top.minsize(800, 600)
win_top.update()

current_window_width = win_top.winfo_width()
current_window_height = win_top.winfo_height()    
screen_width, screen_height = win_top.maxsize()
temp = '%dx%d+%d+%d' % (current_window_width, current_window_height, (screen_width - current_window_width) / 2,
                            (screen_height - current_window_height) / 2)     
win_top.geometry(temp)


main_window.mainloop()