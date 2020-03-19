import factory
from data.user import User


class UserFactory(factory.Factory):
    class Meta:
        model = User

    username = factory.Faker('username')
