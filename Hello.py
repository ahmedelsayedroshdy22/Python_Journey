
Name = "968-maria, (D@t@ Engineer ) ;; 27y  "

New= Name.strip().replace("968-", "").replace("@", "a").replace(";;", "").replace("(", "").replace(")", "").split(",")
Age = New[1].strip().split("  ")



print(f"Age: {Age}")
