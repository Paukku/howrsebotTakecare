    from selenium import webdriver

    browser = webdriver.Chrome("C:\Users\Paukku\Desktop\selenium-3.8.0\selenium\chromedriver.exe")
    browser.get('http://seleniumhq.org/')
	browser.maximize_window()