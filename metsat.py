import time
import random
import selenium


def sleep():
    time.sleep(random.uniform(0.29, 0.41))

def puolitunti(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div/a[@id='boutonBalade-foret']").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr/td/div[@id='walkforetSlider']/ol/li[2]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Vuoria 0.5 tuntia")

def alle2_puolitunti(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[1]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div/a[@id='boutonBalade-foret']").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[1]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr/td/div[@id='walkforetSlider']/ol/li[2]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[1]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Vuoria 0.5 tuntia")

def tunti(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div/a[@id='boutonBalade-foret']").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr/td/div[@id='walkforetSlider']/ol/li[3]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Vuoria 1 tuntia")

def alle2_puolitoista(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[1]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div/a[@id='boutonBalade-foret']").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[1]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr/td/div[@id='walkforetSlider']/ol/li[4]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[1]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Vuoria 1.5 tuntia")

def puolitoista(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div/a[@id='boutonBalade-foret']").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr/td/div[@id='walkforetSlider']/ol/li[4]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Vuoria 1.5 tuntia")

def kaksi(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div/a[@id='boutonBalade-foret']").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr/td/div[@id='walkforetSlider']/ol/li[5]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Vuoria 2 tuntia")

def kaksijapuoli(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div/a[@id='boutonBalade-foret']").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr/td/div[@id='walkforetSlider']/ol/li[6]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Vuoria 2.5 tuntia")


def kolme(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div/a[@id='boutonBalade-foret']").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr/td/div[@id='walkforetSlider']/ol/li[7]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Vuoria 3 tuntia")

def kolmejapuoli(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div/a[@id='boutonBalade-foret']").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr/td/div[@id='walkforetSlider']/ol/li[8]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Vuoria 3.5 tuntia")

def nelja(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div/a[@id='boutonBalade-foret']").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr/td/div[@id='walkforetSlider']/ol/li[9]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Vuoria 4 tuntia")

def neljajapuoli(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div/a[@id='boutonBalade-foret']").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr/td/div[@id='walkforetSlider']/ol/li[10]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Vuoria 4.5 tuntia")

def viisi(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div/a[@id='boutonBalade-foret']").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr/td/div[@id='walkforetSlider']/ol/li[11]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("metsia 5 tuntia")

def alle2_viisi(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[1]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div/a[@id='boutonBalade-foret']").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[1]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr/td/div[@id='walkforetSlider']/ol/li[11]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[1]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Vuoria 5 tuntia")

def viisijapuoli(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div/a[@id='boutonBalade-foret']").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr/td/div[@id='walkforetSlider']/ol/li[12]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Vuoria 5.5 tuntia")

def kuusi(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div/a[@id='boutonBalade-foret']").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr/td/div[@id='walkforetSlider']/ol/li[13]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Vuoria 6 tuntia")

def kuusipuoli(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div/a[@id='boutonBalade-foret']").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr/td/div[@id='walkforetSlider']/ol/li[14]").click()
        sleep()
        driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr[2]/td/button").click()
        sleep()
    except:
        input("Vuoria 6.5 tuntia")