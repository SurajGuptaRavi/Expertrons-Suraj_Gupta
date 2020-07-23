N = input("Enter the Number")
if N.isdigit() and len(N)==10 and int(N[0]) in [7,8,9]:
    print("VALID")
else:
    print("NOT VALID")
