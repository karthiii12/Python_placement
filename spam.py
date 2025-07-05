msg="heyy karthikpm@gmai.com,career opportunities are now at your fingertips.contact +911123455767 for more details"
cons=["@","mail","+911"]
for i in cons:
    if i in msg:
        print("This is a Spam message")
        break
