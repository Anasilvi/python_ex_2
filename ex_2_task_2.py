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
#from ex_2_task_1 import is_valid_email_address as is_valid 
import re
from tkinter import *
gave_up = False
attempts_left = 3

# your code - start

#Adding the function because I had problems importing as a module
def is_valid_email_address(s):
    
    # your code here
    errorCodes = ('Seems legit', 'Must have exactly one @!',
    'pre @ part must contain 3 - 16 alfanum chars', 'pre @ part must only contain alfanum chars',
    'post @ part must have exactly one dot!', 'part after @ and before . must contain 2 - 8 alfanum chars',
    'part after @ and before . must only contain alfanum chars', 'past-dot part invalid, must be from: com, edu, org, gov')
    
    #Regular expression to evaluate if the string match with the pattern
    regex = re.compile(r'^(\w){3,16}[@](\w){3,8}[\.][com|org|edu]')
    if(regex.match(s)):
        return ('None',errorCodes[0])
    
    #Matching the error codes
    else:
        if s.count('@') != 1:
            return(1,errorCodes[1])
        if  len(s.split('@')[0]) < 3 or len(s.split('@')[0]) > 16:
            return(2,errorCodes[2])
        if re.search('[^a-zA-Z\d\s:]',s.split('@')[0]):
            return(3,errorCodes[3])
        if s.split('@')[1].count('.') != 1:
            return(4,errorCodes[4])
        if  len(s.split('@')[1].split('.')[0]) < 2 or len(s.split('@')[1].split('.')[0]) > 8:
            return(5,errorCodes[5])
        if not (re.search('.*[@](\w){3,8}[\.].*', s)):
            return(6,errorCodes[6])
        if s.split('.')[1] not in ('com','org','edu','gov'):
            return(7,errorCodes[7])
    return ('Invalid','Unknown error')




# simple GUI to validate the email
class MyGUI:
    def __init__(self, win):

        self.lbl=Label(window, text="Write your email below:", fg='Black', font=("Arial", 12))
        self.lbl.place(x=60, y=50)
        self.txtfield=Entry(window, text="", bd=5)
        self.txtfield.place(x=80, y=100)
        self.btn=Button(window, text="Validate email", fg='blue')
        self.btn.place(x=100, y=150)
        self.btn.bind('<Button-1>', self.checkEmail)
    def checkEmail(self, event):
        print(is_valid_email_address(self.txtfield.get()))

window=Tk()
mywin=MyGUI(window)
window.title('Validate your email')
window.geometry("300x200+10+20")
window.mainloop()


 
# your code - end
#if not gave_up:
    #print("valid email", email)
#else:
    #print("invalid email", email)
