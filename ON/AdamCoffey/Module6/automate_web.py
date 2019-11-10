from selenium import webdriver


browser = webdriver.Chrome()
browser.get('https://accounts.google.com/signup')
# find input id="firstName" and fill "Thomas" as firstname
firstname = browser.find_element_by_id('firstName')
firstname.send_keys('Thomas')
# find input id="lastName" and fill "Anderson" as lastname
lastname = browser.find_element_by_id('lastName')
lastname.send_keys('Anderson')
# find input id="username" and fill "Neo" as username
username = browser.find_element_by_id('username')
udername.send_keys('Neo')
# find input name="Passwd" and fill "noP@ssw0rd"
passwd = browser.find_element_by_name('Passwd')
passwd.send_keys('noP@ssw0rd')
# find input name="ConfirmPasswd" and fill "noP@ssw0rd" in a confirm box
passwd = browser.find_element_by_name('ConfirmPasswd')
passwd.send_keys('noP@ssw0rd')