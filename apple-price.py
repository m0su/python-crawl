# 엘레강트 오브젝트에 따른 네이밍
# 클래스는 무엇을 하는지(what he does)가 아니라 무엇인지(what he is)에 기반해야 한다.

from urllib.parse import quote_plus
from bson.dbref import DBRef    # 한글 텍스트를 퍼센트 인코딩으로 변환
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   # 해당 태그를 기다림
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException    # 태그가 없는 예외 처리

buy_mac = "https://www.apple.com/kr-k12/shop/buy-mac"
macbook_air = "/macbook-air"
macbook_pro = "/macbook-pro"
mac_mini = "/mac-mini"

macbook_air_options = [
    "/macbook-air/스페이스-그레이-apple-m1-칩(8코어-cpu-및-7코어-gpu)-256gb#",
    "/macbook-air/골드-apple-m1-칩(8코어-cpu-및-7코어-gpu)-256gb#",
    "/macbook-air/실버-apple-m1-칩(8코어-cpu-및-7코어-gpu)-256gb#",
    "/macbook-air/스페이스-그레이-apple-m1-칩(8코어-cpu-및-8코어-gpu)-512gb#",
    "/macbook-air/골드-apple-m1-칩(8코어-cpu-및-8코어-gpu)-512gb#",
    "/macbook-air/실버-apple-m1-칩(8코어-cpu-및-8코어-gpu)-512gb#",
]

macbook_pro_options = [
    "/macbook-pro/13형-스페이스-그레이-apple-m1-칩(8코어-cpu-및-8코어-gpu)-256gb#",
    "/macbook-pro/13형-실버-apple-m1-칩(8코어-cpu-및-8코어-gpu)-256gb##",
]

mac_mini_options = [
    "/mac-mini/apple-m1-칩(8코어-cpu-및-8코어-gpu)-256gb#"
]

# chromedriver 기본셋팅
def drive():
    chromedriver = "./chromedriver"
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument("disable-gpu")
    options.add_argument("lang=ko_KR")

    return webdriver.Chrome(chromedriver, options=options)

# keyword: air, pro, mini
def parse():
    driver = drive()
    driver.get(buy_mac + macbook_air_options[0])

    try: # 정상처리
        # "as-optionselector" // 1. 메모리 2. 저장장치 3.
        
        result = driver.find_element_by_xpath("//*[@id='page']")
        # title = driver.find_element_by_class_name('as-optionselector')

        print(result)
    except TimeoutException:
        print("timeout")
    except NoSuchElementException:
        print("NoSuchElementException")

    driver.quit()

parse()
