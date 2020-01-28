import random
import string


def generate_pass():
    pwlist = ([random.choice(string.punctuation)] + [random.choice(string.digits)]  # 100% 1 digit and 1 spec char
              + [random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(8)]  # 100% 8 letters
              + [random.choice(string.punctuation + string.ascii_lowercase + string.ascii_uppercase + string.digits)
                 # + some (from 1-30) sequence of letters or numbers or spec chars
                 for i in range(random.randint(1, 30))])
    random.shuffle(pwlist)
    password = ''.join(pwlist)
    return password


print(generate_pass())
