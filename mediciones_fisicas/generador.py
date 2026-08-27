import csv
import random

NUM_REGISTROS = 50
ARCHIVO_SALIDA = "datos.csv"


def generar_datos(n):
    registros = []
    tiempo = 0.0
    for _ in range(n):
        tiempo += round(random.uniform(0.5, 2.0), 2)
        valor = round(random.gauss(mu=25.0, sigma=5.0), 3)
        registros.append((round(tiempo, 2), valor))
    return registros


def guardar_csv(registros, ruta):
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["tiempo", "valor"])
        writer.writerows(registros)


def main():
    registros = generar_datos(NUM_REGISTROS)
    guardar_csv(registros, ARCHIVO_SALIDA)
    print(f"Se generaron {len(registros)} registros en '{ARCHIVO_SALIDA}'")


if __name__ == "__main__":
    main()
