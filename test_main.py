from datetime import datetime
from selenium.webdriver.common.by import By
from pytest import mark
import time
from selenium import webdriver
import os
import errno

def save_image(d, ruta):
    time.sleep(2)
    try:
        os.mkdir('src/'+ruta)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    tiempo = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    d.save_screenshot(f"./src/{ruta}/{tiempo}.png")
    return

@mark.parametrize("n,p", [("admin", "admin"), ("admin", "123456")])
def test_inicioSesion(n, p):
    d = webdriver.Chrome()
    d.get("https://advance-login-panel.elsnerdev.com/admin/signin")
    d.maximize_window()
    d.find_element(By.ID, 'username').send_keys(n)
    d.find_element(By.ID, 'password').send_keys(p)
    d.find_element(By.XPATH, '//*[@id="SignIn"]/div/div/div/div/div[4]/button').click()
    save_image(d, 'inicio')
    assert d.current_url == 'https://advance-login-panel.elsnerdev.com/admin/dashboard'
    
def test_cierresesion():
    d = webdriver.Chrome()
    d.get("https://advance-login-panel.elsnerdev.com/admin/signin")
    d.maximize_window()
    d.find_element(By.ID, 'username').send_keys("admin")
    d.find_element(By.ID, 'password').send_keys("123456")
    d.find_element(By.XPATH, '//*[@id="SignIn"]/div/div/div/div/div[4]/button').click()
    time.sleep(4)
    d.find_element(By.XPATH, '/html/body/div[2]/header/div/div/div[2]/ul/li').click()
    d.find_element(By.XPATH, '/html/body/div[2]/header/div/div/div[2]/ul/li/div/div/div/a').click()
    save_image(d, 'cierre')
    assert d.current_url == 'https://advance-login-panel.elsnerdev.com/admin/signin'

def test_myProfile():
    d = webdriver.Chrome()
    d.get("https://advance-login-panel.elsnerdev.com/admin/signin")
    d.maximize_window()
    d.find_element(By.ID, 'username').send_keys("admin")
    d.find_element(By.ID, 'password').send_keys("123456")
    d.find_element(By.XPATH, '//*[@id="SignIn"]/div/div/div/div/div[4]/button').click()
    time.sleep(4)
    d.find_element(By.XPATH, '/html/body/div[2]/header/div/div/div[2]/ul/li').click()
    d.find_element(By.XPATH, '/html/body/div[2]/header/div/div/div[2]/ul/li/div/div/ul/li[1]').click()
    save_image(d, 'myProfile')
    assert d.current_url == 'https://advance-login-panel.elsnerdev.com/admin/profile'

def test_userPage():
    d = webdriver.Chrome()
    d.get("https://advance-login-panel.elsnerdev.com/admin/signin")
    d.maximize_window()
    d.find_element(By.ID, 'username').send_keys("admin")
    d.find_element(By.ID, 'password').send_keys("123456")
    d.find_element(By.XPATH, '//*[@id="SignIn"]/div/div/div/div/div[4]/button').click()
    time.sleep(4)
    d.find_element(By.XPATH, '//*[@id="unifyMenu"]/li[2]/a').click()
    save_image(d, 'userPage')
    assert d.current_url == 'https://advance-login-panel.elsnerdev.com/admin/user'

def test_userSearch():
    d = webdriver.Chrome()
    d.get("https://advance-login-panel.elsnerdev.com/admin/signin")
    d.maximize_window()
    d.find_element(By.ID, 'username').send_keys("admin")
    d.find_element(By.ID, 'password').send_keys("123456")
    d.find_element(By.XPATH, '//*[@id="SignIn"]/div/div/div/div/div[4]/button').click()
    time.sleep(4)
    d.find_element(By.XPATH, '//*[@id="unifyMenu"]/li[2]/a').click()
    d.find_element(By.XPATH, '//*[@id="datatable_filter"]/label/input').send_keys('Monos Monazo')
    user = d.find_element(By.XPATH, '//*[@id="datatable"]/tbody/tr[1]/td[3]').text
    save_image(d, 'userSearch')
    assert user == 'Monos Monazo'

def test_cms():
    d = webdriver.Chrome()
    d.get("https://advance-login-panel.elsnerdev.com/admin/signin")
    d.maximize_window()
    d.find_element(By.ID, 'username').send_keys("admin")
    d.find_element(By.ID, 'password').send_keys("123456")
    d.find_element(By.XPATH, '//*[@id="SignIn"]/div/div/div/div/div[4]/button').click()
    time.sleep(4)
    d.find_element(By.XPATH, '//*[@id="unifyMenu"]/li[3]/a').click()
    save_image(d, 'cms')
    assert d.current_url == 'https://advance-login-panel.elsnerdev.com/admin/cms'

def test_cmsSearch():
    d = webdriver.Chrome()
    d.get("https://advance-login-panel.elsnerdev.com/admin/signin")
    d.maximize_window()
    d.find_element(By.ID, 'username').send_keys("admin")
    d.find_element(By.ID, 'password').send_keys("123456")
    d.find_element(By.XPATH, '//*[@id="SignIn"]/div/div/div/div/div[4]/button').click()
    time.sleep(4)
    d.find_element(By.XPATH, '//*[@id="unifyMenu"]/li[3]/a').click()
    d.find_element(By.XPATH, '//*[@id="datatable_filter"]/label/input').send_keys('5')
    txt = d.find_element(By.XPATH, '//*[@id="datatable"]/tbody/tr/td[2]').text
    save_image(d, 'cmsSearch')
    assert txt == '5'

def test_rolePermission():
    d = webdriver.Chrome()
    d.get("https://advance-login-panel.elsnerdev.com/admin/signin")
    d.maximize_window()
    d.find_element(By.ID, 'username').send_keys("admin")
    d.find_element(By.ID, 'password').send_keys("123456")
    d.find_element(By.XPATH, '//*[@id="SignIn"]/div/div/div/div/div[4]/button').click()
    time.sleep(4)
    d.find_element(By.XPATH, '//*[@id="unifyMenu"]/li[5]/a').click()
    save_image(d, 'rolePermission')
    assert d.current_url == 'https://advance-login-panel.elsnerdev.com/admin/RolePermission'

def test_rolePermissionSearch():
    d = webdriver.Chrome()
    d.get("https://advance-login-panel.elsnerdev.com/admin/signin")
    d.maximize_window()
    d.find_element(By.ID, 'username').send_keys("admin")
    d.find_element(By.ID, 'password').send_keys("123456")
    d.find_element(By.XPATH, '//*[@id="SignIn"]/div/div/div/div/div[4]/button').click()
    time.sleep(4)
    d.find_element(By.XPATH, '//*[@id="unifyMenu"]/li[5]/a').click()
    d.find_element(By.XPATH, '//*[@id="datatable_filter"]/label/input').send_keys('User')
    txt = d.find_element(By.XPATH, '//*[@id="datatable"]/tbody/tr/td[3]/a').text
    save_image(d, 'rolePermissionSearch')
    assert txt == 'Edit'

def test_moduleSettings():
    d = webdriver.Chrome()
    d.get("https://advance-login-panel.elsnerdev.com/admin/signin")
    d.maximize_window()
    d.find_element(By.ID, 'username').send_keys("admin")
    d.find_element(By.ID, 'password').send_keys("123456")
    d.find_element(By.XPATH, '//*[@id="SignIn"]/div/div/div/div/div[4]/button').click()
    time.sleep(4)
    d.find_element(By.XPATH, '//*[@id="unifyMenu"]/li[6]/a').click()
    save_image(d, 'moduleSettings')
    assert d.current_url == 'https://advance-login-panel.elsnerdev.com/admin/ModuleSetting'

def test_moduleSettingsSearch():
    d = webdriver.Chrome()
    d.get("https://advance-login-panel.elsnerdev.com/admin/signin")
    d.maximize_window()
    d.find_element(By.ID, 'username').send_keys("admin")
    d.find_element(By.ID, 'password').send_keys("123456")
    d.find_element(By.XPATH, '//*[@id="SignIn"]/div/div/div/div/div[4]/button').click()
    time.sleep(4)
    d.find_element(By.XPATH, '//*[@id="unifyMenu"]/li[6]/a').click()
    d.find_element(By.XPATH, '//*[@id="datatable_filter"]/label/input').send_keys('5')
    txt = d.find_element(By.XPATH, '//*[@id="datatable"]/tbody/tr/td[3]').text
    save_image(d, 'moduleSettingsSearch')
    assert txt == 'BPS'

def test_userEdit():
    d = webdriver.Chrome()
    d.get("https://advance-login-panel.elsnerdev.com/admin/signin")
    d.maximize_window()
    d.find_element(By.ID, 'username').send_keys("admin")
    d.find_element(By.ID, 'password').send_keys("123456")
    d.find_element(By.XPATH, '//*[@id="SignIn"]/div/div/div/div/div[4]/button').click()
    time.sleep(4)
    d.find_element(By.XPATH, '//*[@id="unifyMenu"]/li[2]/a').click()
    d.find_element(By.XPATH, '//*[@id="datatable_filter"]/label/input').send_keys('Monos')
    data = d.find_element(By.XPATH, '//*[@id="datatable"]/tbody/tr/td[8]/a').text
    save_image(d, 'userEdit')
    assert data == "Edit"

def test_cmsEdit():
    d = webdriver.Chrome()
    d.get("https://advance-login-panel.elsnerdev.com/admin/signin")
    d.maximize_window()
    d.find_element(By.ID, 'username').send_keys("admin")
    d.find_element(By.ID, 'password').send_keys("123456")
    d.find_element(By.XPATH, '//*[@id="SignIn"]/div/div/div/div/div[4]/button').click()
    time.sleep(4)
    d.find_element(By.XPATH, '//*[@id="unifyMenu"]/li[3]/a').click()
    d.find_element(By.XPATH, '//*[@id="datatable_filter"]/label/input').send_keys('55')
    title = d.find_element(By.XPATH, '//*[@id="datatable"]/tbody/tr[3]/td[3]').text
    d.find_element(By.XPATH, '//*[@id="datatable"]/tbody/tr[1]/td[4]/a[2]').click()
    txt = d.find_element(By.XPATH, '//*[@id="title"]').text
    save_image(d, 'cmsEdit')
    assert txt == title

def test_roleEdit():
    d = webdriver.Chrome()
    d.get("https://advance-login-panel.elsnerdev.com/admin/signin")
    d.maximize_window()
    d.find_element(By.ID, 'username').send_keys("admin")
    d.find_element(By.ID, 'password').send_keys("123456")
    d.find_element(By.XPATH, '//*[@id="SignIn"]/div/div/div/div/div[4]/button').click()
    time.sleep(4)
    d.find_element(By.XPATH, '//*[@id="unifyMenu"]/li[5]/a').click()
    d.find_element(By.XPATH, '//*[@id="datatable_filter"]/label/input').send_keys('User')
    data = d.find_element(By.XPATH, '//*[@id="datatable"]/tbody/tr/td[3]/a').text
    save_image(d, 'roleEdit')
    assert data == 'Edit'

def test_moduleEdit():
    d = webdriver.Chrome()
    d.get("https://advance-login-panel.elsnerdev.com/admin/signin")
    d.maximize_window()
    d.find_element(By.ID, 'username').send_keys("admin")
    d.find_element(By.ID, 'password').send_keys("123456")
    d.find_element(By.XPATH, '//*[@id="SignIn"]/div/div/div/div/div[4]/button').click()
    time.sleep(4)
    d.find_element(By.XPATH, '//*[@id="unifyMenu"]/li[6]/a').click()
    d.find_element(By.XPATH, '//*[@id="datatable_filter"]/label/input').send_keys('BPS')
    data = d.find_element(By.XPATH, '//*[@id="datatable"]/tbody/tr/td[5]/a').text
    save_image(d, 'moduleEdit')
    assert data == 'Edit'

def test_passwordEdit():
    d = webdriver.Chrome()
    d.get("https://advance-login-panel.elsnerdev.com/admin/signin")
    d.maximize_window()
    d.find_element(By.ID, 'username').send_keys("admin")
    d.find_element(By.ID, 'password').send_keys("123456")
    d.find_element(By.XPATH, '//*[@id="SignIn"]/div/div/div/div/div[4]/button').click()
    time.sleep(4)
    d.find_element(By.XPATH, '/html/body/div[2]/header/div/div/div[2]/ul/li').click()
    d.find_element(By.XPATH, '/html/body/div[2]/header/div/div/div[2]/ul/li/div/div/ul/li[2]/a').click()
    save_image(d, 'passwordEdit')
    assert d.current_url == 'https://advance-login-panel.elsnerdev.com/admin/change_password'

def test_settings():
    d = webdriver.Chrome()
    d.get("https://advance-login-panel.elsnerdev.com/admin/signin")
    d.maximize_window()
    d.find_element(By.ID, 'username').send_keys("admin")
    d.find_element(By.ID, 'password').send_keys("123456")
    d.find_element(By.XPATH, '//*[@id="SignIn"]/div/div/div/div/div[4]/button').click()
    time.sleep(4)
    d.find_element(By.XPATH, '//*[@id="unifyMenu"]/li[4]/a').click()
    d.find_element(By.XPATH, '//*[@id="unifyMenu"]/li[4]/ul/li[1]/a').click()
    save_image(d, 'settings')
    assert d.current_url == 'https://advance-login-panel.elsnerdev.com/admin/Settings/create'

def test_settingsCopy():
    d = webdriver.Chrome()
    copy = '© Copyright 2006 – 2019'
    d.get("https://advance-login-panel.elsnerdev.com/admin/signin")
    d.maximize_window()
    d.find_element(By.ID, 'username').send_keys("admin")
    d.find_element(By.ID, 'password').send_keys("123456")
    d.find_element(By.XPATH, '//*[@id="SignIn"]/div/div/div/div/div[4]/button').click()
    time.sleep(4)
    d.find_element(By.XPATH, '//*[@id="unifyMenu"]/li[4]/a').click()
    d.find_element(By.XPATH, '//*[@id="unifyMenu"]/li[4]/ul/li[1]/a').click()
    d.find_element(By.ID, 'footer_text').clear()
    d.find_element(By.ID, 'footer_text').send_keys(copy)
    d.find_element(By.XPATH, '//*[@id="Settings"]/div/div/div[2]/button').click()
    time.sleep(3)
    txt = d.find_element(By.XPATH, '/html/body/div[2]/div/div/footer').text
    save_image(d, 'settingsCopy')
    assert txt == copy

def test_banIp():
    d = webdriver.Chrome()
    d.get("https://advance-login-panel.elsnerdev.com/admin/signin")
    d.maximize_window()
    d.find_element(By.ID, 'username').send_keys("admin")
    d.find_element(By.ID, 'password').send_keys("123456")
    d.find_element(By.XPATH, '//*[@id="SignIn"]/div/div/div/div/div[4]/button').click()
    time.sleep(4)
    d.find_element(By.XPATH, '//*[@id="unifyMenu"]/li[4]/a').click()
    d.find_element(By.XPATH, '//*[@id="unifyMenu"]/li[4]/ul/li[2]/a').click()
    save_image(d, 'banIp')
    assert d.current_url == 'https://advance-login-panel.elsnerdev.com/admin/banip'

def test_banIpEdit():
    d = webdriver.Chrome()
    d.get("https://advance-login-panel.elsnerdev.com/admin/signin")
    d.maximize_window()
    d.find_element(By.ID, 'username').send_keys("admin")
    d.find_element(By.ID, 'password').send_keys("123456")
    d.find_element(By.XPATH, '//*[@id="SignIn"]/div/div/div/div/div[4]/button').click()
    time.sleep(4)
    d.find_element(By.XPATH, '//*[@id="unifyMenu"]/li[4]/a').click()
    d.find_element(By.XPATH, '//*[@id="datatable_filter"]/label/input').send_keys('192.168.4.45')
    time.sleep(2)
    data = d.find_element(By.XPATH, '//*[@id="datatable"]/tbody/tr/td[3]/a').text
    save_image(d, 'banIpEdit')
    assert data == 'Edit'