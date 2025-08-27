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

class PasswordService():

    @staticmethod
    def generate_password(complexity: Complexity, length: Length):
        try:
            password = ''

            for _ in range(length.value):
                random_position = randint(0, len(complexity.value) - 1)
                password += complexity.value[random_position]

            return password
        except:
            return 'Ha ocurrido un error intentalo mas tarde.'
    
    @staticmethod
    def hash_password(password: str):
        try:
            return hashpw(password.encode(), gensalt()).decode()
        except:
            return 'Ha ocurrido un error intentalo mas tarde.'
    
    @staticmethod
    def check_password(plain_password: str, hashed_passsword: str):
        try:
            hashed_passsword = hashed_passsword.strip()
            return checkpw(plain_password.encode(), hashed_passsword.encode())
        except ValueError:
            return False
        except:
            return 'Ha ocurrido un error intentalo mas tarde.'
