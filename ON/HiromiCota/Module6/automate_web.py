from selenium import webdriver


browser = webdriver.Safari()
browser.get('https://acounts.google.com/signup')
# scrape for first name field
firstname = browser.find_element_by_id('firstName')
# fill field
firstname.send_keys('Hiromi')
# scrape from last name field
lastname = browser.find_element_by_id('lastName')
lastname.send_keys('Cota')
username = browser.find_element_by_id('username')
username.send_keys('Dudeface McExample')
passwd = browser.find_element_by_id('Passwd')
passwd.send_keys('That\'s the combination to my luggage.')
passwd = browser.find_element_by_id('ConfirmPasswd')
passwd.send_keys('That\'s the combination to my luggage.')