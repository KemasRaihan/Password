# checks if password is longer than 10 cahracters
def length_check(password: str) -> bool:
    if len(password) > 10:
        return True
    else:
        return False


# checks if password contains a lowercase, uppercase, digits and a special character.
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

        

# checks if password contains a year of birth between 1920 to 2020
# For example: if password = 'xyG1989' the function returns True because password contains the substring: '1989'
def year_of_birth(password: str) -> bool:
    birthyears = [str(i) for i in range(1920,2021)]
    return not any(i in password for i in birthyears)
  
        

# checks if the password does NOT contain a substring of length 3 containing consecutive letters or digits
# For example: if password = '123ADE083xyzf@' then the function returns False because there password contains the substrings: '123' and 'xyz'
def consecutive_increasing_substring(password: str) -> bool:
    for i in range(0,len(password)-2):
        substring = password[i:i+2]
        max_char = max(substring)
        min_char = min(substring)
        if (ord(max_char) - ord(min_char) + 1 == len(substring)):
            return False
    return True

# checks if the password only contains unique substring of length 3
# For example: if password = 'abcH837abc@J7' then the function returns False because there password contains the substrings: 'abc' twice.
def unique_substrings(password: str) -> bool:
    for i in range(0,len(password)-2):
        substring = password[i:i+2]
        password_ = password.replace(substring, '')
        if(substring in password_):
            return False
    return True
    

        

# find a strong password with the shortest length within another password
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
