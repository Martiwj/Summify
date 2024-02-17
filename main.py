import customtkinter
from ai import get_chat_completion
from pagereader import read_webpage

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()

root.geometry("800x1000")


def summorize():        
    # Retrieve text from entry1 and set it to the textbox
    text_to_set = entry1.get()
    promt = read_webpage(text_to_set)
    textbox.insert("1.0",get_chat_completion('key spects of this article:\n\n'+promt))
    
def clear_textbox():
    textbox.delete(1.0, 'end')
    
    
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(textbox.get('1.0', customtkinter.END).rstrip())

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Enter URL...")
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="", width=200)
entry1.pack(pady=12, padx=10)

textbox = customtkinter.CTkTextbox(master=frame, height=300, width=600)
textbox.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Summorize!", command=summorize)
button.pack(pady=12, padx=10)

copy_button = customtkinter.CTkButton(master=frame,text="Copy", command=copy_to_clipboard)
copy_button.pack(pady=12, padx=10)

clear_button = customtkinter.CTkButton(master=frame, text="Clear", command=clear_textbox)
clear_button.pack(pady=12, padx=10)

root.mainloop()
