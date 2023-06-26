import random
import string

class PasswordGenerator():

    def __init__(self, length, charset=string.ascii_letters + string.digits, count=float('inf')):
        self.length = length
        self.charset = charset
        self.count = count
        self.generated = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.generated==self.count:
            raise StopIteration
        else:
            self.generated+=1
            password=''
            for _ in range(self.length):
                password = password+ (random.choice(self.charset)) 

        return password
    

password = PasswordGenerator(length=8, charset=string.ascii_lowercase, count=4)


#print(next(password))
#print(next(password))
#print(next(password))
#print(next(password))
#print(next(password))

password2 = PasswordGenerator(length=8, count=4)

for passw in password2:
    print(passw)

