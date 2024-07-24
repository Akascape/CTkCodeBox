import customtkinter
import tkinter

class TextMenu(tkinter.Menu):
    """
    Popup Text Menu for CTkTextbox and CTkEntry
    Author: Akash Bora
    """
    def __init__(self,
                 widget,
                 fg_color=None,
                 text_color=None,
                 hover_color=None,
                 **kwargs):

        super().__init__(tearoff=False, title="menu", borderwidth=0, bd=0, relief="flat", **kwargs)
        
        self.fg_color = customtkinter.ThemeManager.theme["CTkFrame"]["top_fg_color"] if fg_color is None else fg_color
        self.text_color = customtkinter.ThemeManager.theme["CTkLabel"]["text_color"] if text_color is None else text_color
        self.hover_color =  customtkinter.ThemeManager.theme["CTkButton"]["hover_color"] if hover_color is None else hover_color
        
        self.widget = widget
        
        self.add_command(label="Cut", command=self.cut_text)
        self.add_command(label="Copy", command=self.copy_text)
        self.add_command(label="Paste", command=self.paste_text)
        self.add_command(label="Delete", command=self.clear_text)
        self.add_command(label="Clear All", command=self.clear_all_text)
        self.add_command(label="Select All", command=self.select_all_text)
        
        self.add_command(label="Undo", command=self.undo_text)
        
        self.widget.bind("<Button-3>", lambda event: self.do_popup(event))
        self.widget.bind("<Button-2>", lambda event: self.do_popup(event))
        
    def do_popup(self, event):
        """ open the popup menu """
        
        super().config(bg=self.widget._apply_appearance_mode(self.fg_color),
                       fg=self.widget._apply_appearance_mode(self.text_color),
                       activebackground=self.widget._apply_appearance_mode(self.hover_color))
        self.tk_popup(event.x_root, event.y_root) 
                
    def cut_text(self):
        """ cut text operation """
        self.copy_text()
        try: self.widget.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)
        except: pass
        
    def copy_text(self):
        """ copy text operation """                                                                                                                  
        try:
            self.clipboard_clear()
            self.clipboard_append(self.widget.get(tkinter.SEL_FIRST, tkinter.SEL_LAST))
        except: pass
        
    def paste_text(self):
        """ paste text operation """
        try: self.widget.insert(self.widget.index('insert'), self.clipboard_get())
        except: pass

    def clear_all_text(self):
        """ clears sll the text """
        try:
            self.widget.delete(0.0,"end")
        except: pass

    def select_all_text(self):
        """ clears sll the text """
        try:
            self.widget.tag_add("sel", "0.0", "end")
        except: pass
        
    def clear_text(self):
        """ clears sll the text """
        try: self.widget.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)
        except: pass

    def undo_text(self):
        try:
            self.widget.edit_undo()
            self.widget.event_generate("<<ContentChanged>>")
        except: pass
        
