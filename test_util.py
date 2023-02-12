from faker import Faker

fake = Faker('ru_RU')


class Generate:
    @staticmethod
    def user_name():
        return fake.first_name()

    @staticmethod
    def user_email():
        return fake.free_email()

    @staticmethod
    def user_password():
        return fake.bothify("?#?#??#?#")

    @staticmethod
    def user():
        return User(Generate.user_name(), Generate.user_email(), Generate.user_password())


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


DefaultUser = User('Дарья', 'sergeeva06261@ya.ru', '8Zho04A9')
