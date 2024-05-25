from selenium import chrome
import time
import random
from selenium import howrseblupfeed

def blup_metsa_alle2v(driver):
    #koulutus 1h
    hoida(driver)
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[1]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div/a[@id='boutonBalade-foret']").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[1]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr/td/div[@id='walkforetSlider']/ol/li[3]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[1]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr[2]/td/button").click()
    sleep()
    #hoida ja ruoki. kauraa 12 kpl heinä se mitä suosittelee
    hoida(driver)
    sleep()
    need = 10
    howrseblupfeed.findfeed(driver, need)
    sleep()

    #Kouluta öö.. 5.5h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[1]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div/a[@id='boutonBalade-foret']").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[1]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr/td/div[@id='walkforetSlider']/ol/li[12]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[1]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr[2]/td/button").click()
    sleep()

    #Silitys, porkkana, vesi, mahdollisesti ape.
    anna_herkut(driver)
    sleep()

    # Kouluta 1 tuntia?
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[1]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div/a[@id='boutonBalade-foret']").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[1]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr/td/div[@id='walkforetSlider']/ol/li[2]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[1]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr[2]/td/button").click()
    sleep()


def blup_2v(driver):
    # koulutus 1.5h
    hoida(driver)
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div/a[@id='boutonBalade-foret']").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr/td/div[@id='walkforetSlider']/ol/li[4]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr[2]/td/button").click()
    sleep()

    # hoida ja ruoki. kauraa 15 kpl heinä se mitä suosittelee
    hoida(driver)
    sleep()
    need = 15
    howrseblupfeed.findfeed(driver, need)
    sleep()

    # koulutus 2h metsä
    hoida(driver)
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div/a[@id='boutonBalade-foret']").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr/td/div[@id='walkforetSlider']/ol/li[5]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr[2]/td/button").click()
    sleep()

    #kouluta este 6h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[6]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[14]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

    # Silitys, porkkana, vesi, mahdollisesti ape.
    anna_herkut(driver)
    sleep()

    # Kouluta este 1h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[6]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[3]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

def blup_ravi_2v2k(driver):
    # Kouluttaa ravia 2h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[5]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[5]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

    hoida(driver)
    sleep()
    need = 15
    howrseblupfeed.findfeed(driver, need)
    sleep()

    #kouluta 7,5h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[5]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[16]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

    anna_herkut(driver)
    sleep()

    # Kouluttaa ravia 1,5h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[5]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[4]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

def blup_ravi_2v4k(driver):
    # Kouluttaa ravia 2h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[5]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[5]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

    hoida(driver)
    need = 15
    howrseblupfeed.findfeed(driver, need)
    sleep()

    # Kouluttaa ravia 2h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[5]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[5]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-trot']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

    #kouluta nopeutta 4.5h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[2]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-vitesse']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[10]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-vitesse']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

    anna_herkut(driver)
    sleep()

    #kouluta nopeutta 1,5h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[2]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-vitesse']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[4]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-vitesse']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

def kouluta_nopeus_2v(driver):
    # kouluta nopeutta 2h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[2]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-vitesse']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[5]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-vitesse']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

    hoida(driver)
    need = 15
    howrseblupfeed.findfeed(driver, need)
    sleep()

    # kouluta nopeutta 6h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[2]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-vitesse']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[13]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-vitesse']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

    anna_herkut(driver)
    sleep()

    # kouluta nopeutta 1,5h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[2]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-vitesse']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[4]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-vitesse']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

#kisautus 3v-4v

def metstat_4v(driver):
    # koulutus 1.5h
    hoida(driver)
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div/a[@id='boutonBalade-foret']").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr/td/div[@id='walkforetSlider']/ol/li[3]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr[2]/td/button").click()
    sleep()

    # hoida ja ruoki. kauraa 12 kpl heinä se mitä suosittelee
    hoida(driver)
    need = 12
    howrseblupfeed.findfeed(driver, need)
    sleep()

    # Kouluta 6h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div/a[@id='boutonBalade-foret']").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr/td/div[@id='walkforetSlider']/ol/li[13]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr[2]/td/button").click()
    sleep()

    # Silitys, porkkana, vesi, mahdollisesti ape.
    anna_herkut(driver)
    sleep()

    # Kouluta 2 tuntia
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div/a[@id='boutonBalade-foret']").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr/td/div[@id='walkforetSlider']/ol/li[5]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr[2]/td/button").click()
    sleep()

def metstat_ja_koulu_4v(driver):
    # koulutus 1.5h
    hoida(driver)
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div/a[@id='boutonBalade-foret']").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr/td/div[@id='walkforetSlider']/ol/li[3]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr[2]/td/button").click()
    sleep()

    # hoida ja ruoki. kauraa 12 kpl heinä se mitä suosittelee
    hoida(driver)
    need = 12
    howrseblupfeed.findfeed(driver, need)
    sleep()

    # Kouluta 6h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div/a[@id='boutonBalade-foret']").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr/td/div[@id='walkforetSlider']/ol/li[13]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr[2]/td/button").click()
    sleep()

    # Silitys, porkkana, vesi, mahdollisesti ape.
    anna_herkut(driver)
    sleep()

    # Kouluta 2 tuntia
    driver.find_element_by_xpath("html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[3]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-dressage']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[5]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-dressage']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

def koulutakoulu(driver):
    # Kouluta 2 tuntia
    driver.find_element_by_xpath("html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[3]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-dressage']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[5]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-dressage']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

    # hoida ja ruoki. kauraa 12 kpl heinä se mitä suosittelee
    hoida(driver)
    need = 10
    howrseblupfeed.findfeed(driver, need)
    sleep()

    # Kouluta 2 tuntia
    driver.find_element_by_xpath("html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[3]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-dressage']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[18]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-dressage']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

    anna_herkut(driver)
    sleep()

    # Kouluta 2 tuntia
    driver.find_element_by_xpath("html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[3]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-dressage']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[5]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-dressage']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

def koulutaeste(driver):
    # Kouluttaa estettä 2h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[6]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[5]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

    # hoida ja ruoki. kauraa 12 kpl heinä se mitä suosittelee
    hoida(driver)
    need = 15
    howrseblupfeed.findfeed(driver, need)
    sleep()

    # Kouluttaa estettä 6h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[6]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[16]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

    anna_herkut(driver)
    sleep()

    # Kouluttaa estettä 1,5h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div/div/table/tbody/tr[6]/td[3]/button").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr/td/div[2]/ol/li[4]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-saut']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()

def kouluta_vuoret(driver):
    # Kouluttaa vuorta 1,5h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div[2]/a[@id='boutonBalade-montagne']").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr/td/div[@id='walkmontagneSlider']/ol/li[4]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr[2]/td/button").click()
    sleep()

    # hoida ja ruoki. kauraa 12 kpl heinä se mitä suosittelee
    hoida(driver)
    need = 15
    howrseblupfeed.findfeed(driver, need)
    sleep()

    # Kouluttaa vuorta 6h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div[2]/a[@id='boutonBalade-montagne']").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr/td/div[@id='walkmontagneSlider']/ol/li[12]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr[2]/td/button").click()
    sleep()

    anna_herkut(driver)
    sleep()

    # Kouluttaa vuorta 1.5h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div[2]/a[@id='boutonBalade-montagne']").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr/td/div[@id='walkmontagneSlider']/ol/li[4]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr[2]/td/button").click()
    sleep()

def kouluta_vuoretjaeste(driver):
    # Kouluttaa vuorta 1,5h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div[2]/a[@id='boutonBalade-montagne']").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr/td/div[@id='walkmontagneSlider']/ol/li[4]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr[2]/td/button").click()
    sleep()

    # hoida ja ruoki. kauraa 12 kpl heinä se mitä suosittelee
    hoida(driver)
    need = 15
    howrseblupfeed.findfeed(driver, need)
    sleep()

    # Kouluttaa vuorta 6h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div[2]/a[@id='boutonBalade-montagne']").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr/td/div[@id='walkmontagneSlider']/ol/li[13]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[2]/div[1]/div[1]/div[1]/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-montagne']/table/tbody/tr[2]/td/form/div[@id='walk-montagne-form']/div[@id='walk-montagne-form']/table/tbody/tr[2]/td/button").click()
    sleep()

    anna_herkut(driver)
    sleep()

    # Kouluttaa estettä 2h
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-main']/div/div/div/a[@id='boutonBalade-foret']").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='walk']/div[@id='walk-body-content']/div[@id='walk-wrapper']/div[@id='walk-tab-balade-foret']/table/tbody/tr[2]/td/form/div[@id='walk-foret-form']/div[@id='walk-foret-form']/table/tbody/tr/td/div[@id='walkforetSlider']/ol/li[5]").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[3]/div[1]/div[1]/div[@id='training']/div[@id='training-body-content']/div[@id='training-wrapper']/div[@id='training-tab-sout']/table/tbody/tr[2]/td/div/div/form/table/tbody/tr[2]/td/button").click()
    sleep()


def hoida(driver):
    #laita nukkumaan, hoida
    driver.find_element_by_id("boutonPanser").click()
    sleep()
    driver.find_element_by_id("boutonCoucher").click()
    sleep()



def anna_herkut(driver):
    # Silitys, vesi, porkkana, ape
    driver.find_element_by_id("boutonCaresser").click()
    sleep()
    driver.find_element_by_id("boutonBoire").click()
    sleep()
    driver.find_element_by_id("boutonCarotte").click()
    sleep()
    driver.find_element_by_id("boutonMash").click()
    sleep()

def sleep():
    time.sleep(random.uniform(0.87, 2.09))
