import time
import random
import selenium


def sleep():
    time.sleep(random.uniform(0.28, 0.40))

def puolituntia(driver):
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[6]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[2]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

def tunti(driver):
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[6]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[3]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

def puolitoista(driver):
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[6]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[4]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

def kaksi(driver):
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[6]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[5]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

def kaksipuoli(driver):
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[6]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[6]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

def kolme(driver):
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[6]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[7]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

def kolmepuoli(driver):
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[6]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[8]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

def nelja(driver):
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[6]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[9]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

def neljapuoli(driver):
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[6]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[10]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

def viisi(driver):
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[6]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[11]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

def viisipuoli(driver):
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[6]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[12]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

def kuusi(driver):
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[6]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[13]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

def kuusipuoli(driver):
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[6]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[14]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

def seitseman(driver):
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[6]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[15]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

def seitsemanpuoli(driver):
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[6]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[16]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

def kahdeksan(driver):
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[6]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[17]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

def kahdeksanpuoli(driver):
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[6]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[18]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()