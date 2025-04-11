import random
import datetime
def to_uppercase(text):
    return text.upper()

def get_today_date():
    return datetime.date.today().strftime("%Y-%m-%d-%H-%M-%S")

def count_vowels(beautiful):
    vowels = "aeiou"
    return sum(1 for char in beautiful if char in vowels)

def generate_random_number():
    return random.randint(1,200)

def get_full_name():
    return "Ovili Ekene L"
