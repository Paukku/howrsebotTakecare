
import time
import random


def metsa(driver):
    #Kouluttaa metsää 5h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div/a[@id='boutonBalade-foret']").click()
    sleep()

    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr/td/div[@id='walkforetSlider']/ol/li[11]").click()
    sleep()

    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr[2]/td/button").click()
    sleep()
    perushoito(driver)

def vuori(driver):
    # Kouluttaa vuorta 5h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div[2]/a[@id='boutonBalade-montagne']").click()
    sleep()

    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr/td/div[@id='walkmontagneSlider']/ol/li[11]").click()
    sleep()

    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr[2]/td/button").click()
    sleep()
    perushoito(driver)


def kestavyys(driver):
    #Kouluttaa kestävyyttä 5h 30min
    klick = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr/td[3]/button")
    klick.click()
    sleep()

    klick = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-endurance']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[12]")
    klick.click()
    sleep()

    klick = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-endurance']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button")
    klick.click()
    sleep()
    perushoito(driver)


def nopeus(driver):
    #Kouluttaa nopeutta 5h 30min
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[2]/td[3]/button").click()
    sleep()

    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-vitesse']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[12]").click()
    sleep()

    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-vitesse']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

    perushoito(driver)

def koulu(driver):
    #Kouluttaa koulus 8h
    klick = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[3]/td[3]/button")
    klick.click()
    sleep()

    klick = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-dressage']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[18]")
    klick.click()
    sleep()

    klick = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-dressage']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button")
    klick.click()
    sleep()

    perushoito(driver)

def laukka(driver):
    #Kouluttaa laukkas 6h
    klick = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[4]/td[3]/button")
    klick.click()
    sleep()

    klick = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[13]")
    klick.click()
    sleep()

    klick = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-galop']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button")
    klick.click()
    sleep()

    perushoito(driver)


def ravi(driver):
    # Kouluttaa ravia 6h
    klick = driver.find_element_by_xpath(
        "/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[5]/td[3]/button")
    klick.click()
    sleep()

    klick = driver.find_element_by_xpath(
        "/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[13]")
    klick.click()
    sleep()

    klick = driver.find_element_by_xpath(
        "/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button")
    klick.click()
    sleep()

    perushoito(driver)


def este(driver):
    # Kouluttaa estettä 6h
    klick = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[6]/td[3]/button")
    klick.click()
    sleep()

    klick = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[13]")
    klick.click()
    sleep()

    klick = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button")
    klick.click()
    sleep()

    perushoito(driver)

def perushoito(driver):

    #Silitys ja vesi
    hoito = driver.find_element_by_id("boutonCaresser")
    hoito.click()
    sleep()
    hoito = driver.find_element_by_id("boutonBoire")
    hoito.click()
    sleep()

   #Ruokkiminen
    hoito = driver.find_element_by_id("boutonPanser")
    hoito.click()
    sleep()
    try:
        hoito = driver.find_element_by_xpath(
            "/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[1]/div[1]/div[1]/div[1]/div[1]/div[@id='care-wrapper']/div[@id= 'care-tab-main']/div[1]/div[1]/div[1]/a")
        hoito.click()
        sleep()
        hoito = driver.find_element_by_id("feed-button")
        hoito.click()
        sleep()
    except:
        pass


def sleep():
    time.sleep(random.uniform(0.87, 2.09))

