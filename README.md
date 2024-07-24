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
<br> **Requirements:** Pygments and TkLineNums

## Simple Usage
```python
import customtkinter
from CTkCodeBox import *

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
| fg_color | change the fg_color of the widget|
| **language** | set the language lexer for the codebox |
| **theme** | change the overall color theme for the code syntax |
| line_numbering | boolean, enable or disable the line numbering |
| numbering_color | change text color of the line numbering |
| menu | boolean, enable or disable the right click popup menu |
| menu_fg_color | color of the menu (optional) |
| menu_text_color | text color of the menu buttons (optional) |
| menu_hover_color | hover color of the menu buttons (optional) |
| wrap | enable or disabled word wrapping in the textbox |
| select_color | change the selection color of the codebox |
| cursor_color | change the cursor color I (blinking) |
| undo | boolean, enable or disable the undo text feature |
| _*Other Parameters_ | _All other parameters of ctktextbox can be passed in ctkcodebox_ |

## Methods
- **.insert(index, code)**: insert code in the box 
- **.configure(kwargs)**: change parameters of the codebox
- **.cget(parameter)**: get the parameter name from the codebox
- **.update_code()**: update the code syntax colors
- **.clear_code()**: delete all the code from the box
<br>
<a href="https://github-readme-tech-stack.vercel.app">
<img src="https://github-readme-tech-stack.vercel.app/api/cards?title=Languages&lineCount=4&width=520&bg=%230D1117&badge=%23161B22&border=%2321262D&titleColor=%2358A6FF&line1=python%2Cpython%2Cfff800%3BCplusplus%2C%2B%2B%2C7bc9b1%3Bcplusplus%2Csharp%2C6c3bb2%3BCplusplus%2C+%2C4a82cc%3Bjavascript%2Cjavascript%2Cf0fc0d%3B&line2=lua%2Clua%2C5d72e6%3BRust%2Crust%2Ce62323%3Bperl%2Cperl%2C92d5d3%3Bkotlin%2Ckotlin%2C6dfa21%3Bruby%2Cruby%2Cff0000%3B&line3=swift%2Cswift%2Cfe811b%3Bphp%2Cphp%2C3749b3%3Breact%2Creact%2Cd3ff00%3Bjson%2Cjson%2Cffe300%3Bgo%2Cgo%2C11ffdc%3B&line4=yaml%2Cyaml%2C6dc2af%3Bxml%2Cxml%2C63f030%3Bcss%2Ccss%2C1ff9f2%3Bhtml%2Chtml%2C2bc5b4%3BTypescript%2CTypescript%2C42b1c2%3BJAVA%2Cjava%2Ceffc00%3B" alt="Languages" />
</a>

More lexers available here: https://pygments.org/docs/lexers/

## Color Themes
```
abap, arduino, autumn, borland, colorful, default, dracula, emacs, friendly_grayscale, friendly, fruity, github-dark, gruvbox-dark, gruvbox-light, igor, inkpot, lightbulb, lilypond, lovelace, manni, material, monokai, murphy, native, nord-darker, nord, one-dark, paraiso-dark, paraiso-light, pastie, perldoc, rainbow_dash, rrt, sas, solarized-dark, solarized-light, staroffice, stata-dark, stata-light, tango, trac, vim, vs, xcode, zenburn
```
More style examples given here: https://pygments.org/styles/

Follow me for more stuff like this: [`Akascape`](https://github.com/Akascape/)
### That's all, hope this project can help!

