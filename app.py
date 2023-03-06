from tkinter import *
from chat import get_response

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
MSG_BG = "#2C3E50"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 12"
FONT_BOLD = "Helvetica 11 bold"

class ChatApp: 
    
    def __init__(self): 
        self.window = Tk()
        self.setup_main_window()

    def run(self):
        self.window.mainloop()

    def setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width = False, height = False)
        self.window.configure(width = 470, height = 550, bg = BG_COLOR)

        # head label 
        head_label = Label(self.window, bg = BG_COLOR, fg = TEXT_COLOR, 
                           text = "Welcome!", font = FONT_BOLD, pady = 10)
        head_label.place(relwidth=1)

        # divider
        line = Label(self.window, width = 450, bg = BG_GRAY)
        line.place(relwidth = 1, rely=0.07, relheight=0.012)

        # text widget 
        self.text_widget = Text(self.window, width = 20, height = 2, bg = BG_COLOR, 
                                fg = TEXT_COLOR, font = FONT, padx = 5, pady = 5)
        self.text_widget.place(relheight = 0.745, relwidth = 1, rely = 0.08)
       
        # Disable clicking/typing in text widget
        self.text_widget.configure(cursor = "arrow", state = DISABLED) 

        # scroll bar 
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight = 1, relx = 0.97)
        
        # scroll bar changes y position of the text widget
        scrollbar.configure(command = self.text_widget.yview) 

        # bottom label
        bottom_label = Label(self.window, bg = BG_GRAY, height = 80)
        bottom_label.place(relwidth = 1, rely = 0.825)

        # message entry box
        self.msg_entry = Entry(bottom_label, bg = MSG_BG, fg = TEXT_COLOR, font = FONT) 
        self.msg_entry.place(relwidth = 0.7, relheight = 0.06, rely = 0.008, relx = 0.011)
        self.msg_entry.focus() # Widget will be selected on application run 
        self.msg_entry.bind("<Return>", self.on_enter_pressed)

        # send button 
        send_button = Button(bottom_label, text = "Send", font = FONT_BOLD, width = 20,
                             bg = BG_GRAY, command = lambda: self.on_enter_pressed(None))
        send_button.place(relx = 0.77, rely = 0.008, relheight = 0.06, relwidth = 0.22)

    def on_enter_pressed(self, event):
        msg = self.msg_entry.get() # Get input text as string
        self.insert_message(msg, "You")

    def insert_message(self, msg, sender): 
        if not msg: # If message is empty
            return
        self.msg_entry.delete(0, END) # Remove current text from entry box
        msg1 = f"{sender}: {msg}\n\n"

        self.text_widget.configure(state = NORMAL) # Enable text widget for insert
        self.window.after(1000, self.text_widget.insert(END, msg1)) # Add delay after insert
        self.text_widget.configure(state = DISABLED) # Disable it again

        msg2 = f"Botty: {get_response(msg)}\n\n"
 
        self.text_widget.configure(state = NORMAL) # Enable text widget for insert
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state = DISABLED) # Disable it again

        self.text_widget.see(END) # View of text widget will always be the end

if __name__ == "__main__": 
    app = ChatApp()
    app.run()