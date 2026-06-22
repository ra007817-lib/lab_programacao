"""
escreva uma fonção que chamada celsius_para_fahrenheit que recebe
yma temperatura em graus celsos como parametro e retorna o valor
corespondenete em fehrenheit. a  formaloa e: f = c * 1.8 + 32. no
programa principalmete, peça a temparatuara em celsius para o 
usuariao e exba o resutado suado a fiunção
"""

def celsius_para_fahrenheit(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit

temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))

temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)

print("A temperatura em Fahrenheit é:", temperatura_fahrenheit)