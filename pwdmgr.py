import string
import random
from os.path import exists

def gen_pass(size=8, chars=string.ascii_letters + string.digits) -> str:
    return ''.join(random.SystemRandom().choice(chars) for _ in range(size))

print("Please input the desired password size: ")
try:
    user_size = int(input())
except Exception as e:
    print(e)

if not exists("passwords"):
    with open('passwords', 'w') as file:
        file.write(gen_pass(user_size))
else:
    with open('passwords', 'a') as file:
        file.write("\n" + gen_pass(user_size))