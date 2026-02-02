from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


# Automatically handles ChromeDriver version
driver = webdriver.Chrome(ChromeDriverManager().install())

# Instagram users to message
users = ['User_name_1', 'User_name_2']
message_text = "final test"


class InstagramBot:

    def __init__(self, username, password, users, message):
        self.username = username
        self.password = password
        self.users = users
        self.message = message
        self.base_url = 'https://www.instagram.com/'
        self.bot = driver
        self.login()

    def login(self):
        self.bot.get(self.base_url)

        # Username
        WebDriverWait(self.bot, 20).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        ).send_keys(self.username)

        # Password
        password_field = WebDriverWait(self.bot, 20).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        )
        password_field.send_keys(self.password)
        password_field.send_keys(Keys.RETURN)

        time.sleep(5)

        # Save Login Info - Not Now
        self.bot.find_element(By.XPATH,
            '//button[text()="Not Now"]').click()
        time.sleep(3)

        # Notifications - Not Now
        self.bot.find_element(By.XPATH,
            '//button[text()="Not Now"]').click()
        time.sleep(3)

        # Open Direct Messages
        self.bot.find_element(By.XPATH,
            '//a[contains(@href,"/direct/inbox")]').click()
        time.sleep(4)

        self.send_messages()

    def send_messages(self):
        for user in self.users:

            # New message (pencil icon)
            self.bot.find_element(By.XPATH,
                '//button[contains(@aria-label,"New message")]').click()
            time.sleep(3)

            # Search user
            search_box = self.bot.find_element(By.NAME, 'queryBox')
            search_box.send_keys(user)
            time.sleep(3)

            # Select user
            self.bot.find_element(By.XPATH,
                '//div[@role="dialog"]//button').click()
            time.sleep(2)

            # Next
            self.bot.find_element(By.XPATH,
                '//div[@role="dialog"]//button[text()="Next"]').click()
            time.sleep(3)

            # Message box
            msg_box = self.bot.find_element(By.TAG_NAME, 'textarea')
            msg_box.send_keys(self.message)
            msg_box.send_keys(Keys.RETURN)
            time.sleep(4)


def main():
    InstagramBot(
        username="YOUR_USERNAME",
        password="YOUR_PASSWORD",
        users=users,
        message=message_text
    )
    input("DONE - Press Enter to exit")


if __name__ == "__main__":
    main()
