import re
# Python refresher exercises 2 - task 1

# Write and test a function is_valid_email_address(s) that evaluates string s as a valid email address 
# Returns: tuple of 2 elements (res, err):
#          res contains the result (None or error code)
#          err contains an error string ("seems legit" for None,  a short error message for the error code
#
# Rules: (these are mine, not the official web standards!)
# must have 3 parts: <A>@<B>.<C>
# A must have between 3 and 16 alpha numeric chars (test: isalnum()) 
# B must have between 2 and 8 alpha numeric chars (test: isalnum()) 
# C must be one of these:  com edu org gov 
#
# Here are some tests and the expected results:
# 
# charding@iastate.edu (None, 'Seems legit')
# chris.edu (1, 'Must have exactly one @!')
# chris@edu (4, 'post @ part must have exactly one dot!')
# @bla.edu (2, 'pre @ part must contain 3 - 16 alfanum chars')
# throatwobblermangrove@mpfc.org (2, 'pre @ part must contain 3 - 16 alfanum chars')
# chris@X.com (5, 'part after @ and before . must contain 2 - 8 alfanum chars')
# chris.harding@iastate.edu (3, 'pre @ part must only contain alfanum chars')
# chris@pymart.biz (7, 'past-dot part invalid, must be from: com, edu, org, gov')
# chris@letsgo!.org (6, 'part after @ and before . must only contain alfanum chars')
# chris@megasavings.org (5, 'part after @ and before . must contain 2 - 8 alfanum chars')
# tc@tank.com (2, 'pre @ part must contain 3 - 16 alfanum chars')
#
# your function MUST react the same (OK or error) but you don't have to use my exact error messages or codes 
# just something similar to that effect. You could even be more helpful e.g. 
# "throatwobblermangrove is too long (21 chars), must be 3 - 16"
# It's OK to bail out at the first proven error, even if there would have been more errors later!
# Also, I prb. forgot some possible edge cases, please add more if needed!

# As proof, please manually copy/paste the console output for one run into a file called
# results1.txt

def is_valid_email_address(s):
    
    # your code here
    errorCodes = ('Seems legit', 'Must have exactly one @!',
    'pre @ part must contain 3 - 16 alfanum chars', 'pre @ part must only contain alfanum chars',
    'post @ part must have exactly one dot!', 'part after @ and before . must contain 2 - 8 alfanum chars',
    'part after @ and before . must only contain alfanum chars', 'past-dot part invalid, must be from: com, edu, org, gov')
    
    #Regular expression to evaluate if the string match with the pattern
    regex = re.compile(r'^(\w){3,16}[@](\w){3,8}[\.](\bcom\b|\bedu\b|\borg\b|\bgov\b)')
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


__name__ = '__main__'
    

# This if ensures that the following is NOT run if this file was imported as a module (which we'll do next!)
if __name__ == "__main__":
    # tests, including edge cases (incomplete? add more!)
    email_list = ["charding@iastate.edu", 
        "chris.edu",
        "chris@edu",
        "@bla.edu",
        "throatwobblermangrove@mpfc.org", 
        "chris@X.com",
        "chris.harding@iastate.edu",
        "chris@pymart.biz",
        "chris@letsgo!.org",
        "chris@megasavings.org",
        "tc@tank.com",
        ]
    # validate each email from the list
    for e in email_list:
        r, s = is_valid_email_address(e) 
        if r == 'None': #Use '' to compare 2 strings
            print(e, s) # OK
        else:
            print(f"{e} - error: {s}, error code: {r}") # Error

        
