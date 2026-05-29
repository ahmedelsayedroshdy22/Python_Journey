Age = 30 
Height = 184.5 
Name = "Ahmed"
Student = False
No_Value = None 

mylist = [Age , Height , Name , Student , No_Value]

for i in mylist:
    try: 
     print(f"Value for each variable   : {len(i)}" )

    except:
       print(f"No length for the value {i}" )
