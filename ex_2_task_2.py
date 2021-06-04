# Python refresher exercises 2 - task 2

# - as part of some app, the user has to create a valid email address
# - any address will do as long as it's valid
# - your validation will only allow a number of retries if a invalid email is given (default 3)
# - once the number of attempts is exhausted (you should show how many retries are left!), set the
#   variable (flag) gave_up to True and bail out.
# 
# - it's OK to start with my solution from the lecture in flow control, although I 
#   encourage you to try you own solution first (if you can't remember). Any other, working
#   solution is fine, too!
# - when it comes to how to react to an error, your user MUST re-enter a string, but it's up to 
#   you how helpful you want to be:
#   - you could just list all the rules on error and demand a new input
#   - you could list the appropriate error message returned from you function and demand a new input
#   - you could do something fancy and only require re-typing of what's wrong (if that's technically possible):
#       e.g. if the pre @ is wrong (too long, contains a invalid char) you could demand that
#       only that incorrect part is re-entered. Warning - this can be complicated and laborious to test!
# - Note that the check for a valid email is a bit weird (b/c of how I set it up):
#   - iff the first return is None (r == None), the email is valid (yes, None doesn't sound like an OK ...)
#   - if you didn't get None (r != None), then r contains an error code, which you could use in your 
#     flow control for branching, if you want to do something fancy

# Optionally, you can use regex for all this!

# Once you're solved this, run some tests to show me that it works. 
# Again, manually copy/paste the console output in a text file (results2.txt)



# import your function from the previous .py file as a module (you can abbreviate it)
# use ex_2_task_2 here instead once your function works!
from ex_2_task_1 import is_valid_email_address as is_valid 
from tkinter import *
gave_up = False
attempts_left = 3

# your code - start
def checkEmail(email):
   print(email)

# simple GUI to validate the email
window=Tk()

window.title('Validate your email')
window.geometry("300x200+10+20")

lbl=Label(window, text="Write your email below:", fg='Black', font=("Arial", 12))
lbl.place(x=60, y=50)
txtfield=Entry(window, text="", bd=5)
txtfield.place(x=80, y=100)
btn=Button(window, text="Validate email", fg='blue')
btn.place(x=100, y=150)
btn.bind('<Button-1>', checkEmail('hola'))
window.mainloop()


 
# your code - end
#if not gave_up:
    #print("valid email", email)
#else:
    #print("invalid email", email)
