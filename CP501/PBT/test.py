while True:
    UName=input("User Name ?")
    Pass=input("Password ?")
    if UName!='Bob' or Pass!='12345':
        print ("Please Try again ")
        continue
    break
print ("Welcome Bob")
