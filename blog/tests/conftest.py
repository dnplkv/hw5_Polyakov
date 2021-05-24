from account.models import User
from faker import Faker
import pytest


@pytest.fixture(autouse=True, scope='function')
def enable_db_access_for_all_tests(db):
    pass


@pytest.fixture(scope='function')
def acc_fixt():
    acc = User.objects.create()
    yield acc


@pytest.fixture(scope='function')
def fake_fixt():
    faker = Faker()
    yield faker
