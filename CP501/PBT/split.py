f=open ("names.rtf","r")
list_names=[]
for l in f:
    list_names=list_names+l.split(",")
print (list_names)
f.close ()
