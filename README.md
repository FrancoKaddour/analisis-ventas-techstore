# Analisis de Ventas - TechStore 2024

Trabajo Practico: Gestion Colaborativa, Control de Versiones y Organizacion Empresarial
**Catedra:** Organizacion Empresarial - UTN TUP 2026
**Escenario:** B - Analisis de Ventas de una Pequena Empresa

---

## Integrantes del Equipo

| Rol | Nombre | Responsabilidad |
|-----|--------|-----------------|
| P1 - Hugo (Lider y Organizador) | Franco Kaddour | Gobernanza del repositorio, estructura inicial de carpetas |
| P2 - Paco (Desarrollador Tecnico) | Gonzalo Isaias | Script de analisis estadistico y dataset |
| P3 - Luis (Revisor QA) | Franco Kaddour | Peer review, comentarios en PR y merge final |

---

## Descripcion del Proyecto

Analisis del registro de ventas anuales de TechStore, empresa ficticia de tecnologia y
equipamiento de oficina. El script procesa el dataset y calcula los siguientes indicadores:

- Total de ingresos del ano
- Producto mas vendido por ingresos generados
- Mes con mayor facturacion
- Grafico de evolucion mensual de ventas

---

## Dataset

**Archivo:** datos/ventas.csv
**Registros:** 20 transacciones - Enero a Noviembre 2024

| Campo    | Descripcion                          | Ejemplo     |
|----------|--------------------------------------|-------------|
| id       | Identificador unico de la venta      | 1           |
| fecha    | Fecha de la transaccion (YYYY-MM-DD) | 2024-01-05  |
| producto | Nombre del producto vendido          | Notebook    |
| cantidad | Unidades vendidas                    | 2           |
| precio   | Precio unitario en pesos             | 85000       |

---

## Estructura del Repositorio

analisis-ventas-techstore/
|-- datos/        -> ventas.csv
|-- scripts/      -> analisis_ventas.py
|-- resultados/   -> resumen_ventas.txt, grafico_ventas.png
|-- README.md
|-- .gitignore

---

## Como ejecutar el script

En Google Colab:
  !git clone https://github.com/FrancoKaddour/analisis-ventas-techstore.git
  %cd analisis-ventas-techstore
  !python scripts/analisis_ventas.py

En local (requiere Python 3 y matplotlib):
  git clone https://github.com/FrancoKaddour/analisis-ventas-techstore.git
  cd analisis-ventas-techstore
  pip install matplotlib
  python scripts/analisis_ventas.py

---

## Trazabilidad con Jira

| Issue  | Descripcion                                      | Responsable    |
|--------|--------------------------------------------------|----------------|
| PROY-1 | Inicializar repositorio y estructura de carpetas | Franco Kaddour |
| PROY-2 | Desarrollar script de analisis y agregar dataset | Gonzalo Isaias |
| PROY-3 | Peer review, documentacion final y merge del PR  | Franco Kaddour |

---

Repositorio desarrollado con fines educativos - UTN TUP Organizacion Empresarial 2026