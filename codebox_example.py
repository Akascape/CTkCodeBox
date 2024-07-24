import customtkinter
from CTkCodeBox import *

root = customtkinter.CTk()

# Create a CTkLabel at the top
label = customtkinter.CTkLabel(root, text="Code Examples")
label.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

# Create code boxes for different languages
languages = ["python", "javascript", "c++", "rust", "html", "json"]
sample_code = {
    "python": "print('Hello, world!')",
    "javascript": "console.log('Hello, world!');",
    "c++": "#include <iostream>\nint main() {\n    std::cout << \"Hello, world!\";\n    return 0;\n}",
    "rust": "fn main() {\n    println!(\"Hello, world!\");\n}",
    "html": "<!DOCTYPE html>\n<html>\n<head>\n    <title>Hello</title>\n</head>\n<body>\n    <p>Hello, world!</p>\n</body>\n</html>",
    "json": "{\n    \"message\": \"Hello, world!\"\n}"
}

for i, lang in enumerate(languages):
    codebox = CTkCodeBox(root, height=100, language=lang)
    codebox.insert("1.0", sample_code[lang])
    codebox.grid(row=(i // 3) + 1, column=i % 3, padx=10, pady=10, sticky="nsew")

# Make the code boxes resizable
root.grid_rowconfigure((1,2), weight=1)
root.grid_columnconfigure((0,1,2), weight=1)

root.mainloop()

