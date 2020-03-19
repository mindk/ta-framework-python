import factory
from data.models.user import User

# https://factoryboy.readthedocs.io/en/latest/
# https://github.com/joke2k/faker


class UserFactory(factory.Factory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    password = factory.Faker('password')
