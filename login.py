# -*- coding:utf-8 -*-
'''
Created on 2016/2/1

@author: songlin.ji
'''

from Tkinter import StringVar
import json
import os
import sys
import tkMessageBox
import ttk

import Tkinter as tk
from flash_station import FOLDER_CONFIG
from flash_station import FOLDER_IMAGES
from flash_station import THEME_COLOR


class LoginFrame(tk.Frame):
    
    def __init__(self, master=None, logout=None):
        tk.Frame.__init__(self, master=master, bg=THEME_COLOR)
        
        self._login_success = logout
        
        '''Layout'''
        self.__create_logo()
        self.__create_lable()
        self.__create_entry()
        self.__create_button()
        self.__config_layout()
        
        '''load the data of accounts'''
        self.__load_accounts()
    
    def __create_logo(self):
        self._photo = tk.PhotoImage(file=os.path.join(sys.path[0], FOLDER_IMAGES, 'acading-logo.gif'))
        ttk.Label(self, image=self._photo, background=THEME_COLOR)\
        .grid(row=0, column=1, pady=10)
        
        ttk.Label(self, text='Flash Station', style='Title.TLabel').grid(row=1, column=1, pady=10)
    
    def __create_lable(self):
        
        _cnf = {'font':("Helvetica", "16", "bold"), 'bg':THEME_COLOR, 'fg':"#ffc20e"}
        
        tk.Label(self, cnf=_cnf, text='User Name:')\
        .grid(row=2, column=0, pady=20, sticky=tk.E)  
              
        tk.Label(self, cnf=_cnf, text='Password:')\
        .grid(row=3, column=0, pady=20, sticky=tk.E)
        
    def __create_entry(self):
        _cnf = {'font':("Helvetica", "16", "bold"), 'width':20}
        
        self._user_name = StringVar()
        tk.Entry(self, cnf=_cnf , textvariable=self._user_name)\
        .grid(row=2, column=1, ipady=4, sticky=tk.W)
        
        self._password = StringVar()
        tk.Entry(self, cnf=_cnf, textvariable=self._password, show='*')\
        .grid(row=3, column=1, ipady=4, sticky=tk.W)
        
    def __login_click(self):
        _name = self._user_name.get()
        
        if not _name:
            tkMessageBox.showwarning("Warning", "The user name cannot be empty!")
            return
        
        _password = self._password.get()
        
        if not _password:
            tkMessageBox.showwarning("Warning", "The password cannot be empty!")
            return            
        
        global APP_CONFIG
        
        for item in self._accounts:
            if item['name'] == _name and item['password'] == _password:
                
                if self._login_success:
                    self._login_success()
                else:                    
                    tkMessageBox.showinfo("Tip", "Validation succeeded!")
                return
            
        tkMessageBox.showwarning("Warning", "User name and password do not match!") 
        
    def __create_button(self):
        _cnf = {'font':('Helvetica', 18, 'bold'), 'activebackground':'#7CCD7C', 'fg':'white', 'bg':'#7CCD7C'}
        tk.Button(self, cnf=_cnf , text=' Login ', height=3, width=6, command=self.__login_click)\
        .grid(row=2, column=2, rowspan=2, padx=20, sticky=tk.W)
    
    def __config_layout(self):
        self.rowconfigure(1, weight=2)
        self.rowconfigure(4, weight=3)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(2, weight=1)

    def __load_accounts(self):
        try:
            configFile = open(os.path.join(sys.path[0], FOLDER_CONFIG, 'account.json'), 'r')
            self._accounts = json.loads(configFile.read())['account']
        finally:
            configFile.close()

    def clear(self):
        self._user_name.set('')
        self._password.set('')
