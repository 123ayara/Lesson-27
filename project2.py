import random
import string
def generate_password(length):
 if length<6:
  return "Password length should be at least 6 characters."
 lowercase=string.ascii_lowercase
 uppercase=string.ascii_uppercase
 digits=string.digits
 password_chars=[random.choice(lowercase),random.choice(uppercase),random.choice(digits)]
 all_chars=lowercase+uppercase+digits
 password_chars+=random.choices(all_chars,k=length-3)
 random.shuffle(password_chars)
 password=''.join(password_chars)
 return password
password=generate_password(12)
print("generated password:",password)
