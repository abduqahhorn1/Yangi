login = input('login : ')
password = input('Kodni kiriting : ')



assert len(login)>5, "login xato"
assert type(password)==int, "raqam kiriting"
assert len(password)>5, "parol xato"

print("Saytga xush kelibsiz")