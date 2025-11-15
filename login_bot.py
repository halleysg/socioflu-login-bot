import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class SocioFluLoginBot:
	def __init__(self):
		self.driver = None
		self.base_url = "https://sociofutebol.com.br/"
		self.login_url = "https://nense.com.br"
		self.home_url = f"{self.login_url}/planos"

	def setup_driver(self):
		"""Initialize the Chrome WebDriver"""
		options = webdriver.ChromeOptions()
		options.add_argument('--headless')
		options.add_argument('--no-sandbox')
		options.add_argument('--disable-dev-shm-usage')
		options.add_argument('--disable-notifications')
		options.add_argument('--disable-gpu')

		self.driver = webdriver.Chrome(options=options)
		self.driver.implicitly_wait(10)

	def is_logged_in(self):
		"""Check if user is logged in by checking the current URL"""
		return self.driver.current_url == self.home_url

	def logout(self):
		"""Perform logout if user is logged in"""
		if self.is_logged_in():
			try:
				# Wait for the logout button and click it
				logout_button = WebDriverWait(self.driver, 10).until(
					EC.presence_of_element_located((By.CLASS_NAME, "fengi-exit"))
				)
				logout_button.click()
				time.sleep(2)  # Wait for logout pop-up
				
				cofirm_logout_button = WebDriverWait(self.driver, 10).until(
					EC.presence_of_element_located((By.CLASS_NAME, "swal2-confirm app-swal-button app-swal-button--confirm"))
				)
				cofirm_logout_button.click()
				time.sleep(2)  # Wait for logout to complete
				
				return True
			except TimeoutException:
				print("Could not find logout button")
				return False
		return True

	def login(self, username, password):
		"""Perform login with given credentials"""
		try:
			# Navigate to login page if not already there
			if self.driver.current_url != self.login_url:
				self.driver.get(self.login_url)

			login_button = WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located((By.CLASS_NAME, "header-18__container-wrapper-auth-button"))
			)
			login_button.click()
			time.sleep(2)  # Wait for logout to complete

			# Wait for login form elements
			username_field = WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located((By.ID, "mat-input-1"))
			)
			password_field = self.driver.find_element(By.ID, "mat-input-0")
			login_button = self.driver.find_element(By.CLASS_NAME, "login-btn")


			# Fill in the credentials
			username_field.clear()
			username_field.send_keys(username)
			password_field.clear()
			password_field.send_keys(password)

			# Click login button
			login_button.click()
			time.sleep(10)

			# Wait for redirect to home page
			WebDriverWait(self.driver, 10).until(
				lambda driver: driver.current_url == self.home_url
			)
			return True

		except TimeoutException as e:
			print(f"Login failed: {str(e)}")
			return False

	def run(self, username, password):
		"""Main method to run the login bot"""
		try:
			self.setup_driver()
			
			# Navigate to the initial URL
			self.driver.get(self.base_url)
			
			# If already logged in, logout first
			self.logout()
			
			# Perform login
			if self.login(username, password):
				print("Successfully logged in!")
			else:
				print("Login failed!")

		except Exception as e:
			print(f"An error occurred: {str(e)}")
		
		finally:
			if self.driver:
				self.driver.quit()

if __name__ == "__main__":
    from dotenv import load_dotenv
    import os
    import sys
    from datetime import datetime
    
    print(f"Script ran at: {datetime.now()}")
    # Load environment variables from .env file
    load_dotenv()
    
    # Get credentials from environment variables
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')
    
    if not username or not password:
        print("Error: Missing credentials!")
        print("Please create a .env file with USERNAME and PASSWORD")
        sys.exit(1)
    
    bot = SocioFluLoginBot()
    bot.run(username, password)