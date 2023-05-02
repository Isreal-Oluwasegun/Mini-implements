from  tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog


class Text_Editor():
    def __init__(self, window):
        self.window = window
        self.window.title("TEXT EDITOR")
        self.window.geometry("1200x1200")
        self.window.protocol("WM_DELETE_WINDOW", self.close_app)
        self.filename = None
        self.title = StringVar()
        self.status = StringVar()
        
        self.title_bar = Label(
            self.window, 
            textvariable=self.title,
            font=("Arial","10","bold"), 
            bd=1, 
            relief='ridge'
            )
        
        self.title_bar.pack(side="top", fill="both")
        self.settitle()
        
        self.status_bar = Label(
            self.window, 
            textvariable=self.status, 
            font=("Arial","10","bold"), 
            bd=1, 
            relief='ridge'
            )
        
        self.status_bar.pack(side="bottom", fill="both")
        self.status.set("Welcome to text editor")
        
        self.main_menu = Menu(
            self.window, 
            tearoff=0, 
            font=("Arial","10","bold"), 
            activeforeground="grey"
            )
        
        self.window.config(menu=self.main_menu)
        
        self.main_menu_file = Menu(
            self.main_menu,
            tearoff=0,
            activeforeground="grey",
            font=("Arial","10","bold")
            )
        
        self.main_menu.add_cascade(
            label="File",
            menu=self.main_menu_file
            )
        
        self.main_menu_file.add_command(
            label="New",
            accelerator="Ctrl N",
            command=self.new_file
            )
        
        self.main_menu_file.add_command(
            label="Open",
            accelerator="Ctrl O",
            command=self.open_file
            )
        
        self.main_menu_file.add_command(
            label="Save",
            accelerator="Ctrl S",
            command=self.save
            )
        
        self.main_menu_file.add_command(
            label="Save As",
            accelerator="Ctrl A",
            command=self.save_as
            )
        
        self.main_menu_file.add_command(
            label="Exit",
            accelerator="Ctrl Q",
            command=self.close_app
            )
        

        self.main_menu_edit = Menu(
            self.main_menu, tearoff=0,
            activeforeground="grey",
            font=("Arial","10","bold")
            )
        
        self.main_menu.add_cascade(
            label="Edit",
            menu=self.main_menu_edit
            )
        
        self.main_menu_edit.add_command(
            label="Copy",
            accelerator="Ctrl C",
            command=self.copy
            )
        
        self.main_menu_edit.add_command(
            label="Paste",
            accelerator="Ctrl V",
            command=self.paste
            )
        
        self.main_menu_edit.add_command(
            label="Cut",
            accelerator="Ctrl X",
            command=self.cut
            )
           
        #self.main_menu_edit.add_command(
        #   label="Undo",
        #   accelerator="Ctrl Z",
        #   command=self.undo
         #   )
    
        #self.main_menu_edit.add_command(
        #   label="Undo",
        #   accelerator="Ctrl Z",
        #   command=self.redo
        #    )
        #self.main_menu_help = Menu(
        #    self.main_menu,
        #   tearoff=0,
        #   activeforeground="grey",
        #   font=("Times","15","bold")
        #   )
        
        #self.main_menu.add_command(
         #   label="About",
        #    menu=self.main_menu_help
        #    )
        
        self.main_menu_format = Menu(self.main_menu, tearoff=0)
        self.main_menu.add_cascade(label="Format", menu=self.main_menu_format)
        self.main_menu_format.add_command(label="Font")
        
        self.yscroll = Scrollbar(self.main_menu, orient="vertical")
        
        self.textarea = Text(self.window, yscrollcommand=self.yscroll, font=("Arial","10","bold"))
        self.textarea.focus_get() 
        
        self.yscroll.config(command=self.textarea.yview)
        self.yscroll.pack(side="right", fill="both")
        self.textarea.pack(fill="both", expand=1)
             
        self.shortcut()
        
        
    def settitle(self):
        if self.filename:
            self.title.set(self.filename)
        else:
            self.title.set("Untitle")
                
        
    def new_file(self, *args):
        self.textarea.delete("1.0", "end")
        self.filename = None 
        self.settitle()
            
        self.status.set("New file created")
            
    def open_file(self, *args):
        try:
            
            filetype = (
                ("Text files", "*.txt"),
                ("Pyton files", "*.py"),
                ("All files", "*.*")
                )
            self.filename = filedialog.askopenfilename(
                title="Open file",
                initialdir="/",
                filetypes=filetype
                )
            if self.filename:
                with open(self.filename, "r") as inline:
                    self.textarea.delete("1.0","end")
                    for line in inline:
                        self.textarea.insert("end", line)
                self.settitle()
                self.status.set("Open successfully")
        except Exception as e:
            self.textarea.delete("1.0","end-1c")   
            messagebox.showinfo("Exception", e)
                    
                
    def save(self, *args):
        if self.filename is None:
            self.save_as()      
        else:
            text = self.textarea.get("1.0", "end-1c")
            with open(self.filename, 'w') as file:
                file.write(text)
            self.settitle()
            self.status.set("Saved successfully")

    def save_as(self, *args):
        filetypes = (
            ("Text File", "*.txt"),
            ("Python File", ".py"),
            ("All File", "*.*")
        )
        self.filename = filedialog.asksaveasfilename(
            defaultextension = ".txt",
            filetypes = filetypes
        )
        text = self.textarea.get("1.0", "end-1c")
        with open(self.filename, 'w') as file:
            file.write(text)
        self.settitle()
        self.status.set("Saved successfully")  
        
        
    def close_app(self, *args):
        response = messagebox.askokcancel("Exit?","Do you really want to exit?")
        if response:
            self.window.destroy()    
            
    def copy(self, *args):
        self.textarea.event_generate("<<Copy>>")
        
    def paste(self, *args):
        self.textarea.event_generate("<<Paste>>")
        
    def cut(self, *args):
        self.textarea.event_generate("<<Cut>>") 
        
    def shortcut(self):
        self.textarea.bind("<Control-n>",self.new_file)
        self.textarea.bind("<Control-N>",self.new_file)
        self.textarea.bind("<Control-o>",self.open_file)
        self.textarea.bind("<Control-O>",self.open_file)
        self.textarea.bind("<Control-s>",self.save)
        self.textarea.bind("<Control-S>",self.save)
        self.textarea.bind("<Control-q>",self.close_app)
        self.textarea.bind("<Control-Q>",self.close_app)
        self.textarea.bind("<Control-c>",self.copy)
        self.textarea.bind("<Control-v>",self.paste)
        

        
window = Tk()
Text_Editor(window)

window.mainloop()
                
                
                
            
            
    
    
        