import sys
from softdes import lambda_handler
import pytest

a = {'ndes': '1', 'code': '"""Arquivo a ser enviado ao sistema"""\n\ndef desafio1(number):\n    """Função que retorna o valor entrado"""\n    return number\n', 'args': [[1], [2], [3]], 'resp': [0, 0, 0], 'diag': ['a', 'b', 'c']}
b = {'ndes': '1', 'code': '"""Arquivo a ser enviado ao sistema"""\n\ndef desafio1(number):\n    """Função que retorna o valor entrado"""\n    return number\n', 'args': [[1], [2], [3]], 'resp': [1, 2, 3], 'diag': ['a', 'b', 'c']}
c = {'ndes': '1', 'code': '"""Arquivo a ser enviado ao sistema"""\n\ndef desafio1(number):\n    """Função que retorna o valor entrado"""\n    return number\n', 'args': [[1], [2], [3]], 'resp': [0, 2, 0], 'diag': ['a', 'b', 'c']}
d = {'ndes': '1', 'code': '"""Arquivo a ser enviado ao sistema"""\n\ndef desafio2(number):\n    """Função que retorna o valor entrado"""\n    return number\n', 'args': [[1], [2], [3]], 'resp': [0, 2, 0], 'diag': ['a', 'b', 'c']}
e = {'diag': ['a', 'b', 'c']}

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