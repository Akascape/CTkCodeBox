# CTkCodeBox

A code editor widget for customtkinter.
![image](https://github.com/user-attachments/assets/a22c6142-afc8-4239-840f-76e06ef7c668)


## Features
- Multiple language support
- Code syntax highlighting
- Multiple Themes
- Right-click copy-paste menu
- Line numbers on left side
- Fully customizable
- Easy to Use

## Installation
### [<img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/Akascape/CTkCodeBox?&color=white&label=Download%20Source%20Code&logo=Python&logoColor=yellow&style=for-the-badge"  width="400">](https://github.com/Akascape/CTkCodeBox/archive/refs/heads/main.zip)

**Download the source code, paste the `CTkCodeBox` folder in the directory where your program is present.**
## Simple Usage
```python
import customtkinter
from CTkCodeBox import *

customtkinter.set_appearance_mode("light")

root = customtkinter.CTk()

codebox = CTkCodeBox(root, language="python")
codebox.pack(padx=10, pady=10, expand=True,fill="both")

root.mainloop()
```

## Arguments
| Parameter | Description |
|-----------| ------------|
| width |  change the default width of the widget |
| height | change the default height of the widget |
| **fg_color** | change the fg_color of the widget|
| language | set the language lexer for the codebox |
| theme | change the overall color theme for the code syntax |
| line_numbering | boolean, enable or disable the line numbering |
| menu | boolean, enable or disable the right click popup menu |
| menu_fg_color | color of the menu (optional) |
| menu_text_color | text color of the menu buttons (optional) |
| menu_hover_color | hover color of the menu buttons (optional) |
| wrap | enable or disabled word wrapping in the textbox |
| select_color | change the selection color of the codebox |
| cursor_color | change the cursor color I (blinking) |
| undo | boolean, enable or disable the undo text feature |
| _*Other Parameters_ | _All other parameters for ctktextbox can be passed in ctkcodebox_ |

## Methods
- **.insert(index, code)**: insert code in the box 
- **.configure(kwargs)**: change parameters of the codebox
- **.cget(parameter)**: get the parameter name from the codebox
- **.update_code()**: update the code syntax colors
- **.clear_code()**: delete all the code from the box
<br>
  <a href="https://github-readme-tech-stack.vercel.app">
    <img src="https://github-readme-tech-stack.vercel.app/api/cards?title=LANGUAGES&align=left&titleAlign=left&fontSize=20&lineHeight=10&lineCount=2&theme=ayu&width=450&bg=%25230B0E14&titleColor=%231c9eff&line1=lua%2Clua%2Cauto%3Bpython%2Cpython%2Cauto%3BC%2CC+Lang%2Cauto%3B&line2=OpenGL%2COpenGL%2Cffffff%3Bhtml%2Chtml%2Cauto%3B" alt="GitHub Readme Tech Stack" />
  </a>


