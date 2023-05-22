import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="class")
def saucedemo(request):
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    request.cls.driver = driver

    def teardown():
        driver.quit()

    request.addfinalizer(teardown)
