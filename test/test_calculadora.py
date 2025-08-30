import pytest
from calculadora import sumar, restar, multiplicar, dividir

#test en la función sumar
"""def test_sumar_positivos(enteros): #Usando el fixture enteros
    num1, num2 = enteros
    assert sumar(num1, num2) == 15
    
def test_sumar_negativos():
    assert sumar(-10, -5) == -15
    
def test_sumar_cero():
    assert sumar(0, 5) == 5"""
    
#Parametrización de tests

import pytest
from calculadora import sumar

@pytest.mark.parametrize("num1, num2, resultado_esperado", [
    (10, 5, 15),          # Test para números positivos
    (-10, -5, -15),       # Test para números negativos
    (0, 5, 5)             # Test para cero
])
def test_sumar_parametrizada(num1, num2, resultado_esperado):
    assert sumar(num1, num2) == resultado_esperado
    

#test en la función restar
"""def test_restar_positivos(enteros):
    num1, num2 = enteros
    assert restar(num1, num2) == 5
    
def test_restar_negativos():
    assert restar(-10, -5) == -5
    
def test_restar_cero():
    assert restar(0, 5) == -5"""

@pytest.mark.smoke       #Se usa con pytest -m smoke
@pytest.mark.parametrize("num1, num2, resultado_esperado", [
    (10, 5, 5),          # Test para números positivos
    (-10, -5, -5),       # Test para números negativos
    (0, 5, -5)             # Test para cero
])
def test_restar_parametrizada(num1, num2, resultado_esperado):
    assert restar(num1, num2) == resultado_esperado
    
    
#test en la función multiplicar
def test_multiplicar_positivos(enteros):
    num1, num2 = enteros
    assert multiplicar(num1, num2) == 50
    
def test_multiplicar_negativos():
    assert multiplicar(-10, -5) == 50
    
def test_multiplicar_cero():
    assert multiplicar(0, 5) == 0
    
# Tests para la función dividir
@pytest.mark.exception               #Se usa con pytest -m exception
def test_dividir_positivos(enteros):
    num1, num2 = enteros
    assert dividir(num1, num2) == 2
    
def test_dividir_negativos():
    assert dividir(-10, -5) == 2
    
def test_dividir_por_cero_lanza_error():
    with pytest.raises(ValueError):
        dividir(5, 0)
    
def test_dividir_cero_entre_un_numero():
    assert dividir(0, 5) == 0