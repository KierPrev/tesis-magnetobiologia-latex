"""
Campo magnetico en el centro geometrico de cada compartimento del cajon.

Complementa el calculo de dosis por nivel de la torre de exposicion:
mientras el valor nominal se evalua sobre el eje del iman (donde no hay
semillas, por coincidir con la arista entre los cuatro compartimentos),
este script evalua |B| en el centro geometrico de un compartimento.

Los cuatro compartimentos son equivalentes por simetria de reflexion
respecto de los dos planos verticales que contienen al eje, aun cuando
la cara del iman de ceramica sea rectangular.

NOTA: este archivo esta pensado para integrarse al repositorio
tesis-magnetobiologia-software, junto a los demas scripts de dosis.
Mover alli y reutilizar el modelo/Br ya definidos en el pipeline en
lugar de las constantes hardcodeadas de abajo.

Requiere: magpylib >= 5 (unidades SI).
"""

import numpy as np
import magpylib as magpy

# --- Geometria y remanencias ajustadas (Tablas de dimensiones y de ajuste) ---
IMANES = {
    "ceramica_n": dict(dimension_mm=(100.0, 80.0, 30.5), Br_mT=318.9),
    "neodimio_n": dict(dimension_mm=(50.8, 50.8, 25.3), Br_mT=926.3),
}

# Altura del centro de la capa de semillas sobre la cara del iman, por nivel
ALTURAS_MM = [5.3, 15.1, 24.9, 34.7, 44.5, 54.3, 64.1, 73.9]

# Huella del cajon: 65.56 mm de lado, cuatro compartimentos en arreglo 2x2.
# El centro de cada uno queda a un cuarto del lado respecto del eje.
LADO_CAJON_MM = 65.56
D_COMPARTIMENTO_MM = LADO_CAJON_MM / 4  # 16.39 mm


def fuente(nombre):
    m = IMANES[nombre]
    a, b, c = m["dimension_mm"]
    return magpy.magnet.Cuboid(
        polarization=(0.0, 0.0, m["Br_mT"] * 1e-3),        # T
        dimension=(a * 1e-3, b * 1e-3, c * 1e-3),          # m
    ), c


def campo_mT(src, x_mm, y_mm, z_mm):
    """B en mT en el punto dado (mm), con origen en el centro del iman."""
    return src.getB((x_mm * 1e-3, y_mm * 1e-3, z_mm * 1e-3)) * 1e3


def tabla(nombre, d_mm=D_COMPARTIMENTO_MM):
    src, espesor = fuente(nombre)
    filas = []
    for nivel, h in enumerate(ALTURAS_MM, start=1):
        z = espesor / 2 + h                      # cara del iman en z = c/2
        B_eje = campo_mT(src, 0.0, 0.0, z)
        B_com = campo_mT(src, d_mm, d_mm, z)
        n_eje = np.linalg.norm(B_eje)
        n_com = np.linalg.norm(B_com)
        filas.append(dict(
            nivel=nivel, altura_mm=h,
            Bz_eje=B_eje[2], modB_eje=n_eje,
            Bz_comp=B_com[2], modB_comp=n_com,
            ratio=n_com / n_eje,
        ))
    return filas


def sensibilidad(nombre, d_min=15.5, d_max=17.5):
    """Variacion relativa maxima de |B| al mover d dentro del rango dado."""
    ref = {f["nivel"]: f["modB_comp"] for f in tabla(nombre)}
    peor = 0.0
    for d in (d_min, d_max):
        for f in tabla(nombre, d_mm=d):
            peor = max(peor, abs(f["modB_comp"] - ref[f["nivel"]]) / ref[f["nivel"]])
    return peor


if __name__ == "__main__":
    for nombre in IMANES:
        print(f"\n== {nombre}  (d = {D_COMPARTIMENTO_MM:.2f} mm)")
        print(f"{'Niv':>3} {'h(mm)':>7} {'Bz eje':>8} {'|B| eje':>8} "
              f"{'Bz comp':>9} {'|B| comp':>9} {'ratio':>7}")
        for f in tabla(nombre):
            print(f"{f['nivel']:>3} {f['altura_mm']:>7.1f} {f['Bz_eje']:>8.2f} "
                  f"{f['modB_eje']:>8.2f} {f['Bz_comp']:>9.2f} "
                  f"{f['modB_comp']:>9.2f} {f['ratio']:>7.3f}")
        print(f"  sensibilidad a d en [15.5, 17.5] mm: "
              f"{sensibilidad(nombre) * 100:.1f}% maximo")
