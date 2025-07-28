# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

def generate_password():
    lower_letters = list('abcdefghijklmnopqrstuvwxyz')
    upper_letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    numbers = list('123456789')
    symbols = list('!@#$%^&*()[]')

    letters_password = 10
    symbol_password = 4
    numbers_password = 3

    password_user = []

    # Distribute upper and lower letters
    if letters_password > 1:
        no_up_l = random.randint(1, letters_password - 1)
    else:
        no_up_l = 1
    no_l_l = letters_password - no_up_l

    up_l = [random.choice(upper_letters) for _ in range(no_up_l)]
    l_l = [random.choice(lower_letters) for _ in range(no_l_l)]
    syb = [random.choice(symbols)for _ in range(symbol_password)]
    nums = [random.choice(numbers) for _ in range(numbers_password)]

    password_user = up_l+l_l+syb+nums
    random.shuffle(password_user)
    password = ''.join(password_user)
    password_input.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if website == "" or email=="" or password== "":
        messagebox.showerror(title="Oops",message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered:\nEmail:{email}\nPassword:{password}\nIs it ok to save?")
        if is_ok:
            with open('password_generator.txt','a') as file:
                file.write(f"{website}|{email}|{password}\n")
        website_input.delete(0,END)
        password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20,bg=YELLOW)
canvas = Canvas(width=200, height=200,bg=YELLOW, highlightthickness=0)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=pass_img)
canvas.grid(row=0,column=1)

website_label = Label(text='Website:',bg=YELLOW,font=(FONT_NAME,10,'bold'))
website_label.grid(row=1,column=0)

website_input = Entry(window)
website_input.config(width=51)
website_input.grid(row=1,column=1,columnspan=2)
website_input.focus()

Email = Label(text='Email/Username:',bg=YELLOW,font=(FONT_NAME,10,'bold'))
Email.grid(row=2,column=0)

email_input = Entry(window)
email_input.config(width=51)
email_input.grid(row=2,column=1,columnspan=2)
email_input.insert(0,"ssanyukta16@gmail.com")

password = Label(text='Password:',bg=YELLOW,font=(FONT_NAME,10,'bold'))
password.grid(row=3,column=0)

password_input = Entry(window)
password_input.config(width=32)
password_input.grid(row=3,column=1)

generate_button = Button(text='Generate Password',command=generate_password)
generate_button.grid(row=3,column=2)


add_button = Button(text='Add',command=save_password)
add_button.grid(row=4,column=1,columnspan=2)
add_button.config(width=44)

window.mainloop()