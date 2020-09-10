import string
import random

def generate_pass():
    digits_list = list(string.digits)
    symbols = list(string.punctuation)
    cap_aplha = list(string.ascii_uppercase)
    small_aplha = list(string.ascii_lowercase)
    master_list = digits_list + symbols + cap_aplha + small_aplha
    # print(master_list)

    password = ""
    password_size = random.randint(12,18)
    for i in range(password_size):
        password += random.choice(master_list)
    
    return password

if __name__ == "__main__":
    print("-----------------------------------------------------\nIntelligent Password Generator of VARIABLE LENGTH with\nMIXED UPPER CASE, LOWER CASE characters and SYMBOLS\n-----------------------------------------------------\n ")
    print(generate_pass())

