import csv
import statistics

ARCHIVO_ENTRADA = "datos.csv"
ARCHIVO_INFORME = "informe.md"


def leer_datos(ruta):
    tiempos = []
    valores = []
    with open(ruta, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for fila in reader:
            tiempos.append(float(fila["tiempo"]))
            valores.append(float(fila["valor"]))
    return tiempos, valores


def calcular_estadisticas(tiempos, valores):
    promedio = statistics.mean(valores)
    desviacion = statistics.stdev(valores)
    valor_maximo = max(valores)
    tiempo_maximo = tiempos[valores.index(valor_maximo)]
    return {
        "n": len(valores),
        "promedio": promedio,
        "desviacion": desviacion,
        "valor_maximo": valor_maximo,
        "tiempo_maximo": tiempo_maximo,
    }


def guardar_informe(stats, ruta):
    contenido = f"""# Informe de mediciones físicas

- **Registros analizados:** {stats['n']}
- **Promedio:** {stats['promedio']:.3f}
- **Desviación estándar:** {stats['desviacion']:.3f}
- **Valor máximo:** {stats['valor_maximo']:.3f} (en tiempo = {stats['tiempo_maximo']:.2f} s)
"""
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(contenido)


def main():
    tiempos, valores = leer_datos(ARCHIVO_ENTRADA)
    stats = calcular_estadisticas(tiempos, valores)
    guardar_informe(stats, ARCHIVO_INFORME)
    print(f"Informe generado en '{ARCHIVO_INFORME}' a partir de {stats['n']} registros")


if __name__ == "__main__":
    main()
