import tkinter as tk
import pickle
import tkinter.messagebox


def register():
    def destroy_top_level():
        top_level.destroy()

    def sign_up():

        # get data from entry-s in sign-up page
        un = top_un_entry.get()
        pw = top_pw_entry.get()
        cf = top_cf_entry.get()

        # open database and load in
        try:
            with open('user.pickle', 'rb') as file:
                data = pickle.load(file)
        except FileNotFoundError:
            with open('user.pickle', 'wb') as file:
                data = {'admin': 'admin'}
                pickle.dump(data, file)
                file.close()
            with open('user.pickle', 'rb') as file:
                data.clear()
                data = pickle.load(file)

        # any entry is empty
        if un == '' or pw == '' or cf == '':
            hint.config(text="Any entry can't be entry!", fg='red')
            top_un_entry.delete(0, len(un))
            top_pw_entry.delete(0, len(pw))
            top_cf_entry.delete(0, len(cf))
            return

        # password is not equal to confirm password
        if pw != cf:
            hint.config(text='Password is not equal to Confirm Password', fg='red')
            top_pw_entry.delete(0, len(pw))
            top_cf_entry.delete(0, len(cf))
            return

        # username has been signed up
        if un in data:
            hint.config(text='This user name has been used.', fg='red')
            top_un_entry.delete(0, len(un))
            top_pw_entry.delete(0, len(pw))
            top_cf_entry.delete(0, len(cf))
            return

        # put new user in database in no-problem-conditions
        with open('user.pickle', 'wb') as file:
            data[un] = pw
            pickle.dump(data, file)
        tk.messagebox.showinfo('Welcome', "You've successfully signed up.")
        top_level.destroy()

    top_level = tk.Toplevel(width=500, height=500)
    top_level.title('register your account')

    # user name label and entry
    top_un_frame = tk.Frame(top_level, height=100, width=400, border=10)
    top_un_frame.pack()
    top_un_label = tk.Label(top_un_frame, text='User name : ', font=('Times New Roman', 20), width=10, anchor='w')
    top_un_label.pack(side=tk.LEFT)
    top_un_entry = tk.Entry(top_un_frame, font=('Times New Roman', 20))
    top_un_entry.pack(side=tk.RIGHT)

    # password label and entry
    top_pw_frame = tk.Frame(top_level, height=100, width=400, border=10)
    top_pw_frame.pack()
    top_pw_label = tk.Label(top_pw_frame, text='Password : ', font=('Times New Roman', 20), width=10, anchor='w')
    top_pw_label.pack(side=tk.LEFT)
    top_pw_entry = tk.Entry(top_pw_frame, font=('Times New Roman', 20), show='*')
    top_pw_entry.pack(side=tk.RIGHT)

    # confirm password label and entry
    top_cf_frame = tk.Frame(top_level, height=100, width=400, border=10)
    top_cf_frame.pack()
    top_cf_label = tk.Label(top_cf_frame, text='Confirm Password : ', font=('Times New Roman', 14), width=15,
                            anchor='w')
    top_cf_label.pack(side=tk.LEFT)
    top_cf_entry = tk.Entry(top_cf_frame, font=('Times New Roman', 20), show='*')
    top_cf_entry.pack(side=tk.RIGHT)

    hint = tk.Label(top_level)
    hint.pack()

    # button
    top_bt_frame = tk.Frame(top_level, height=100, width=200, border=10)
    top_bt_frame.pack()
    sign_up = tk.Button(top_bt_frame, text='Sign Up', command=sign_up)
    sign_up.pack(side=tk.LEFT, padx=10)
    cancel = tk.Button(top_bt_frame, text='cancel', command=destroy_top_level)
    cancel.pack(side=tk.RIGHT)

    top_level.mainloop()


def destroy_window(window):
    window.destroy()


def login(un, pw):
    with open('user.pickle', 'rb') as file:
        data = pickle.load(file)
    if (un not in data) or (un in data and pw != data[un]):
        tk.messagebox.showerror('Error', 'User name or Password is wrong!')
        return
    tk.messagebox.showinfo('welcome', 'Welcome to this system, ' + un)


def main():
    window = tk.Tk()
    window.title('Welcome to Joe Website')
    window.geometry('500x300')
    window.resizable(0, 0)

    # text of welcome
    welcome = tk.Label(window, text='Welcome', font=('Times New Roman', 20), height=2)
    welcome.pack()

    # user name label and entry
    un_frame = tk.Frame(window, height=100, width=400, border=10)
    un_frame.pack()
    label1_un = tk.Label(un_frame, text='User name : ', font=('Times New Roman', 20), width=10, anchor='w')
    label1_un.pack(side=tk.LEFT)
    un_entry = tk.Entry(un_frame, font=('Times New Roman', 20))
    un_entry.pack(side=tk.RIGHT)

    # password label and entry
    pw_frame = tk.Frame(window, height=100, width=400, border=10)
    pw_frame.pack()
    label1_pw = tk.Label(pw_frame, text='Password : ', font=('Times New Roman', 20), width=10, anchor='w')
    label1_pw.pack(side=tk.LEFT)
    pw_entry = tk.Entry(pw_frame, font=('Times New Roman', 20), show='*')
    pw_entry.pack(side=tk.RIGHT)

    button_frame = tk.Frame(window, height=100, width=300)
    button_frame.pack(pady=15)
    tk.Button(button_frame, text='login', bd=5, font=('times new roman', 12), width=6, command=lambda: login
    (un_entry.get(), pw_entry.get())).pack(side=tk.LEFT, padx=20)
    tk.Button(button_frame, text='register', bd=5, font=('times new roman', 12), width=6, command=register) \
        .pack(side=tk.LEFT)
    tk.Button(button_frame, text='cancel', bd=5, font=('times new roman', 12), width=6, command=lambda: destroy_window
    (window)).pack(side=tk.RIGHT, padx=20)

    window.mainloop()


if __name__ == '__main__':
    main()
