
link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_id("book")
# говорим Selenium проверять в течение 13 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR")
    )
button.click()

x = browser.find_element_by_id("input_value").text
result = calc(x)

answer_field = browser.find_element_by_id("answer")
answer_field.send_keys(result)

button2 = browser.find_element_by_xpath("//button[text()='Отправить']")
button2.click()