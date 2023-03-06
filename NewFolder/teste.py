def calc_consumo(distancia, combustivel):
  consumo = combustivel / distancia
  consumo_km = consumo * 100
  return consumo_km

distancia = float(input("Insira a distância percorrida (em km): "))
combustivel = float(input("Insira o volume de combustível gasto (em litros): "))

consumo_km = calc_consumo(distancia, combustivel)

print("O consumo de gasolina em km/l é de:", consumo_km, "km/l")
