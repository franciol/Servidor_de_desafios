import pytest
import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from softdes import lambda_handler




a = {'ndes': '1', 'code': '"""Arquivo a ser enviado ao sistema"""\n\ndef desafio1(number):\n    """Função que retorna o valor entrado"""\n    return number\n', 'args': [[1], [2], [3]], 'resp': [0, 0, 0], 'diag': ['a', 'b', 'c']}
b = {'ndes': '1', 'code': '"""Arquivo a ser enviado ao sistema"""\n\ndef desafio1(number):\n    """Função que retorna o valor entrado"""\n    return number\n', 'args': [[1], [2], [3]], 'resp': [1, 2, 3], 'diag': ['a', 'b', 'c']}
c = {'ndes': '1', 'code': '"""Arquivo a ser enviado ao sistema"""\n\ndef desafio1(number):\n    """Função que retorna o valor entrado"""\n    return number\n', 'args': [[1], [2], [3]], 'resp': [0, 2, 0], 'diag': ['a', 'b', 'c']}
d = {'ndes': '1', 'code': '"""Arquivo a ser enviado ao sistema"""\n\ndef desafio2(number):\n    """Função que retorna o valor entrado"""\n    return number\n', 'args': [[1], [2], [3]], 'resp': [0, 2, 0], 'diag': ['a', 'b', 'c']}
e = {'diag': ['a', 'b', 'c']}
driver = webdriver.Firefox(executable_path=os.path.curdir+"/geckodriver")
    



def test_01():
    assert (lambda_handler(a,'')) == "a b c"

def test_02():
    assert lambda_handler(b,'') == ''

def test_03():
    assert lambda_handler(c,'') == "a c"

def test_04():
    assert lambda_handler(d,'') == "Nome da função inválido. Usar 'def desafio1(...)'"

def test_05():
    assert lambda_handler(e,'') == "Função inválida."

def test_06():
    driver.get("http://igor:password@localhost:80")
    assert "SoftDes" in driver.title

def test_07():
    driver.find_element_by_id("resposta").send_keys(os.getcwd()+"/desafio.py")
    btn = driver.find_element_by_class_name("btn-primary")
    btn.click()
    time.sleep(0.5)
    table = driver.find_element_by_class_name("table")
    rows = table.find_elements_by_tag_name("tr")
    cols = rows[1].find_elements_by_tag_name("td")
    assert "Erro" in cols[2].text
    time.sleep(1)

def test_08():    
    driver.find_element_by_id("resposta").send_keys(os.getcwd()+"/desafio_certo.py")
    btn = driver.find_element_by_class_name("btn-primary")
    btn.click()
    time.sleep(0.5)
    table = driver.find_element_by_class_name("table")
    rows = table.find_elements_by_tag_name("tr")
    cols = rows[1].find_elements_by_tag_name("td")
    assert "OK!" in cols[2].text
    time.sleep(1)
    driver.close()
