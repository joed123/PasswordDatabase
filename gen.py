import random
import string


def generate_password(uppercase, lowercase, digits, specialchar, length):
    character_pool = ""
    if uppercase:
        character_pool += string.ascii_uppercase
    if lowercase:
        character_pool += string.ascii_lowercase
    if digits:
        character_pool += string.digits
    if specialchar:
        character_pool += string.punctuation

    if not character_pool:  
        return "No characters selected"

    return "".join(random.choice(character_pool) for _ in range(length))