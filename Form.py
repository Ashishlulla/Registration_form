import tkinter as tk
import webbrowser
from tkinter import messagebox as m_box

window = tk.Tk()
window.maxsize(width=600, height=320)
window.title("Signup Page")
# ________________________________Frame__________________________
login_frame = tk.LabelFrame(window, background="#28719C")
login_frame.pack(side='left', anchor='nw')

signup_frame = tk.LabelFrame(window, background="#D8DDE3")
signup_frame.pack(side='left', anchor='ne')

# ______________________________End Frame ______________________
# ___________________________Icons____________________________
username = tk.PhotoImage(file='username.png')
password = tk.PhotoImage(file='secure.png')
twitter = tk.PhotoImage(file='twitter.png')
facebook = tk.PhotoImage(file='facebook1.png')
google = tk.PhotoImage(file='google1.png')
linkedin = tk.PhotoImage(file='linkedin.png')
signup = tk.PhotoImage(file='signup.png')


# ____________________________end Icon_____________________________
# __________________________Login Labels___________________________

login_label = tk.Label(login_frame, text=' L O G I N ', font=('Arial', 16, 'bold', 'underline')
                       , background='yellow')
username_label = tk.Label(login_frame, text='Username : ', image=username, compound='left',
                          background="#28719C")
password_label = tk.Label(login_frame, text='Password : ', image=password, compound='left',
                          background="#28719C")
# ________________________________Sign Up Label__________________________
label = tk.Label(signup_frame, text='New Users can Sign Up through\n@Webcode', background="#D8DDE3",
                 fg='green')

label1 = tk.Label(signup_frame, text='Developed By: Ashish Lulla', background="#D8DDE3",
                  fg='green')

# _____________________________ Labels Grid______________________________

login_label.grid(row=1, columnspan=3, padx=50, pady=50)
username_label.grid(row=2, column=0, sticky=tk.W, padx=10, pady=10)
password_label.grid(row=3, column=0, sticky=tk.W, padx=10, pady=10)
label.grid(row=1, columnspan=3, padx=20, pady=20)
label1.grid(row=7, columnspan=4, padx=20)
# ______________________________Labels Grid End__________________________

# _______________________________ Entry Box _________________________________
username_var = tk.StringVar()
username_box = tk.Entry(login_frame, width=40, textvariable=username_var)
username_box.focus()

password_var = tk.StringVar()
password_box = tk.Entry(login_frame, width=40, show="*", textvariable=password_var)
# ________________________________End Entry Box _____________________________

# _________________________________ Entry Grid________________________________
username_box.grid(row=2, column=1, sticky=tk.W, padx=20, pady=10)
password_box.grid(row=3, column=1, sticky=tk.W, padx=20, pady=10)
# _________________________________End Entry Box Grid____________________________
# _________________________________Check Button _______________________________
remember_var = tk.StringVar()
remember = tk.Checkbutton(login_frame, text='Remember me', background="#28719C", variable=remember_var,
                          onvalue="Remember",
                          offvalue="Don't Remember")
remember.grid(row=4, column=1, sticky=tk.W, padx=20, pady=10)
# _________________________________End Check Button____________________________
# ___________________________________ Button __________________________________
login = tk.Button(login_frame, text=' Log in ', background='green', width=15, command=login)

sign_up_button = tk.Button(signup_frame, text='Sign Up', background='purple', width=100,
                           image=signup, compound='left', fg='white', command=sign_up)
google_button = tk.Button(signup_frame, text='Google', background='#9C3333', width=100,
                          image=google, compound='left', fg='white', command=google_url)
facebook_button = tk.Button(signup_frame, text='facebook', background='#72B1DB', width=100,
                            image=facebook, compound='left', fg='white', command=facebook_url)
twitter_button = tk.Button(signup_frame, text='twitter', background='#1875F0', width=100,
                           image=twitter, compound='left', fg='white')
linkedin_button = tk.Button(signup_frame, text='Linkedin', background='#494A4D', width=100,
                            image=linkedin, compound='left', fg='white')

# _________________________________End Button ________________________________
# _________________________________Button Grid _____________________________
login.grid(row=4, column=1, sticky=tk.E, padx=20, pady=30)
sign_up_button.grid(row=2, columnspan=4, padx=20, pady=5)
google_button.grid(row=3, columnspan=4, padx=20, pady=5)
facebook_button.grid(row=4, columnspan=4, padx=20, pady=5)
twitter_button.grid(row=5, columnspan=4, padx=20, pady=5)
linkedin_button.grid(row=6, columnspan=4, padx=20, pady=10)

# ________________________________End Button Grid_____________________________

window.mainloop()
