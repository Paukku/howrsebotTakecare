
import random
import time

def findfeedblup(driver, need):
    random_time()
    hoida = driver.find_element_by_id("boutonNourrir")
    hoida.click()
    random_time()

    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']//table/tbody/tr[2]/td/form//div/div/div/span/span[2][contains(text(), Varoitus']")
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[20]").click()
        random_time()
    except:
        pass

    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'3')]")
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[4]").click()
        random_time()
    except:
        pass


    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'5')]")
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[6]").click()
        random_time()
    except:
        pass

    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'6')]")
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[7]").click()
        random_time()
    except:
        pass

    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'7')]")
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[8]").click()
        random_time()
    except:
        pass

    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'8')]")
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[9]").click()
        random_time()
    except:
        pass

    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'9')]")
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[10]").click()
        random_time()
    except:
        pass

    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'10')]")
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[11]").click()
        random_time()

    except:
        pass

    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'11')]")
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[12]").click()
        random_time()
    except:
        pass

    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'12')]")
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[13]").click()
        random_time()
    except:
        pass

    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'13')]")
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[14]").click()
        random_time()
    except:
        pass

    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'14')]")
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[15]").click()
        random_time()
    except:
        pass

    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'15')]")
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[16]").click()
        random_time()

    except:
        pass

    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'16')]")
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[17]").click()
        random_time()
    except:
        pass

    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'17')]")
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[18]").click()
        random_time()
    except:
        pass

    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'18')]")
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[19]").click()
        random_time()
    except:
        pass

    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'19')]")
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[20]").click()
        random_time()
    except:
        pass

    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'20')]")
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[21]").click()
        random_time()
    except:
        pass
    try:
        if(need==2):
            driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[3]").click()
            random_time()

        if (need == 7):
            driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[8]").click()
            random_time()

        if (need == 8):
            driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[9]").click()
            random_time()

        if (need == 9):
            driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[10]").click()
            random_time()

        if(need == 10):
            driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[11]").click()
            random_time()

        if (need == 11):
            driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[12]").click()
            random_time()

        if(need == 12):
            driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[12]").click()
            random_time()

        if (need == 13):
            driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[14]").click()
            random_time()

        if(need == 15):
            driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[16]").click()
            random_time()

    except:
        input("Ruoki hepo, en voinut itse. Älä paina ruokintanappia kuitenkaan! Laita vaan oikeisiin kohti ruokkimiset")

    driver.find_element_by_id("feed-button").click()
    random_time()





def findfeed(driver):
    try:
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']//table/tbody/tr[2]/td/form//div/div/div/span/span[2][contains(text(), Varoitus']")
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[20]")
        hoito.click()
        random_time()
        driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[4]").click()
        random_time()
        hoito = driver.find_element_by_id("feed-button")
        hoito.click()
    except:
        pass

    try:
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'3')]")
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[4]")
        hoito.click()
        random_time()
        driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[4]").click()
        random_time()
        hoito = driver.find_element_by_id("feed-button")
        hoito.click()
    except:
        pass


    try:
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'5')]")
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[6]")
        hoito.click()
        random_time()
        driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[4]").click()
        random_time()
        hoito = driver.find_element_by_id("feed-button")
        hoito.click()
    except:
        pass

    try:
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'6')]")
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[7]")
        hoito.click()
        random_time()
        driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[4]").click()
        random_time()
        hoito = driver.find_element_by_id("feed-button")
        hoito.click()
    except:
        pass

    try:
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'7')]")
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[8]")
        hoito.click()
        random_time()
        driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[4]").click()
        random_time()
        hoito = driver.find_element_by_id("feed-button")
        hoito.click()
    except:
        pass

    try:
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'8')]")
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[9]")
        hoito.click()
        random_time()
        driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[4]").click()
        random_time()
        hoito = driver.find_element_by_id("feed-button")
        hoito.click()
    except:
        pass

    try:
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'9')]")
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[10]")
        hoito.click()
        random_time()
        driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[4]").click()
        random_time()
        hoito = driver.find_element_by_id("feed-button")
        hoito.click()
    except:
        pass

    try:
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'10')]")
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[11]")
        hoito.click()
        random_time()
        driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[4]").click()
        random_time()
        hoito = driver.find_element_by_id("feed-button")
        hoito.click()
    except:
        pass

    try:
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'11')]")
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[12]")
        hoito.click()
        random_time()
        driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[4]").click()
        random_time()
        hoito = driver.find_element_by_id("feed-button")
        hoito.click()
    except:
        pass

    try:
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'12')]")
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[13]")
        hoito.click()
        random_time()
        driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[4]").click()
        random_time()
        hoito = driver.find_element_by_id("feed-button")
        hoito.click()
    except:
        pass

    try:
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'13')]")
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[14]")
        hoito.click()
        random_time()
        driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[4]").click()
        random_time()
        hoito = driver.find_element_by_id("feed-button")
        hoito.click()
    except:
        pass

    try:
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'14')]")
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[15]")
        hoito.click()
        random_time()
        driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[4]").click()
        random_time()
        hoito = driver.find_element_by_id("feed-button")
        hoito.click()
    except:
        pass

    try:
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'15')]")
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[16]")
        hoito.click()
        random_time()
        driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[4]").click()
        random_time()
        hoito = driver.find_element_by_id("feed-button")
        hoito.click()
    except:
        pass

    # try:
    #     hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'16')]")
    #     hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[17]")
    #     hoito.click()
    #     random_time()
    #     driver.find_element_by_xpath(
    #         "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[4]").click()
    #     random_time()
    #     hoito = driver.find_element_by_id("feed-button")
    #     hoito.click()
    # except:
    #     pass
    #
    # try:
    #     hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'17')]")
    #     hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[18]")
    #     hoito.click()
    #     random_time()
    #     driver.find_element_by_xpath(
    #         "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[4]").click()
    #     random_time()
    #     hoito = driver.find_element_by_id("feed-button")
    #     hoito.click()
    # except:
    #     pass
    #
    # try:
    #     hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'18')]")
    #     hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[19]")
    #     hoito.click()
    #     random_time()
    #     driver.find_element_by_xpath(
    #         "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[4]").click()
    #     random_time()
    #     hoito = driver.find_element_by_id("feed-button")
    #     hoito.click()
    # except:
    #     pass
    #
    # try:
    #     hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'19')]")
    #     hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[20]")
    #     hoito.click()
    #     random_time()
    #     driver.find_element_by_xpath(
    #         "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[4]").click()
    #     random_time()
    #     hoito = driver.find_element_by_id("feed-button")
    #     hoito.click()
    # except:
    #     pass
    #
    # try:
    #     hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'20')]")
    #     hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[21]")
    #     hoito.click()
    #     random_time()
    #     driver.find_element_by_xpath(
    #         "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[4]").click()
    #     random_time()
    #     hoito = driver.find_element_by_id("feed-button")
    #     hoito.click()
    # except:
    #     pass


def findfeedlow(driver):
    try:
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']//table/tbody/tr[2]/td/form//div/div/div/span/span[2][contains(text(), Varoitus']")
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[20]")
        hoito.click()
        random_time()
        driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[7]").click()
        random_time()
        hoito = driver.find_element_by_id("feed-button")
        hoito.click()
    except:
        pass

    try:
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'3')]")
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[4]")
        hoito.click()
        random_time()
        driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[7]").click()
        random_time()
        hoito = driver.find_element_by_id("feed-button")
        hoito.click()
    except:
        pass


    try:
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'5')]")
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[6]")
        hoito.click()
        random_time()
        driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[7]").click()
        random_time()
        hoito = driver.find_element_by_id("feed-button")
        hoito.click()
    except:
        pass

    try:
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'6')]")
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[7]")
        hoito.click()
        random_time()
        driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[7]").click()
        random_time()
        hoito = driver.find_element_by_id("feed-button")
        hoito.click()
    except:
        pass

    try:
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'7')]")
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[8]")
        hoito.click()
        random_time()
        driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[7]").click()
        random_time()
        hoito = driver.find_element_by_id("feed-button")
        hoito.click()
    except:
        pass

    try:
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'8')]")
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[9]")
        hoito.click()
        random_time()
        driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[7]").click()
        random_time()
        hoito = driver.find_element_by_id("feed-button")
        hoito.click()
    except:
        pass

    try:
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'9')]")
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[10]")
        hoito.click()
        random_time()
        driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[7]").click()
        random_time()
        hoito = driver.find_element_by_id("feed-button")
        hoito.click()
    except:
        pass

    try:
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'10')]")
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[11]")
        hoito.click()
        random_time()
        driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[7]").click()
        random_time()
        hoito = driver.find_element_by_id("feed-button")
        hoito.click()
    except:
        pass

    try:
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'11')]")
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[12]")
        hoito.click()
        random_time()
        driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[7]").click()
        random_time()
        hoito = driver.find_element_by_id("feed-button")
        hoito.click()
    except:
        pass

    try:
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'12')]")
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[13]")
        hoito.click()
        random_time()
        driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[7]").click()
        random_time()
        hoito = driver.find_element_by_id("feed-button")
        hoito.click()
    except:
        pass

    try:
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'13')]")
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[14]")
        hoito.click()
        random_time()
        driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[7]").click()
        random_time()
        hoito = driver.find_element_by_id("feed-button")
        hoito.click()
    except:
        pass

    try:
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'14')]")
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[15]")
        hoito.click()
        random_time()
        driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[7]").click()
        random_time()
        hoito = driver.find_element_by_id("feed-button")
        hoito.click()
    except:
        pass

    try:
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'15')]")
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[16]")
        hoito.click()
        random_time()
        driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[7]").click()
        random_time()
        hoito = driver.find_element_by_id("feed-button")
        hoito.click()
    except:
        pass

    try:
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'16')]")
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[17]")
        hoito.click()
        random_time()
        driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[7]").click()
        random_time()
        hoito = driver.find_element_by_id("feed-button")
        hoito.click()
    except:
        pass

    try:
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'17')]")
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[18]")
        hoito.click()
        random_time()
        driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[7]").click()
        random_time()
        hoito = driver.find_element_by_id("feed-button")
        hoito.click()
    except:
        pass

    try:
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'18')]")
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[19]")
        hoito.click()
        random_time()
        driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[7]").click()
        random_time()
        hoito = driver.find_element_by_id("feed-button")
        hoito.click()
    except:
        pass

    try:
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'19')]")
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[20]")
        hoito.click()
        random_time()
        driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[7]").click()
        random_time()
        hoito = driver.find_element_by_id("feed-button")
        hoito.click()
    except:
        pass

    try:
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'20')]")
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[21]")
        hoito.click()
        random_time()
        driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[7]").click()
        random_time()
        hoito = driver.find_element_by_id("feed-button")
        hoito.click()
    except:
        pass


def random_time():
    time.sleep(random.uniform(0.6, 1.09))