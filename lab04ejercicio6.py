
def calcularSalario(horas, tarifa): 
    HORAS_SEMANALES = 40 
    horas_extras = 0 
    if (int(horas) > HORAS_SEMANALES): 
        horas_extras = int(horas) - HORAS_SEMANALES
        calculo = int(horas) * float(tarifa) + (horas_extras * int(tarifa) * 1.5)
    return calculo 


horas = input ("Ingrese número de horas trabajadas: ")
tarifa = input ("Ingrese tarifa por hora: ")
salario = calcularSalario(horas, tarifa)
print (salario)