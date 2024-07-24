"""
CTkCodeBox
Author: Akash Bora
License: MIT
"""

import customtkinter
from .text_menu import TextMenu
from tklinenums import TkLineNumbers
from pygments import lex
from pygments.lexers import python, javascript, c_cpp, dotnet, html, css, data, go, jvm, php, ruby, rust, scripting, perl, objective, jsx
from pygments.styles import get_style_by_name, get_all_styles

class AddLineNums(TkLineNumbers):
    """
    Class for adding line numbers in CTkTextbox using TkLineNumbers
    """
    def __init__(self,
                 master,
                 text_color=None,
                 justify="left",
                 padx=30,
                 **kwargs):

        self.master = master
        self.text_color = self.master.cget("border_color") if text_color is None else text_color
        self.fg_color = self.master.cget("fg_color")
        
        customtkinter.windows.widgets.appearance_mode.CTkAppearanceModeBaseClass.__init__(self)
        
        super().__init__(self.master, self.master, justify=justify,
                         colors=(self.master._apply_appearance_mode(self.text_color),
                                 self.master._apply_appearance_mode(self.fg_color)),
                         relief="flat", height=self.master.winfo_reqheight(), **kwargs)
        
        padding = self.master.cget("border_width") + self.master.cget("corner_radius")

        super().grid(row=0, column=0, sticky="nsw", padx=(padding,0), pady=padding-1)
            
        self.master._textbox.grid_configure(padx=(padx, 0))
        self.master._textbox.lift()
        self.master._textbox.configure(yscrollcommand=self.set_scrollbar)
        self.master._textbox.bind("<<ContentChanged>>", self.redraw, add=True)
        self.master.bind("<Key>", lambda e: self.after(10, self.redraw), add=True)

    def set_scrollbar(self, x,y):
        self.redraw(x,y)
        self.master._y_scrollbar.set(x,y)

    def _set_appearance_mode(self, mode_string):
        self.colors = (self.master._apply_appearance_mode(self.text_color),
                       self.master._apply_appearance_mode(self.fg_color))
        self.set_colors()
        
class CTkCodeBox(customtkinter.CTkTextbox):
    """
    Widget for displaying code in CTk
    """
    def __init__(self,
                 master,
                 language,
                 height=200,
                 theme:str="solarized-light",
                 line_numbering:bool=True,
                 numbering_color:str=None,
                 undo:bool=True,
                 menu:bool=True,
                 menu_fg_color:str=None,
                 menu_text_color:str=None,
                 menu_hover_color:str=None,
                 wrap:bool=True,
                 select_color:str=None,
                 cursor_color:str=None,
                 **kwargs):
        
        super().__init__(master, undo=undo, height=height, **kwargs)
        
        if wrap:
            self.configure(wrap="word")
        if line_numbering:
            AddLineNums(self, text_color=numbering_color)
        if menu:
            TextMenu(self, fg_color=menu_fg_color, text_color=menu_text_color, hover_color=menu_hover_color)

        self.select_color = select_color
        if select_color:
            self._textbox.config(selectbackground=self.select_color)
        self.cursor_color = cursor_color
        
        if self.cursor_color:
            self._textbox.config(insertbackground=self.cursor_color)
            
        self.bind('<KeyRelease>', self.update_code)  # When a key is released, update the code
        self.bind('<<ContentChanged>>', self.update_code)
        self.bind("<Control-a>", lambda e: self.after(200, self._select_all), add=True)
        
        self.theme_name = theme
        self.all_themes = list(get_all_styles())
                
        self.common_langs = {
            "python": python.PythonLexer,
            "c": c_cpp.CLexer,
            "cpp": c_cpp.CppLexer,
            "c++": c_cpp.CppLexer,
            "c#": dotnet.CSharpLexer,
            "html": html.HtmlLexer,
            "javascript": javascript.JavascriptLexer,
            "xml": html.XmlLexer,
            "css": css.CssLexer,
            "json": data.JsonLexer,
            "yaml": data.YamlLexer,
            "go": go.GoLexer,
            "typescript": javascript.TypeScriptLexer,
            "kotlin": jvm.KotlinLexer,
            "php": php.PhpLexer,
            "ruby": ruby.RubyLexer,
            "rust": rust.RustLexer,
            "lua": scripting.LuaLexer,
            "java": jvm.JavaLexer,
            "perl": perl.PerlLexer,
            "swift": objective.SwiftLexer,
            "react": jsx.JsxLexer,
        }
        self.language = language
        self.check_lexer()
        self.configure_tags()
        self.edited = False

    def check_lexer(self):
        if type(self.language) is str:
            if self.language.lower() in self.common_langs:
                self.lexer = self.common_langs[self.language.lower()]
            else:
                raise ValueError("This language is not available, try to pass the pygments lexer instead. \nAvailable lexers: https://pygments.org/docs/lexers")
        else:
            self.lexer = self.language
            
    def configure_tags(self):
        if self.theme_name not in self.all_themes:
            raise ValueError(f"Invalid theme name: {self.theme_name}, \nAvailable themes: {self.all_themes}")
        style = get_style_by_name(self.theme_name)
        for token, values in style:
            foreground = values['color']
            if foreground:
                self.tag_config(str(token), foreground=f'#{foreground}')

    def update_code(self, event=None, edited=True):
        code = self.get('0.0', 'end-1c')
        self.clear_code()
        self.highlight_code(code)
        if edited:
            self.edited = True
            
    def clear_code(self):
        for tag in self.tag_names():
            self.tag_remove(tag, '0.0', 'end')
            
    def _select_all(self):
        self.tag_add("sel", "0.0", "end")
        
    def insert(self, start, end):
        super().insert(start, end)
        self.update_code(edited=False)
        self.edit_reset()
        self.edited = False
        
    def highlight_code(self, code):
        code = code.replace("\n"," ",1)
        try:
            tokens = list(lex(code, self.lexer()))
        except:
            raise ValueError("Not a valid lexer. Available lexers: https://pygments.org/docs/lexers")
        start_line=1
        start_index = 0
        for token in tokens:
            end_line, end_index = self.index(f'{start_line}.{start_index}+{len(token[1])} chars').split('.')
            self.tag_add(str(token[0]), f'{start_line}.{start_index}', f'{end_line}.{end_index}')
            start_line = end_line
            start_index = end_index
            
    def configure(self, param=None, **kwargs):
        if "theme" in kwargs:
            self.theme_name = kwargs.pop("theme")
            self.configure_tags()
        if "language" in kwargs:
            self.language = kwargs.pop("language")
            self.check_lexer()
        if "select_color" in kwargs:
            self.select_color = kwargs.pop("select_color")
            self._textbox.config(selectbackground=self.select_color)
        if "cursor_color" in kwargs:
            self.cursor_color = kwargs.pop("cursor_color")
            self._textbox.config(insertbackground=self.cursor_color)
        super().configure(**kwargs)

    def cget(self, param):
        if param=="theme":
            return self.theme_name
        if param=="language":
            return self.language
        if param=="select_color":
            return self.select_color
        if param=="cursor_color":
            return self.cursor_color
        return super().cget(param)
