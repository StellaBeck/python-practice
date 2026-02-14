def check_password_strength(password):
    if password.__len__() < 6:
        return "Weak"
    elif password.isalnum():
        return "Medium"
    else:
        contains_special_ch = False
        contains_alp = False
        contains_num = False
        for ch in "!@#$%^&*()_+{}[]\\|;:'\",./<>?-=":
            if ch in password:
                contains_special_ch = True
                break
        for ch in "abcdefghijklmnopqrstuvwxyz":
            if ch in password.lower():
                contains_alp = True
                break
        for ch in "1234567890":
            if ch in password:
                contains_num = True
                break
        if(contains_special_ch and contains_alp and contains_num):
            return "Strong"

print(check_password_strength("4fe"))
print(check_password_strength("ag448fg"))
print(check_password_strength("ag44*8fg"))