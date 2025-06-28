from faker import Faker

fake = Faker()

def login_generator():
    return fake.user_name()

def password_generator():
    return str(fake.random_number(digits=5))

def name_generator():
    return fake.first_name()

