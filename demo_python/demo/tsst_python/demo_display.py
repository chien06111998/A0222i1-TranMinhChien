from tkinter import *

def click():
    print("Button clicked")

window = Tk()
window.geometry("400x600")

window.title("HTX Tool VN")
txt_login = Label(window, text="Đăng nhập")
txt_login.grid(column=0, row=0)

txt_username = Label(window, text="Tài khoản")
input_username = Entry(window, width=350)
txt_username.grid(column=1, row=1)
input_username.grid(column=2, row=1)

key_button = Button(window, text="Key", command=click)
register_button = Button(window, text="Đăng ký", command=click)
login_button = Button(window, text="Đăng Nhập", command=click)
key_button.pack(padx=50, pady=50)
register_button.pack(padx=50, pady=50)
login_button.pack(padx=50, pady=50)

key_button.grid(column=1, row=3)
register_button.grid(column=2, row=3)
login_button.grid(column=3, row=3)

window.mainloop()