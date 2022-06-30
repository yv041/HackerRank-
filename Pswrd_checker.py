# Password Checker

print('Enter your Username ')
username = input()
print('Enter your Password ')
pswrd = str(input())
length = len(pswrd)
astrick = '*' * length

print(f'Hi {username} your password is {astrick} and {length} digit long')