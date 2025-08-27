from enum import Enum
from random import randint
from bcrypt import hashpw, gensalt, checkpw

class Length(Enum):
    easy = 10
    medium = 20
    hard = 30

class Complexity(Enum):
    easy = 'abcdefghijklmnñopqrstuvwxyz'
    medium = 'abcdefghijklmnñopqrstuvwxyz1234567890'
    hard = 'abcdefghijklmnñopqrstuvwxyz1234567890,.<>-´¨+*`¿?¡=!&%()/$·|@#~'

class PasswordData():

    @staticmethod
    def generate_password(complexity: Complexity, length: Length):
        password = ''

        for _ in range(length.value):
            random_position = randint(0, len(complexity.value) - 1)
            password += complexity.value[random_position]

        return password
    
    @staticmethod
    def hash_password(password: str):
        return hashpw(password.encode(), gensalt()).decode()
    
    @staticmethod
    def check_password(plain_password: str, hashed_passsword: str):
        hashed_passsword = hashed_passsword.strip()
        return checkpw(plain_password.encode(), hashed_passsword.encode())
