from selenium import webdriver

page = 0
count = 1
for i in range(page, count):
    URL = f"https:// ... &page={page}& ... "
    driver = webdriver.Chrome('drivers/chromedriver')
    driver.get(URL)
    screenshot = driver.save_screenshot(f"save/{page}page.png")
    driver.quit()
    page += 1
