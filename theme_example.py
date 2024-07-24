import customtkinter
from CTkCodeBox import *

# Create the main application window
app = customtkinter.CTk()
app.geometry("400x400")
app.title("CodeBox Themes")

# Create a CTkLabel to display a title
title_label = customtkinter.CTkLabel(app, text="CodeBox Examples", font=("Helvetica", 16, "bold"))
title_label.pack()

# Create a CTkCodeBox with an initial theme
codebox = CTkCodeBox(app, language="python", theme="solarized-light")
codebox.pack(padx=10, pady=10, fill="both", expand=True)
demo_code = """def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

count = 0
num = 2
while count < 10:
    if is_prime(num):
        print(num)
        count += 1
    num += 1

"""
codebox.insert("0.0", demo_code)

# Create a CTkComboBox for theme selection
theme_values = ['abap', 'arduino', 'autumn', 'borland',
                'colorful', 'default', 'dracula', 'emacs', 'friendly_grayscale',
                'friendly', 'fruity', 'github-dark', 'gruvbox-dark', 'gruvbox-light',
                'igor', 'inkpot', 'lightbulb', 'lilypond', 'lovelace', 'manni', 'material',
                'monokai', 'murphy', 'native', 'nord-darker', 'nord', 'one-dark', 'paraiso-dark',
                'paraiso-light', 'pastie', 'perldoc', 'rainbow_dash', 'rrt', 'sas', 'solarized-dark',
                'solarized-light', 'staroffice', 'stata-dark', 'stata-light', 'tango', 'trac', 'vim', 'vs',
                'xcode', 'zenburn']
             
def update_theme(e):
    codebox.configure(theme=e)
    
theme_combobox = customtkinter.CTkComboBox(app, values=theme_values,command=update_theme)
theme_combobox.pack(padx=10, fill="x", expand=True)
theme_combobox.set("solarized-light")

def switch_mode():
    if theme_switch.get():
        customtkinter.set_appearance_mode("Dark")
    else:
        customtkinter.set_appearance_mode("Light")
        
theme_switch = customtkinter.CTkSwitch(app, text="Dark Mode", command=switch_mode)
theme_switch.pack(pady=10, expand=True)
theme_switch.toggle()

app.mainloop()
