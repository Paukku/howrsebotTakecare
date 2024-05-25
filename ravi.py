import time
import random
import selenium


def sleep():
    time.sleep(random.uniform(0.28, 0.40))

def puoli(driver):
    # Kouluttaa ravia 2h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[5]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[2]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

def tunti(driver):
    # Kouluttaa ravia 2h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[5]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[3]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

def puolitoista(driver):
    # Kouluttaa ravia 2h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[5]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[4]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

def kaksi(driver):
    # Kouluttaa ravia 2h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[5]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[5]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

def kaksipuoli(driver):
    # Kouluttaa ravia 2h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[5]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[6]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

def kolme(driver):
    # Kouluttaa ravia 2h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[5]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[7]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

def kolmepuoli(driver):
    # Kouluttaa ravia 2h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[5]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[8]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

def nelja(driver):
    # Kouluttaa ravia 2h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[5]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[9]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

def neljapuoli(driver):
    # Kouluttaa ravia 2h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[5]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[10]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

def viis(driver):
    # Kouluttaa ravia 2h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[5]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[11]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

def viisipuoli(driver):
    # Kouluttaa ravia 2h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[5]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[12]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

def kuusi(driver):
    # Kouluttaa ravia 2h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[5]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[13]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

def kuusipuoli(driver):
    # Kouluttaa ravia 2h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[5]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[14]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

def seitseman(driver):
    # Kouluttaa ravia 2h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[5]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[15]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

def seitsemanpuoli(driver):
    # Kouluttaa ravia 2h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[5]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[16]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

def kahdeksan(driver):
    # Kouluttaa ravia 2h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[5]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[17]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()