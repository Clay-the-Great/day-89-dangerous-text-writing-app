from threading import Timer
import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
WATERMARK_TEXT = "Watermark"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
LIGHT_GREEN = "#E8F3D6"
DARK_BLUE = "#1C658C"
YELLOW = "#f7f5dd"
GREY = "#CFD2CF"
FONT_NAME = "Courier"
FONT_NAME_2 = "Sans Serif"
TIME_DELAY = 3


# ------------------------------Functionalities-------------------------

class App:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.config(pady=50, padx=50)
        self.window.title("Dangerous Text Editor")
        self.timer = Timer(TIME_DELAY, self.delete)
        self.timer.start()

        self.heading_label = tkinter.Label(
            text=f"You Lose Everything After {TIME_DELAY} Seconds of No Typing",
            fg=DARK_BLUE, font=(FONT_NAME, 20, "bold")
        )
        self.heading_label.grid(column=0, row=0)
        self.text_field = tkinter.Text(self.window,
                                       font=('sans serif', 20),
                                       width=50,
                                       height=6,
                                       pady=10,
                                       background="black",
                                       foreground="white",
                                       )
        self.text_field.grid(column=0, row=1, pady=20)
        self.text_field.bind('<KeyPress>', self.on_key_press)

        self.window.mainloop()

    def on_key_press(self, event):
        self.timer.cancel()
        self.timer = Timer(TIME_DELAY, self.delete)
        self.timer.start()

    def delete(self):
        self.text_field.delete("1.0", "end")


app = App()

# This project has to use OOP. I didn't use a class on my first try, and it didn't work, below is why.

# def on_key_press(event):
#     global timer
#     timer.cancel()  # This destructs the previous timer.
#     new_now = datetime.now()
#     new_run_at = now + timedelta(seconds=3)
#     new_delay = (run_at - now).total_seconds()
#     timer = Timer(new_delay, delete).start()  # This creates a new timer, so this doesn't work.
