import pytest
from faker import Faker


@pytest.fixture()
def fn_scope():
    print("Function Session started")

    yield

    print("Function Session terminated")


@pytest.fixture(scope="class")
def cls_scope():
    print("Class session started")

    yield

    print("Class session terminated")


@pytest.fixture(scope="module")
def module_scope():
    print("Module session started")

    yield

    print("Module session terminated")


@pytest.fixture(scope="package")
def package_scope():
    print("package session started")

    yield

    print("package session terminated")


@pytest.fixture(scope="session")
def session_scope():
    print("session session started")

    yield

    print("session session terminated")


def test_1(cls_scope, module_scope, package_scope, fn_scope, session_scope):
    print("First test")


def test_2(package_scope, module_scope, session_scope, cls_scope, fn_scope):
    print("Second test")

    faker = Faker()

    san = faker.name()

    print(faker.text())
