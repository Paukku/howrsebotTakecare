import time
import random


def trail(driver):
    try:
        sleep()
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[4]/div/div//div/div/div/table/tbody/tr[1]/td[3]/a")
        hoito.click()
        sleep()
        sleep()
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='competitionsContent']/div/div/table/tbody/tr/td[8]/button")
        hoito.click()
        sleep()
    except:
        driver.refresh()
        sleep()
        sleep()
        try:
            hoito = driver.find_element_by_xpath(
                "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[4]/div/div//div/div/div/table/tbody/tr[1]/td[3]/a")
            hoito.click()
            sleep()

            hoito = driver.find_element_by_xpath(
                "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='competitionsContent']/div/div/table/tbody/tr/td[8]/button")
            hoito.click()
            sleep()
        except:
            input("ongelma kisakohdassa")



def cutting(driver):

    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[4]/div/div//div/div/div/table/tbody/tr[1]/td[2]/a").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='competitionsContent']/div/div/table/tbody/tr/td[8]/button").click()
    sleep()


def maasto(driver):
    driver.execute_script("window.scrollTo(0, 1080)")
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[4]/div/div//div/div/div/table/tbody/tr[2]/td[1]/a").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='competitionsContent']/div/div/table/tbody/tr/td[8]/button").click()
    sleep()


def ravi(driver):
    try:
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[4]/div/div//div/div/div/table/tbody/tr[1]/td[1]/a")
        hoito.click()
        sleep()
        sleep()
        hoito = driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='competitionsContent']/div/div/table/tbody/tr/td[8]/button")
        hoito.click()
        sleep()
        sleep()
    except:
        input("ongelma kisakohdassa")


def sleep():
    time.sleep(random.uniform(0.57, 1.09))