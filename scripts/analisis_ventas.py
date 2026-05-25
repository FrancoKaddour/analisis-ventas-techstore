
import csv
import os
import matplotlib.pyplot as plt

BASE_DIR     = '/content/analisis-ventas-techstore'
RUTA_CSV     = os.path.join(BASE_DIR, "datos",      "ventas.csv")
RUTA_TXT     = os.path.join(BASE_DIR, "resultados", "resumen_ventas.txt")
RUTA_GRAFICO = os.path.join(BASE_DIR, "resultados", "grafico_ventas.png")

os.makedirs(os.path.join(BASE_DIR, "resultados"), exist_ok=True)

ventas = []
with open(RUTA_CSV, newline="", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        ventas.append({
            "fecha":    fila["fecha"],
            "producto": fila["producto"],
            "cantidad": int(fila["cantidad"]),
            "precio":   int(fila["precio"]),
        })

for v in ventas:
    v["total"] = v["cantidad"] * v["precio"]

total_ventas = sum(v["total"] for v in ventas)

ingresos_producto = {}
for v in ventas:
    p = v["producto"]
    ingresos_producto[p] = ingresos_producto.get(p, 0) + v["total"]
producto_top = max(ingresos_producto, key=ingresos_producto.get)

ingresos_mes = {}
for v in ventas:
    mes = v["fecha"][:7]
    ingresos_mes[mes] = ingresos_mes.get(mes, 0) + v["total"]
mes_top = max(ingresos_mes, key=ingresos_mes.get)

resultado = f"""
====================================================
  ANALISIS DE VENTAS - TECHSTORE 2024
====================================================
  Total de ventas del ano : $ {total_ventas:,}
  Producto mas vendido    : {producto_top}
  Mes con mas ventas      : {mes_top}
====================================================
"""

print(resultado)
with open(RUTA_TXT, "w", encoding="utf-8") as f:
    f.write(resultado)
print("[OK] Resumen guardado en: resultados/resumen_ventas.txt")

meses          = sorted(ingresos_mes.keys())
ventas_por_mes = [ingresos_mes[m] for m in meses]

nombres_meses = {
    "01": "Ene", "02": "Feb", "03": "Mar", "04": "Abr",
    "05": "May", "06": "Jun", "07": "Jul", "08": "Ago",
    "09": "Sep", "10": "Oct", "11": "Nov", "12": "Dic"
}
etiquetas = [nombres_meses[m.split("-")[1]] for m in meses]

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(etiquetas, ventas_por_mes, marker="o", color="steelblue", linewidth=2)
ax.fill_between(etiquetas, ventas_por_mes, alpha=0.15, color="steelblue")
ax.set_title("Evolucion de Ventas Mensuales - TechStore 2024", fontsize=14)
ax.set_xlabel("Mes")
ax.set_ylabel("Ingresos ($)")
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x:,.0f}"))
plt.tight_layout()
plt.savefig(RUTA_GRAFICO, dpi=150)
print("[OK] Grafico guardado en: resultados/grafico_ventas.png")
