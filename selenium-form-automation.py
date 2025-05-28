import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Step 1 - Lunch Browser
driver=webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()
print(driver.title)

# Step 2 - First Name (XPath)
driver.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys("Shweta")

# Step 3 - Last Name (CSS Selector)
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Last Name']").send_keys("Chhari")

# Step 4 - Address (CSS Selector)
driver.find_element(By.CSS_SELECTOR,"textarea[ng-model='Adress']").send_keys("Chembur Camp")

# Step 5 - Email address (XPATH)
driver.find_element(By.XPATH,"//input[@type='email']").send_keys("Shwetachhari@gmail.com")

# Step 6 - phone number (XPATH)
driver.find_element(By.XPATH, "//input[@ng-model='Phone']").send_keys("9876543210")

# Step 7 - Gender (XPATH)
driver.find_element(By.XPATH, "//input[@value='FeMale']").click()

# Step 8 - Hobbies (Contains xpath)
checkbox_values = ['Hockey', 'Movies']
for value in checkbox_values:
    xpath = f"//input[contains(@value,'{value}')]"
    driver.find_element(By.XPATH,xpath).click()
time.sleep(3)

# Step 9 - Language (XPATH)
languages=["English","Hindi"]
driver.find_element(By.ID,"msdd").click()
for lang in languages:
    driver.find_element(By.PARTIAL_LINK_TEXT,lang).click()
time.sleep(3)


# Step 9 - skills
skills=Select(driver.find_element(By.ID,'Skills'))
skills.select_by_visible_text("Python")
time.sleep(3)

# Step 10 - Select Country
driver.find_element(By.CLASS_NAME,"selection").click()
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("India")
driver.find_element(By.XPATH,"//li[text()='India']").click()
time.sleep(3)

# Step 11 - Date of Birth
year=Select(driver.find_element(By.ID,"yearbox"))
year.select_by_visible_text("1997")
time.sleep(3)

month=Select(driver.find_element(By.XPATH,"//select[@placeholder='Month']"))
month.select_by_visible_text("December")

date=Select(driver.find_element(By.ID,"daybox"))
date.select_by_visible_text("6")
time.sleep(3)

# Step 12 - Password
password_field = driver.find_element(By.ID, "firstpassword")
password_field.send_keys("Test@123")

# Step 13 - Confirm Password
confirm_password_field = driver.find_element(By.ID, "secondpassword")
confirm_password_field.send_keys("Test@123")

# Step 14 - Submit
driver.find_element(By.XPATH,"//button[@type='submit']").click()














