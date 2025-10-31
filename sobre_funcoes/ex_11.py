# Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e 
# devolva uma string no formato D de mes_por_extenso de AAAA. Opcionalmente, valide a data e 
# retorne None caso a data seja inválida.

from datetime import datetime

try:
    # Tenta criar um objeto datetime a partir de uma string
    data = datetime.strptime("2024-10-31", "%Y-%m-%d")
    print("Data válida:", data)
except ValueError:
    print("Formato de data inválido.")