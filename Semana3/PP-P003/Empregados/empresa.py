from empregado import Empregado

def Reajusta_dez_porcento(empregados):
    for empregado in empregados:
        empregado.salario *= 1.1  # Aumenta o salário em 10%
