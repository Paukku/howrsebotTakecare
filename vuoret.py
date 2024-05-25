import time
import random
import selenium


def sleep():
    time.sleep(random.uniform(0.29, 0.41))

def puolituntia(driver):
    # Kouluttaa vuorta
    klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div[2]/a[@id='boutonBalade-montagne']")
    klik.click()
    sleep()
    klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr/td/div[@id='walkmontagneSlider']/ol/li[2]")
    klik.click()
    sleep()
    klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr[2]/td/button")
    klik.click()
    sleep()

def tunti(driver):
    # Kouluttaa vuorta
    klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div[2]/a[@id='boutonBalade-montagne']")
    klik.click()
    sleep()
    klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr/td/div[@id='walkmontagneSlider']/ol/li[3]")
    klik.click()
    sleep()
    klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr[2]/td/button")
    klik.click()
    sleep()

def puolitoista(driver):
    # Kouluttaa vuorta
    klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div[2]/a[@id='boutonBalade-montagne']")
    klik.click()
    sleep()
    klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr/td/div[@id='walkmontagneSlider']/ol/li[4]")
    klik.click()
    sleep()
    klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr[2]/td/button")
    klik.click()
    sleep()

def kaksi(driver):
    # Kouluttaa vuorta
    klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div[2]/a[@id='boutonBalade-montagne']")
    klik.click()
    sleep()
    klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr/td/div[@id='walkmontagneSlider']/ol/li[5]")
    klik.click()
    sleep()
    klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr[2]/td/button")
    klik.click()
    sleep()

def kaksipuoli(driver):
    # Kouluttaa vuorta
    klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div[2]/a[@id='boutonBalade-montagne']")
    klik.click()
    sleep()
    klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr/td/div[@id='walkmontagneSlider']/ol/li[6]")
    klik.click()
    sleep()
    klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr[2]/td/button")
    klik.click()
    sleep()

def kolme(driver):
    # Kouluttaa vuorta
    klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div[2]/a[@id='boutonBalade-montagne']")
    klik.click()
    sleep()
    klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr/td/div[@id='walkmontagneSlider']/ol/li[7]")
    klik.click()
    sleep()
    klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr[2]/td/button")
    klik.click()
    sleep()

def kolmepuoli(driver):
    # Kouluttaa vuorta
    klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div[2]/a[@id='boutonBalade-montagne']")
    klik.click()
    sleep()
    klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr/td/div[@id='walkmontagneSlider']/ol/li[8]")
    klik.click()
    sleep()
    klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr[2]/td/button")
    klik.click()
    sleep()

def nelja(driver):
    # Kouluttaa vuorta
    klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div[2]/a[@id='boutonBalade-montagne']")
    klik.click()
    sleep()
    klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr/td/div[@id='walkmontagneSlider']/ol/li[9]")
    klik.click()
    sleep()
    klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr[2]/td/button")
    klik.click()
    sleep()

def neljapuoli(driver):
    # Kouluttaa vuorta
    klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div[2]/a[@id='boutonBalade-montagne']")
    klik.click()
    sleep()
    klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr/td/div[@id='walkmontagneSlider']/ol/li[10]")
    klik.click()
    sleep()
    klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr[2]/td/button")
    klik.click()
    sleep()

def viisi(driver):
    # Kouluttaa vuorta
    klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div[2]/a[@id='boutonBalade-montagne']")
    klik.click()
    sleep()
    klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr/td/div[@id='walkmontagneSlider']/ol/li[11]")
    klik.click()
    sleep()
    klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr[2]/td/button")
    klik.click()
    sleep()

def viisipuoli(driver):
    # Kouluttaa vuorta
    klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div[2]/a[@id='boutonBalade-montagne']")
    klik.click()
    sleep()
    klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr/td/div[@id='walkmontagneSlider']/ol/li[12]")
    klik.click()
    sleep()
    klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr[2]/td/button")
    klik.click()
    sleep()

def kuusi(driver):
    # Kouluttaa vuorta
    klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div[2]/a[@id='boutonBalade-montagne']")
    klik.click()
    sleep()
    klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr/td/div[@id='walkmontagneSlider']/ol/li[13]")
    klik.click()
    sleep()
    klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr[2]/td/button")
    klik.click()
    sleep()

def kuusipuoli(driver):
    # Kouluttaa vuorta
    klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div[2]/a[@id='boutonBalade-montagne']")
    klik.click()
    sleep()
    klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr/td/div[@id='walkmontagneSlider']/ol/li[14]")
    klik.click()
    sleep()
    klik = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr[2]/td/button")
    klik.click()
    sleep()
