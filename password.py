# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def length_check(password: str) -> bool:
    if len(password) > 10:
        return True
    else:
        return False


def character_categories(password: str) -> bool:
    l = False
    u = False
    d = False
    s = False
    specialchar="$@_£%&*~#"
    for char in password:
        if char.islower():
            l = True
            break
        elif char.isupper():
            char = True
            break
        elif char.isdigit():
            d = True
            break
        elif char in specialchar:
            s = True
            break
    return (l and u and d and s)

        


def year_of_birth(password: str) -> bool:
    birthyears = [str(i) for i in range(1920,2021)]
    return not any(i in password for i in birthyears)
  
        




def consecutive_increasing_substring(password: str) -> bool:
    for i in range(0,len(password)-2):
        substring = password[i:i+2]
        max_char = max(substring)
        min_char = min(substring)
        if (ord(max_char) - ord(min_char) + 1 == len(substring)):
            return False
    return True

def unique_substrings(password: str) -> bool:
    for i in range(0,len(password)-2):
        substring = password[i:i+2]
        password_ = password.replace(substring, '')
        if(substring in password_):
            return False
    return True
    

        


def shortest_strong_substring(password: str) -> str:
    if(length_check(password)):
        n = 10
        for i in range(n,len(password)):
            for j in range(0,len(password)-i):
                substr = password[j:j+i]
                if character_categories(substr) and (not year_of_birth(substr)) and (not consecutive_increasing_substring(substr)) and (unique_substrings(substr)):
                        return substr
    return ''

print(shortest_strong_substring('1930xyz##T234T'))