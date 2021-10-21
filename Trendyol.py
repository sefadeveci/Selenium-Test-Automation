import time
import json

import pypyodbc
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pytest
from selenium.webdriver.support import expected_conditions as EC
import webbrowser



class TestTrendyol():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_login(self):
        conn = pypyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server=DESKTOP-I3V9S4O\SQLEXPRESS01;"
            "Database=telefonrehber;"
            "Trusted_Connection=yes;"
        )
        cursor = conn.cursor()
        datetime.now()
        sql = "INSERT INTO testresults (Gerçekleştiren_Kişi, Tanım, Açıklama,Durum,Öncelik,dtarih) VALUES(?,?,?,?,?,?)"
        wait = WebDriverWait(self.driver, 20)
        self.driver.get("https://www.trendyol.com")

        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "modal-close"))).click()
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "close-button"))).click()

        actualUrl = "https://www.trendyol.com/"
        expected = self.driver.current_url
        # self.assertEqual(actualUrl, expected)

        if (actualUrl == expected):
            print("Welcome")
            values = ("Tester1", "SiteyeGiris", "SiteyeGirisBasarili", "Basarili", "-", datetime.now())
            cursor.execute(sql, values)
            conn.commit()
        else:
            print("Fail")
            values = ("Tester1", "SiteyeGiris", "SiteyeGirisBaşarisiz", "Basarisiz", "-", datetime.now())
            cursor.execute(sql, values)
            conn.commit()

        login: WebElement = self.driver.find_element_by_css_selector(".account-user > .link-text")
        login.click()
        username: WebElement = self.driver.find_element_by_id("login-email")
        password: WebElement = self.driver.find_element_by_id("login-password-input")

        username.send_keys("asdasdasdsefa@gmail.com")
        password.send_keys("testhesabı00")
        gir: WebElement = self.driver.find_element_by_xpath(
            "//div[@id='login-register']/div[3]/div/form/button/span").click()
        actualUrl1 = "https://www.trendyol.com/giris?cb=https%3A%2F%2Fwww.trendyol.com%2Fbutik%2Fliste%2F2%2Ferkek"
        expected1 = self.driver.current_url
        # self.assertEqual(actualUrl, expected)
        if (actualUrl1 == expected1):
            print("Giris Basarılı")
            values = ("Tester1", "ÜyeGiris", "ÜyeGirisBasarili", "Basarili", "Test1", datetime.now())
            cursor.execute(sql, values)
            conn.commit()
        else:
            print("Giriş Başarısız.")
            values = ("Tester1", "ÜyeGiris", "ÜyeGirisBaşarisiz", "Basarisiz", "Test1", datetime.now())
            cursor.execute(sql, values)
            conn.commit()


        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".search-box").send_keys("samsung s20")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".search-icon").click()
        time.sleep(2)

        actualUrl2 = "https://www.trendyol.com/sr?q=samsung%20s20&qt=samsung%20s20&st=samsung%20s20&os=1"

        expected2 = self.driver.current_url

        # self.assertEqual(actualUrl, expected)
        if (actualUrl2 == expected2):
            print("Doğru Ürün Araması")
            values = ("Tester1", "ÜrünArama", "Dogru Ürün Arandi", "Basarili", "Test2", datetime.now())
            cursor.execute(sql, values)
            conn.commit()
        else:
            print("Yanlış Ürün Araması")
            values = ("Tester1", "ÜrünArama", "Ürün Aramasinda Hata", "Basarisiz", "Test2", datetime.now())
            cursor.execute(sql, values)
            conn.commit()


        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, "[data-id='78348960']").click()

        select = Select(self.driver.find_element_by_css_selector('select'))
        time.sleep(2)
        select.select_by_value('PRICE_BY_ASC')
        time.sleep(2)
        actualUrl3 = "https://www.trendyol.com/sr?q=samsung+s20&qt=samsung+s20&st=samsung+s20&sst=PRICE_BY_ASC"
        expected3 = self.driver.current_url

        # self.assertEqual(actualUrl, expected)
        if (actualUrl3 == expected3):
            print("Ürünler doğru sıralandı")
            values = ("Tester1", "ÜrünSiralama", "Ürünler Dogru Siralandi", "Basarili", "Test3", datetime.now())
            cursor.execute(sql, values)
            conn.commit()
        else:
            print("Ürünler yanlış sıralandı")
            values = ("Tester1", "ÜrünSiralama", "Ürünler Yanlis Siralandi", "Basarisiz", "Test3", datetime.now())
            cursor.execute(sql, values)
            conn.commit()
        time.sleep(2)

        self.driver.find_element(By.CSS_SELECTOR, "[data-id='52681989']").click()
        time.sleep(2)
        tab_list = self.driver.window_handles
        self.driver.switch_to.window(tab_list[1])
        actualUrl4 = "https://www.trendyol.com/samsung/m4025-d204-drum-unitesi-chip-p-52681989?boutiqueId=61&merchantId=198613"
        expected4 = self.driver.current_url

        # self.assertEqual(actualUrl, expected)
        if (actualUrl4 == expected4):
            print("Doğru Ürün Seçildi")
            values = ("Tester1", "ÜrünSecim", "Ürün Dogru Secildi", "Basarili", "Test4", datetime.now())
            cursor.execute(sql, values)
            conn.commit()
        else:
            print("Yanlış Ürün Seçildi")
            values = ("Tester1", "ÜrünSecim", "Ürün Yanlıs Secildi", "Basarisiz", "Test4", datetime.now())
            cursor.execute(sql, values)
            conn.commit()
        time.sleep(2)
        self.driver.find_element_by_class_name("add-to-basket").click()

        time.sleep(2)
        sepet: WebElement = self.driver.find_element_by_css_selector(".account-basket > .link-text")
        sepet.click()
        time.sleep(2)
        actualUrl5 = "https://www.trendyol.com/sepet"
        expected5 = self.driver.current_url
        # self.assertEqual(actualUrl, expected)
        if (actualUrl5 == expected5):
            print("Ürün Başarıyla Sepete Eklendi")
            values = ("Tester1", "Sepete Ekle", "Ürün Sepete Basariyla Eklendi", "Basarili", "Test5", datetime.now())
            cursor.execute(sql, values)
            conn.commit()
        else:
            print("Ürün Sepete Eklenemedi")
            values = ("Tester1", "Sepete Ekle", "Ürün Sepete Eklenemedi", "Basarisiz", "Test5", datetime.now())
            cursor.execute(sql, values)
            conn.commit()

        select_employee = "SELECT * FROM testresults"
        cursor = conn.cursor()
        cursor.execute(select_employee)
        result = cursor.fetchall()

        p = []
        tbl = "<tr><td>ID</td><td>GerçeklestirenKisi</td><td>Tanim</td><td>Aciklama</td><td>Durum</td><td>Oncelik</td><td>dTarih</td></tr>"
        p.append(tbl)

        for row in result:
            a = "<tr><td>%s</td>"%row[0]
            p.append(a)
            b = "<td>%s</td>"%row[1]
            p.append(b)
            c = "<td>%s</td>"%row[2]
            p.append(c)
            d = "<td>%s</td>"%row[3]
            p.append(d)
            e = "<td>%s</td>"%row[4]
            p.append(e)
            f = "<td>%s</td>"%row[5]
            p.append(f)
            g = "<td>%s</td></tr>"%row[6]
            p.append(g)

        contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
        <html>
        <head>
        <meta content="text/html; charset=ISO-8859-1"
        http-equiv="content-type">
        <title>Python Webbrowser</title>
        </head>
        <body>
        <table>
        %s
        </table>
        </body>
        </html>
        ''' % (p)
        filename = 'webbrowser.html'
        main(contents, filename)
        webbrowser.open(filename)

def main(contents, filename):
    output = open(filename, "w")
    output.write(contents)
    output.close()


