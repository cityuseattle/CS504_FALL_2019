from selenium import webdriver

browser= webdriver.Chrome()
browser.get('http://accounts.google.com/signup')
firstname = browser.find_element_by_id('firstName')
firstname.send_keys('Thomas')

lastname = browser.find_element_by_id('firstName')
lastname.send_keys('Anderson')

username = browser.find_element_by_id('username')
username.send_keys('Neo')

passwd = browser.find_element_by_name('Passwd')
passwd.send_keys('noP@ssw0rd')

passwd = browser.find_element_by_name('ConfirmPasswd')
passwd.send_keys('noP@ssw0rd')