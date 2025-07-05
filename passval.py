def passValid(password):
    digit=symbol=lower=0
    ss=["!",'@','#',"$","%","^","&","*"]
    if len(password)>=12 and password[0].isupper():
        for ch in password:
            if ch.isdigit():
                digit+=1
                continue
            if ch in ss:
                symbol+=1
                continue
            if ch.islower():
                lower+=1
        if(digit>0 and symbol>0 and lower>0):return True
        else:return False
    else:
        return False
   



password="Jomonvincent@2004"
if(passValid(password)):
    print("login successfull")
else:
    print("login failed")