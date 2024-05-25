import time
import random
from selenium import competition
from selenium import blupblup
from selenium import howrseblupfeed
from selenium import webdriver

def log_in():
    driver = webdriver.Chrome('C:\\Users\\Paukku\\PycharmProjects\\howrsebot\\selenium\\chromedriver')
    driver.get("http://wwww.howrse.fi")
    driver.maximize_window()
    sleep()
    driver.find_element_by_id('header-login-label').click()
    long_sleep()
    user = driver.find_element_by_id('login')
    user.send_keys('pikkukissa')
    long_sleep()
    password = driver.find_element_by_id('password')
    password.send_keys('Katti93')
    sleep()
    driver.find_element_by_id('authentificationSubmit').click()
    long_sleep()
    driver.get("https://www.howrse.fi/member/account/")
    long_sleep()
    driver.get("https://www.howrse.fi/member/account/?type=partage")

    long_sleep()
    kirjaudu = driver.find_element_by_xpath("html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/div[@id='cols-middle']/div[@id='cols-middle-margin']/section/div[@id='partage']/table[@id='table-0']/tbody/tr[2]/td[3]/button")
    kirjaudu.click()
    long_sleep()
    driver.get("http://www.howrse.fi/elevage/chevaux/")
    long_sleep()
    blup(driver)

def blup(driver):
    sleep()


    #Blupattavan howrsen osoite tähän!
    driver.get('https://www.howrse.fi/elevage/chevaux/cheval?id=10548832')
    round=26
    skills = 26
    calculator = 0
    wins = 0

    while (round < 7):
        sleep()
        blupblup.hoida(driver)
        sleep()
        howrseblupfeed.findfeed(driver, 0)
        sleep()
        age(driver)
        sleep()
        round = round +1

    while(round < 10):
        blupblup.blup_metsa_alle2v(driver)
        sleep()
        age(driver)
        sleep()
        round = round +1

    # blupblup.blup_2v(driver)
    # sleep()
    # age(driver)
    # round = round + 1
    # sleep()
    # blupblup.blup_ravi_2v2k(driver)
    # sleep()
    # age(driver)
    # round = round + 1
    # sleep()
    # blupblup.blup_ravi_2v4k(driver)
    # sleep()
    # age(driver)
    # round = round + 1

    while (round < 16):
        blupblup.kouluta_nopeus_2v(driver)
        sleep()
        age(driver)
        sleep()
        round = round +1

    print("Odotan varustusten laittoa")
    time.sleep(65)

    #VARUSTUS JA ERIKOISTUMINEN LÄNNENRATSASTUKSEEN

    #TARKISTA MONTA KISAA ON?
    #KISAUTUS -> taitojen haku


    while(skills < 25):
        blupblup.hoida(driver)
        sleep()
        if(calculator == 0):
            competition.trail(driver)
            sleep()
            howrseblupfeed.findfeed(driver, 10)
            sleep()
            calculator = calculator + 1
            print("käyn ruokkimassa")

        if(calculator < 7):
            competition.trail(driver)
            sleep()
            calculator = calculator + 1
            sleep()
            print("kisat", calculator)


        if(calculator == 7):
            blupblup.anna_herkut(driver)
            sleep()
            age(driver)
            sleep()
            calculator = 0
            print("kisat", calculator)




        skills = skills + 1


    print("Odotan että erikoistuminen vaihtuu")
    time.sleep(5)

    # competition.maasto(driver)
    # sleep()
    # competition.maasto(driver)
    # sleep()
    # age(driver)
    # sleep()
    wins = 21

    calculator = 0

    while (wins < 20):
        blupblup.hoida(driver)
        sleep()
        if (calculator == 0):
            competition.maasto(driver)
            sleep()
            howrseblupfeed.findfeed(driver, 10)
            sleep()
            print("Kävin täällä")
            calculator = calculator + 1
            wins = wins + 1


        if(calculator < 7):
            print("kisat", calculator)
            competition.maasto(driver)
            sleep()
            calculator = calculator + 1
            wins = wins + 1


        if (calculator == 7):
            blupblup.anna_herkut(driver)
            sleep()
            age(driver)
            sleep()
            calculator = 0
            round = round + 1
            sleep()




    time.sleep(120)
    blupblup.anna_herkut(driver)
    age(driver)
    round = round + 1

    # sleep()
    # blupblup.metstat_4v(driver)
    # sleep()
    # age(driver)
    # sleep()
    # round = round +1
    # sleep()
    # blupblup.metstat_4v(driver)
    # sleep()
    # age(driver)
    # sleep()
    # round = round + 1
    # sleep()
    # blupblup.metstat_ja_koulu_4v(driver)
    # sleep()
    # age(driver)
    # sleep()
    # round = round + 1


    while(round < 30):
        blupblup.koulutakoulu(driver)
        sleep()
        age(driver)
        sleep()
        round = round+1

    while(round < 33):
        blupblup.blup_ravi_2v2k(driver)
        sleep()
        age(driver)
        sleep()
        round = round +1

    while(round < 37):
        blupblup.koulutaeste(driver)
        sleep()
        age(driver)
        sleep()
        round = round +1

    while(round < 48):
        blupblup.kouluta_vuoret(driver)
        sleep()
        age(driver)
        sleep()
        round = round +1

    sleep()
    # blupblup.kouluta_vuoretjaeste(driver)
    sleep()
    age(driver)
    sleep()
    sleep()

    #Astuttaa tamman
    driver.find_element_by_xpath("div[@id='reproduction-tab-0']/table/tbody/tr/td[3]/a").click()
    sleep()
    driver.find_element_by_xpath("section[@id='page-contents']/div[@id='resultatsRecherche']/div/ul/li[2]/div/a").click()
    sleep()
    driver.find_element_by_xpath("section[@id='page-contents']/div[@id='resultatsRecherche']/table/tbody/tr/td[8]/a").click()
    sleep()
    driver.find_element_by_id("boutonDoReproduction").click()
    sleep()
    howrseblupfeed.findfeed(driver, 2)
    sleep()
    blupblup.hoida(driver)
    sleep()
    age(driver)
    i = 0
    while(i<5):
        howrseblupfeed.findfeed(driver, 2)
        sleep()
        blupblup.hoida(driver)
        sleep()
        age(driver)
        sleep()
        i = i+1

    driver.find_element_by_id("boutonEchographie").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-right']/div[5]/div[1]/div[1]//div[1]/div[1]/div[@id='reproduction-body-content']/div[1]/div[1]/table/tbody/tr[2]/td/div/table/tbody/tr/td[2](text(),'1 orivarsa rotu:')]")
    sleep()


    time.sleep(600)





def sleep():
    time.sleep(random.uniform(0.87, 1.29))

def long_sleep():
    time.sleep(random.uniform(5.75, 12.103))

def age(driver):
    driver.find_element_by_id("boutonVieillir").click()
    sleep()
    driver.find_element_by_xpath("/html/body/div[@id='container']/main[@id='content']/div[@id='cols-wrapper']/section[@id='page-contents']/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]/div[2]/div[@id='night-body-content']/div[@id='night-wrapper']/div[@id='night-tab-age']/table/tbody/tr[2]/td/form/div/button").click()
    sleep()

if __name__ == "__main__":
    log_in()
    exit()
