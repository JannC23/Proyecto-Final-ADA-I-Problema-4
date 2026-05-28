from core.motor_consultas import MotorConsultas

motor = MotorConsultas()
archivo = open("entrada.txt", "r")
lineas = archivo.readlines()
archivo.close()
indice = 0
N = int(lineas[indice].strip())
indice += 1

for _ in range(N):
    partes = lineas[indice].strip().split()
    valor = int(partes[0])
    inicio = int(partes[1])
    fin = int(partes[2])
    motor.agregar_rango(valor, inicio, fin)
    indice += 1

Q = int(lineas[indice].strip())
indice += 1
salida = []

for _ in range(Q):
    partes = lineas[indice].strip().split()
    operacion = partes[0]

    if operacion == "VALUE":
        pos = int(partes[1])
        r = motor.value(pos)
        salida.append(f"VALUE {pos} = {r}")
    elif operacion == "SUM":
        ini = int(partes[1])
        fin = int(partes[2])
        r = motor.suma(ini, fin)
        salida.append(f"SUM {ini} {fin} = {r}")
    elif operacion == "UPDATE":
        ini = int(partes[1])
        fin = int(partes[2])
        valor = int(partes[3])
        motor.update(ini, fin, valor)
        salida.append(f"UPDATE {ini} {fin} {valor} = OK")
    elif operacion == "FREQUENCY":
        valor = int(partes[1])
        r = motor.frequency(valor)
        salida.append(f"FREQUENCY {valor} = {r}")
    elif operacion == "MAX_RANGE":
        ini = int(partes[1])
        fin = int(partes[2])
        r = motor.max_range(ini, fin)
        salida.append(f"MAX_RANGE {ini} {fin} = {r}")
    elif operacion == "MIN_RANGE":
        ini = int(partes[1])
        fin = int(partes[2])
        r = motor.min_range(ini, fin)
        salida.append(f"MIN_RANGE {ini} {fin} = {r}")
    elif operacion == "DECOMPRESS":
        ini = int(partes[1])
        fin = int(partes[2])
        r = motor.decompress(ini, fin)
        salida.append(f"DECOMPRESS {ini} {fin} = {r}")
    elif operacion == "COUNT_RANGES":
        r = motor.count_ranges()
        salida.append(f"COUNT_RANGES = {r}")
    elif operacion == "MERGE":
        motor.merge()
        salida.append("MERGE = OK")
    indice += 1

archivo = open("salida.txt", "w")

for linea in salida:
    archivo.write(linea + "\n")
archivo.close()