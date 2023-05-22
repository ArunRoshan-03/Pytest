import random

import pytest
from faker import Faker

from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class TestSaucedemo(BaseClass):
    def test_login(self):
        self.username = "standard_user"
        self.password = "secret_sauce"
        self.driver.find_element(By.ID, "user-name").send_keys(self.username)
        self.driver.find_element(By.ID, "password").send_keys(self.password)
        self.driver.find_element(By.ID, "login-button").click()

    def test_add_to_cart(self):
        detail = []
        validating_price = 0
        fake_data = Faker()
        add_cart_button = self.driver.find_elements(By.XPATH,
                                                    "//button[@class='btn btn_primary btn_small btn_inventory']")
        for data in random.sample(add_cart_button, 2):
            for cart in add_cart_button:
                if cart == data:
                    cart.click()
        self.driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        price = self.driver.find_elements(By.XPATH, "//div[@class='inventory_item_price']")
        for alpha in price:
            detail.append(alpha.text)
        for beta in detail:
            total_cost = float(beta.replace("$", ""))
            validating_price = validating_price + total_cost
        self.driver.find_element(By.ID, "checkout").click()
        self.driver.find_element(By.ID, "first-name").send_keys(fake_data.name())
        self.driver.find_element(By.ID, "last-name").send_keys(fake_data.name())
        self.driver.find_element(By.ID, "postal-code").send_keys(fake_data.random_number(digits=6))
        self.driver.find_element(By.ID, "continue").click()
        total = self.driver.find_element(By.XPATH, "//div[@class='summary_subtotal_label']").text
        float_price = float(total.replace("Item total: $", ""))
        assert float_price == validating_price, "Issues in adding Product"

