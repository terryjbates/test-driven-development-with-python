from selenium import webdriver 
browser = webdriver.Chrome()
browser.get('http://localhost:5000') 
assert 'tdd_with_python' in browser.title
