from selenium import webdriver
import random
import time

def findfeed(driver, need):
    hoida = driver.find_element_by_id("boutonNourrir")
    hoida.click()
    random_time()

    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']//table/tbody/tr[2]/td/form//div/div/div/span/span[2][contains(text(), Varoitus']")
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[20]").click()
        random_time()
    except:
        pass

    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'3')]")
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[4]").click()
        random_time()
    except:
        pass


    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'5')]")
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[6]").click()
        random_time()
    except:
        pass

    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'6')]")
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[7]").click()
        random_time()
    except:
        pass

    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'7')]")
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[8]").click()
        random_time()
    except:
        pass

    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'8')]")
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[9]").click()
        random_time()
    except:
        pass

    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'9')]")
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[10]").click()
        random_time()
    except:
        pass

    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'10')]")
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[11]").click()
        random_time()

    except:
        pass

    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'11')]")
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[12]").click()
        random_time()
    except:
        pass

    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'12')]")
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[13]").click()
        random_time()
    except:
        pass

    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'13')]")
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[14]").click()
        random_time()
    except:
        pass

    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'14')]")
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[15]").click()
        random_time()
    except:
        pass

    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'15')]")
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[16]").click()
        random_time()

    except:
        pass

    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'16')]")
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[17]").click()
        random_time()
    except:
        pass

    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'17')]")
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[18]").click()
        random_time()
    except:
        pass

    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'18')]")
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[19]").click()
        random_time()
    except:
        pass

    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'19')]")
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[20]").click()
        random_time()
    except:
        pass

    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'20')]")
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[21]").click()
        random_time()
    except:
        pass

    if(need==2):
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[3]").click()
        random_time()

    if(need == 10):
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[11]").click()
        random_time()

    if(need == 12):
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[13]").click()
        random_time()

    if(need == 15):
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[14]").click()
        random_time()

    driver.find_element_by_id("feed-button").click()





def random_time():
    time.sleep(random.uniform(0.6, 1.09))