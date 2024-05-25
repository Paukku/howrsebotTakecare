from selenium import webdriver
import random
import time
import howrsefeed
import howrsetraining
import koulu
import ravi
import este
import laukka
import nopeus
import kestavyys
import competition
import vuoret

def log_in():
    driver = webdriver.Chrome('C:\\Users\\Paula\\Desktop\\howrsebot\\sele\\chromedriver')
    driver.get("http://wwww.howrse.fi")
    driver.maximize_window()
    sleep()
    driver.find_element_by_id('header-login-label').click()
    long_sleep()
    user = driver.find_element_by_id('login')

    sleep()
    driver.find_element_by_id('authentificationSubmit').click()
    long_sleep()

    # pikkukissa(driver)
    #
    driver.get("https://www.howrse.fi/member/account/")
    driver.get("https://www.howrse.fi/member/account/?type=sharing")

    sleep()
    driver.execute_script("window.scrollTo(0, 440)")
    sleep()
    # #
    # driver.find_element_by_xpath(
    #     "html/body/div[@id='container']/main[@id='content']/section/section/div/div[@id='main-content']/div/article[2]/div/table/tbody/tr[3]/td[2]/button").click()
    # sleep()
    # anni(driver)
    # sleep()


    # driver.find_element_by_xpath(
    #   "html/body/div[@id='container']/main[@id='content']/section/section/div/div[@id='main-content']/div/article[2]/div/table/tbody/tr[1]/td[2]/button").click()
    # sleep()
    # esma(driver)
    # sleep()

    sleep()
    driver.find_element_by_xpath(
        "html/body/div[@id='container']/main[@id='content']/section/section/div/div[@id='main-content']/div/article[2]/div/table/tbody/tr[2]/td[2]/button").click()
    sleep()
    pizkunen(driver)
    sleep()
    # # # #
    sleep()
    driver.find_element_by_xpath(
        "html/body/div[@id='container']/main[@id='content']/section/section/div/div[@id='main-content']/div/article[2]/div/table/tbody/tr[4]/td[2]/button").click()
    sleep()
    ladybird(driver)
    sleep()

    driver.close()


def pikkukissa(driver):
    # sleep()
    # driver.get("http://www.howrse.fi/elevage/chevaux/")
    # sleep()
    # driver.get('https://www.howrse.fi/elevage/chevaux/cheval?id=13054022')  # 12357899
    # hoida_eiautomaatti(driver, 195)  # 260

    # sleep()
    # driver.get("http://www.howrse.fi/elevage/chevaux/")
    # sleep()
    # driver.get('https://www.howrse.fi/elevage/chevaux/cheval?id=12037910')  # 11719398
    # hoida_eiautomaatti(driver, 100) # 464

    sleep()
    driver.get("http://www.howrse.fi/elevage/chevaux/")
    sleep()
    driver.get('https://www.howrse.fi/elevage/chevaux/cheval?id=14252154')  # 14252154
    hoida_eiautomaatti(driver, 511)

    # # uloskirjautuminen
    # sleep()


def pizkunen(driver):
    # sleep()
    # driver.get("http://www.howrse.fi/elevage/chevaux/")
    # sleep()
    # driver.get('https://www.howrse.fi/elevage/chevaux/cheval?id=13054053')  # 12028618
    # pizkunen_knabet(driver, 400)  # 260

    sleep()
    driver.get("http://www.howrse.fi/elevage/chevaux/")
    sleep()
    driver.get('https://www.howrse.fi/elevage/chevaux/cheval?id=10749548') # 13303062
    hoida_eiautomaatti(driver, 810) #260

    # uloskirjautuminen
    log_out = driver.find_element_by_xpath("html/body/div[@id='container']/header/nav[1]/ul/li[3]")
    sleep()
    log_out.click()
    sleep()
    log_out = driver.find_element_by_xpath("html/body/div[@id='container']/header/nav[1]/ul/li[3]/div/ul/li[6]")
    log_out.click()
    sleep()


def esma(driver):
    # sleep()
    # driver.get("http://www.howrse.fi/elevage/chevaux/")
    # sleep()
    # driver.get('https://www.howrse.fi/elevage/chevaux/cheval?id=12814712')  #13054366
    # esma_knabet(driver, 200)

    sleep()
    driver.get("http://www.howrse.fi/elevage/chevaux/")
    sleep()
    driver.get('https://www.howrse.fi/elevage/chevaux/cheval?id=14204078') #12747880
    hoida_eiautomaatti(driver, 700) #940

    # uloskirjautuminen
    log_out = driver.find_element_by_xpath("html/body/div[@id='container']/header/nav[1]/ul/li[3]")
    sleep()
    log_out.click()
    log_out = driver.find_element_by_xpath("html/body/div[@id='container']/header/nav[1]/ul/li[3]/div/ul/li[6]")
    sleep()
    log_out.click()


def ladybird(driver):
    sleep()
    driver.get("http://www.howrse.fi/elevage/chevaux/")
    sleep()
    driver.get('https://www.howrse.fi/elevage/chevaux/cheval?id=13752691') # 13809540
    hoida_eiautomaatti(driver, 51) #260

    # uloskirjautuminen
    log_out = driver.find_element_by_xpath("html/body/div[@id='container']/header/nav[1]/ul/li[3]")
    sleep()
    log_out.click()
    sleep()
    log_out = driver.find_element_by_xpath("html/body/div[@id='container']/header/nav[1]/ul/li[3]/div/ul/li[6]")
    log_out.click()
    sleep()

def anni(driver):

    sleep()
    driver.get("http://www.howrse.fi/elevage/chevaux/")
    sleep()
    driver.get("https://www.howrse.fi/elevage/chevaux/?elevage=412622")
    sleep()
    driver.get("http://www.howrse.fi/elevage/chevaux/cheval?id=12211508") #12211508
    hoidettavia = 531
    hoida_eiautomaatti(driver, hoidettavia)
    sleep()

    # uloskirjautuminen
    log_out = driver.find_element_by_xpath("html/body/div[@id='container']/header/nav[1]/ul/li[3]")
    sleep()
    log_out.click()
    sleep()
    log_out = driver.find_element_by_xpath("html/body/div[@id='container']/header/nav[1]/ul/li[3]/div/ul/li[6]")
    log_out.click()
    sleep()


def hoida(driver, hoidettavia):
    time.sleep(2)
    hoidettu = 0
    laskuun = 0
    laske = random_heppa()
    print(laske)
    while hoidettu < hoidettavia:
        # keskus(driver)
        keskus_anni(driver)
        tehtava(driver)
        tehtava_sleep()
        hoito = driver.find_element_by_id("boutonPanser")
        hoito.click()
        sleep()
        try:
            hoito = driver.find_element_by_id("boutonNourrir")
            hoito.click()
            sleep()
            hoito = driver.find_element_by_id("feed-button")
            hoito.click()
            sleep()
        except:
            pass
            sleep()
        hoito = driver.find_element_by_id("nav-next")
        hoito.click()
        hoidettu += 1
        laskuun += 1
        laske = tarkista(laske, laskuun)


def pizkunen_knabet(driver, hoida):
    time.sleep(2)
    hoidettu = 0
    laskuun = 0
    laske = random_heppa()

    while (hoidettu < hoida):

        sleep()
        hoito = driver.find_element_by_id("boutonPanser")
        hoito.click()
        sleep()

        hoito = driver.find_element_by_id("boutonCoucher")
        hoito.click()
        sleep()

        nopeus.neljapuoli(driver)
        sleep()

        anna_herkut(driver)
        sleep()

        hoito = driver.find_element_by_id("boutonNourrir")
        hoito.click()
        sleep()


        try:
            howrsefeed.findfeedblup(driver)
            sleep()

        except:
            pass
            sleep()

        nopeus.neljapuoli(driver)
        sleep()
        hoidettu += 1
        laskuun += 1
        laske = tarkista(laske, laskuun)
        hoito = driver.find_element_by_id("nav-next")
        hoito.click()
        sleep()


def esma_knabet(driver, hoida):
    time.sleep(2)
    hoidettu = 0
    laskuun = 0
    laske = random_heppa()

    while (hoidettu < hoida):

        sleep()
        hoito = driver.find_element_by_id("boutonPanser")
        hoito.click()
        sleep()

        hoito = driver.find_element_by_id("boutonCoucher")
        hoito.click()
        sleep()

        kestavyys.viisi(driver)
        sleep()

        # anna_herkut(driver)
        # sleep()

        hoito = driver.find_element_by_id("boutonNourrir")
        hoito.click()
        sleep()


        try:
            howrsefeed.findfeedblup(driver)
            sleep()

        except:
            pass
            sleep()

        # laukka.viisi(driver)
        # sleep()
        hoidettu += 1
        laskuun += 1
        laske = tarkista(laske, laskuun)
        hoito = driver.find_element_by_id("nav-next")
        hoito.click()
        sleep()


def hoida_eiautomaatti(driver, hoida):
    time.sleep(2)
    hoidettu = 0
    laskuun = 0
    laske = random_heppa()
    while(hoidettu < hoida):
        sleep()
        # keskus_anni(driver)
        keskus_normaali(driver)
        sleep()
        tehtava(driver)
        tehtava_sleep()

        sleep()
        hoito = driver.find_element_by_id("boutonPanser")
        hoito.click()
        sleep()

        hoito = driver.find_element_by_id("boutonCoucher")
        hoito.click()
        sleep()

        hoito = driver.find_element_by_id("boutonNourrir")
        hoito.click()
        sleep()

        try:
            howrsefeed.findfeed(driver)
            sleep()

        except:
            pass
            sleep()

        hoidettu += 1
        laskuun += 1
        print(hoidettu)
        laske = tarkista(laske, laskuun)
        hoito = driver.find_element_by_id("nav-next")
        hoito.click()
        sleep()


def pikkukissa_knabet(driver, hoida):
    time.sleep(2)
    hoidettu = 0
    laskuun = 0
    laske = random_heppa()

    while (hoidettu < hoida):

        sleep()
        hoito = driver.find_element_by_id("boutonPanser")
        hoito.click()
        sleep()

        hoito = driver.find_element_by_id("boutonCoucher")
        hoito.click()
        sleep()

        # vuoret
        try:
            vuoret.puolitoista(driver)
            sleep()
        except:
            input("ei oo tallissa?")
        hoito = driver.find_element_by_id("boutonNourrir")
        hoito.click()
        sleep()

        try:
            howrsefeed.findfeedblup(driver)
            sleep()

        except:
            pass
            sleep()

        try:
            vuoret.viisipuoli(driver)
            sleep()
        except:
            input("Tee 5.5h vuoria")

        anna_herkut(driver)
        sleep()

        try:
            vuoret.tunti(driver)
            sleep()
        except:
            input("Tee 1h vuoria")

        hoidettu += 1
        laskuun += 1
        laske = tarkista(laske, laskuun)
        hoito = driver.find_element_by_id("nav-next")
        hoito.click()
        sleep()


def pikkukissa_muut(driver, hoida):
    time.sleep(2)
    hoidettu = 0
    laskuun = 0
    laske = random_heppa()

    while (hoidettu < hoida):

        sleep()
        hoito = driver.find_element_by_id("boutonPanser")
        hoito.click()
        sleep()

        hoito = driver.find_element_by_id("boutonCoucher")
        hoito.click()
        sleep()
        try:
            koulu.viisi(driver)
        except:
            try:
                nopeus.viisi(driver)
            except:
                tehtava(driver)
        sleep()

        anna_huonot_herkut(driver)
        sleep()

        hoito = driver.find_element_by_id("boutonNourrir")
        hoito.click()
        sleep()


        try:
            howrsefeed.findfeedlow(driver)
            sleep()

        except:
            pass
            sleep()

        # koulu.viisi(driver)
        sleep()
        hoidettu += 1
        laskuun += 1
        laske = tarkista(laske, laskuun)
        hoito = driver.find_element_by_id("nav-next")
        hoito.click()
        sleep()


def hoida_anni(driver, hoidettavia):
    time.sleep(2)
    hoidettu = 0
    laskuun = 0
    laske = random_heppa()
    print(laske)
    while hoidettu < hoidettavia:
        print(hoidettu)
        sleep()
        hoito = driver.find_element_by_id("boutonPanser")
        hoito.click()
        sleep()
        hoito = driver.find_element_by_id("boutonCoucher")
        hoito.click()
        sleep()
        try:
            driver.find_element_by_id("boutonNourrir").click()
            sleep()
            hoito = driver.find_element_by_id("feed-button")
            hoito.click()
            sleep()
        except:
            pass

        hoidettu += 1
        laskuun += 1
        laske = tarkista(laske, laskuun)
        hoito = driver.find_element_by_id("nav-next")
        hoito.click()
        sleep()


def tehtava(driver):
    try:
        hoito = driver.find_element_by_id("boutonMissionEquus")
        hoito.click()
    except:
        try:
            hoito = driver.find_element_by_id("boutonMissionForet")
            hoito.click()
        except:
            try:
                hoito = driver.find_element_by_id("boutonMissionMontagne")
                hoito.click()
            except:
                pass
        sleep()


def keskus(driver):
    try:
        driver.find_element_by_xpath("html/body/div[@id='container']/main/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[5]/div/div/div/div/div/div/div[@id='cheval-inscription']/a").click()
        tehtava_sleep()
        tehtava_sleep()
        driver.find_element_by_id("tab-box-reserve").click()
        tehtava_sleep()
        tehtava_sleep()
        driver.find_element_by_xpath("html/body/div[@id='container']/main/section/section/div[@id='boxContent']/table/tbody/tr[7]/td[9]/button").click()
        tehtava_sleep()
        driver.find_element_by_id("boutonCoucher").click()
        sleep()
    except:
        pass

    try:
        hoito = driver.find_element_by_xpath("html/body/div[@id='container']/main/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[5]/div/div/div/div/div/div/div[@id='cheval-inscription']/a")
        hoito.click()
        sleep()
        hoito = driver.find_element_by_xpath("html/body/div[@id='container']/main/section/section/div[@id='centresContent']/table/thead/tr/td[6]/span[2]/span/span[5]/a")
        hoito.click()
        tehtava_sleep()
        tehtava_sleep()
        hoito = driver.find_element_by_xpath("html/body/div[@id='container']/main/section/section/div[@id='centresContent']/table/tbody/tr/td[8]/button")
        hoito.click()
        tehtava_sleep()
        hoito = driver.find_element_by_id("boutonCoucher")
        hoito.click()
        sleep()
    except:
        pass


def keskus_normaali(driver):

    try:
        klik = driver.find_element_by_xpath("html/body/div[@id='container']/main/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[3]/div/div/div/div/div/div/div[@id='cheval-inscription']/a")
        klik.click()
        tehtava_sleep()
        tehtava_sleep()
        klik = driver.find_element_by_xpath("html/body/div[@id='container']/main/section/section/ul/li[@id='tab-box-reserve']/div/a")
        klik.click()
        tehtava_sleep()
        klik = driver.find_element_by_xpath("html/body/div[@id='container']/main/section/section/div[@id='boxContent']/table/tbody/tr[3]/td[10]/button")
        klik.click()
        tehtava_sleep()
    except:
        pass


def keskus_anni(driver):
    try:
        klik = driver.find_element_by_xpath(
            "html/body/div[@id='container']/main/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[3]/div/div/div/div/div/div/div[@id='cheval-inscription']/a")
        klik.click()
        tehtava_sleep()
        driver.find_element_by_xpath("html/body/div[@id='container']/main/section/section/div[@id='centresContent']/table/thead/tr/td[6]/span[2]/span/span[9]/a").click()
        sleep()
        sleep()
        driver.find_element_by_xpath("html/body/div[@id='container']/main/section/section/div[@id='centresContent']/table/tbody/tr/td[10]/button").click()
        sleep()
        driver.find_element_by_id("boutonCoucher").click()
        sleep()
    except:
        pass


def tarkista(laske, laskuun):
    if laskuun == laske:
        odota = random_wait()
        print("Odotetaan ", odota, " sekuntia")
        time.sleep(odota)
        laske = random_heppa()
        return laske
    else:
        return laske


def anna_herkut(driver):
    # Silitys, vesi, porkkana, ape
    try:
        klik = driver.find_element_by_id("boutonCaresser")
        klik.click()
        sleep()
    except:
        input("Silitä")
    try:
        klik = driver.find_element_by_id("boutonBoire")
        klik.click()
        sleep()
    except:
        input("vesi")
    try:
        klik =driver.find_element_by_id("boutonCarotte")
        klik.click()
        sleep()
    except:
        input("porkkana")
    try:
        klik = driver.find_element_by_id("boutonMash")
        klik.click()
        sleep()
    except:
        input("ape")


def anna_huonot_herkut(driver):
    # Silitys, vesi, porkkana
    try:
        klik = driver.find_element_by_id("boutonCaresser")
        klik.click()
        sleep()
    except:
        input("Silitä")
    try:
        klik = driver.find_element_by_id("boutonBoire")
        klik.click()
        sleep()
    except:
        input("vesi")
    # try:
    #     klik =driver.find_element_by_id("boutonCarotte")
    #     klik.click()
    #     sleep()
    # except:
    #     input("porkkana")


def sleep():
    time.sleep(random.uniform(1.43,  1.55))


def tehtava_sleep():
    time.sleep(random.uniform(1.48, 1.57))


def long_sleep():
    time.sleep(random.uniform(5.75, 12.103))


def very_long_sleep():
    time.sleep(random.uniform(90.75, 454.103))


def random_heppa():
    horse = random.randint(18, 170)
    return horse


def random_wait():
    wait = random.uniform(5, 50)
    return wait


if __name__ == "__main__":
    log_in()
    exit()