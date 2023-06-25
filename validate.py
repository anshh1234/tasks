flag=True
while(flag==True):
    password = input("Enter a string with at least 1 capital letter (A-P), 1 small letter (c-z), 1 number (0-9), and 1 special character (@, #, !): ")
    
    has_capital = False
    has_small = False
    has_number = False
    has_special = False
    
    for char in password:
        if 'A' <= char <= 'P':
            has_capital = True
        elif 'c' <= char <= 'z':
            has_small = True
        elif '0' <= char <= '9':
            has_number = True
        elif char in '@#!':
            has_special = True
    
    if has_capital and has_small and has_number and has_special:
        print("valid")
        break
    else:
        print("Invalid")
        break
