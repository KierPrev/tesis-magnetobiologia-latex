# Mapa dosis experimental ↔ literatura

> Cruce entre los niveles de la torre de exposición y los 33 resúmenes de `resumenes/`.
> Generado el 29/07/26. Protocolo propio: **1 h de exposición sobre semilla seca**, luego hidratación con 5 mL y germinación 72 h a 25 °C. Variable: cambio porcentual de peso húmedo a las 72 h.

---

## 1. Tres desajustes de diseño que conviene tener presentes

### 1.1 La literatura reporta efecto sobre la *velocidad*, no sobre el punto final

Es el hallazgo más importante del cruce, y el más incómodo.

De la sección 3.1 del `ResumenTotal`:

> «El SMF no siempre aumenta el porcentaje final de germinación cuando las semillas ya tienen alta viabilidad (>90%), pero **acelera consistentemente la velocidad de germinación** (MGT reducido 8–34%).»

Casos concretos donde el punto final **no** cambió pero la velocidad sí:

| Paper | Dosis | Germinación final | Velocidad |
|---|---|---|---|
| Flórez 2007 | 125 mT, 24 h | sin cambio (94–98%) | T10 −29% |
| Martínez 2017 | 125 mT, 24 h | sin cambio (95%) | MGT −8%, T1 −34% |
| Torres 2019a | 50 mT, 1 min | sin cambio (~91%) | MGT −12,4% |
| Shine 2017 | 200 mT, 60 min | +0–10% | velocidad +8–58% |

Mi medición es de **un solo punto temporal** (72 h). Si el tratamiento adelanta la germinación pero a las 72 h todas las bandejas ya llegaron al mismo estado, el diseño es ciego al efecto por construcción.

**Consecuencia:** la medición a tiempos múltiples, que en la bitácora figuraba como «línea futura», pasa a ser candidata a explicación del resultado nulo. Vale discutirlo con Leo y decirlo en la Discusión.

### 1.2 Los niveles de cerámica caen en un régimen que la literatura trata con exposiciones largas

Se identifican dos regímenes:

- **(a)** exposiciones cortas (1–60 min) a intensidades medias-altas (150–250 mT)
- **(b)** exposiciones largas (24 h–crónica) a intensidades moderadas (~125 mT)

Mis niveles de cerámica van de **11,7 a 76,2 mT** con **1 h** de exposición: por debajo del rango de (a) y muy por debajo del tiempo de (b). Es una combinación intensidad-tiempo que casi no está explorada.

El neodimio, en cambio, sí entra en (a) en sus tres primeros niveles.

### 1.3 Campo no uniforme: a favor

Tapia-Belmonte 2023 (meta-análisis, 29 especies): peso fresco **+123% con campo no uniforme** frente a uniforme. Uso imán permanente, o sea campo no uniforme. La inhomogeneidad que cuantifiqué —y que aparecía como limitación— podría no ser un defecto en términos de efecto biológico.

Ojo con la tensión: Torres 2019a, con campo **homogéneo**, encontró inhibición por encima de 150 mT. Los que reportan 200 mT/1 h como óptimo usan imanes (no uniforme). Puede que la discrepancia sea justamente la uniformidad.

---

## 2. Papers sobre absorción de agua — los más cercanos a mi variable

Mido peso húmedo, que mezcla agua embebida con crecimiento. Hay tres trabajos específicamente sobre unión de agua en la semilla:

| Paper | Dosis | Hallazgo | Nivel propio más cercano |
|---|---|---|---|
| Vashisth & Nagarajan 2009 | 100, 200 mT · 1–2 h | sitios de unión débil **+61%**, isotermas de sorción | Neodimio 3 (97 mT) y 2 (160 mT) |
| Torres, Socorro & Hincapié 2018 | 80–200 mT · 10 min | sitios de adsorción totales **+49%** (200 mT), ΔH reducida | Neodimio 2 (160 mT) |
| Vashisth & Nagarajan 2010 | 100, 200 mT · 1–2 h | NMR: T₂c aparece **3 h antes**; α-amilasa +22% | Neodimio 3 (97 mT) |

**Son el punto de comparación más directo que tengo.** Si hay efecto sobre el peso húmedo a 72 h, la vía más plausible es esta, no el crecimiento.

Y notar el detalle del T₂c: el efecto sobre el agua aparece **3 h antes**, no a las 72 h. Refuerza 1.1.

---

## 3. Mapa por nivel — Neodimio norte

| Nivel | \|B\| centro | Papers en esa dosis | Tiempo que usan | Coincidencia con mi 1 h |
|---|---|---|---|---|
| **1** | 253,5 mT | Răcuciu 2006 (50–250, continuo) · Flórez 2007 (250, 24 h) · Shine 2017 (50–250, 30–120 min) | 30 min – continuo | **Buena** con Shine 2017 |
| **2** | 160,2 mT | Aladjadjiyan 2002 (150, 10–30 min) · Torres-Socorro 2018 (80–200, 10 min) · Domínguez-Pacheco 2010 (160, 30–480 min) | 10–480 min | **Buena** |
| **3** | 97,1 mT | Anand 2012 (100, 1–2 h) · Shine & Guruprasad 2012 (100, 1–2 h) · Vashisth & Nagarajan 2009/2010 (100, 1–2 h) · Sharma 2017 (100, 2 h) | **1–2 h** | **Excelente — casi réplica exacta** |
| **4** | 60,0 mT | Ahamed 2013 (57–60, *Capsicum*) | paso único | Débil (otra especie) |
| **5** | 38,6 mT | Siyami 2018 (40, 5–10 min) | 5–10 min | Parcial |
| **6** | 25,9 mT | — | — | **Zona sin cobertura** |
| **7** | 18,1 mT | — | — | **Zona sin cobertura** |
| **8** | 13,0 mT | Radhakrishnan 2019 (revisión, desde 4 mT) | variable | Solo revisiones |

**El nivel 3 (97 mT, 1 h) es prácticamente una réplica de Anand 2012 y Vashisth & Nagarajan 2010.** Si hay un nivel donde esperar señal por precedente directo, es ese. Y si ahí sale nulo, es un nulo informativo: contradice cuatro trabajos con la misma dosis y tiempo.

**Óptimo canónico de la literatura: 200 mT durante 1 h** (Shine & Guruprasad 2012, Vashisth & Joshi 2017, Shine 2017, Kataria 2017). Mis niveles 1 (253) y 2 (160) lo encierran, ninguno lo toca. Sería el argumento para un nivel intermedio si se rediseñara.

---

## 4. Mapa por nivel — Cerámica norte

| Nivel | \|B\| centro | Papers en esa dosis | Tiempo que usan | Coincidencia con mi 1 h |
|---|---|---|---|---|
| **1** | 76,2 mT | Alattar 2021 (70, *Capsicum*, agua) · Torres-Socorro 2018 (desde 80) | continuo / 10 min | Débil |
| **2** | 61,0 mT | Ahamed 2013 (57–60, *Capsicum*) | paso único | Débil (otra especie) |
| **3** | 46,7 mT | Siyami 2018 (40) · Torres 2019a (50, 1 min) · Shine 2017 (desde 50) | 1–10 min | Parcial |
| **4** | 35,1 mT | Siyami 2018 (40, 5–10 min) | 5–10 min | Parcial |
| **5** | 26,3 mT | — | — | **Zona sin cobertura** |
| **6** | 19,8 mT | — | — | **Zona sin cobertura** |
| **7** | 15,1 mT | — | — | **Zona sin cobertura** |
| **8** | 11,7 mT | Radhakrishnan 2019 (desde 4 mT) · Araújo 2016 (desde 0,015 mT) | variable | Solo revisiones |

**Ningún nivel de cerámica tiene un precedente sólido en maíz con 1 h de exposición.** El paper más cercano en intensidad es Siyami 2018 (40 mT) pero con 5–10 min y midiendo rendimiento de grano en campo, no peso a 72 h.

Esto reencuadra el resultado nulo del cerámica: no es que contradiga a la literatura, es que **explora una zona que la literatura no cubrió**. Es un resultado más débil de lo que sería un nulo en el nivel 3 del neodimio, pero también más original.

---

## 5. Cobertura de la literatura vs. mis niveles

```
mT   0    25    50    75   100        150        200        250
     |-----|-----|-----|-----|----------|----------|----------|
lit.       ▁▁▁▁▁▂▂▂▂▂▂▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█████████▓▓▓▓▓▓▓
Cer. 8 7 6 5   4    3    2  1
Neo. 8  7 6  5      4      3           2                  1
```

- **Denso** entre 100 y 250 mT: es donde está el óptimo canónico.
- **Ralo** por debajo de 40 mT: solo revisiones, sin estudios directos en maíz.
- **Seis de mis dieciséis niveles** (cerámica 5–8, neodimio 6–7) caen en la zona sin cobertura.

---

## 6. Para la Discusión: cómo enmarcar un resultado nulo

Ordenado de más a menos defendible:

1. **El diseño mide punto final, la literatura reporta velocidad** (§1.1). Es la explicación más fuerte y está respaldada por cuatro papers donde el punto final no cambió.
2. **La mayoría de los niveles cae fuera del rango explorado** (§5), sobre todo en cerámica.
3. **Desajuste intensidad-tiempo** (§1.2): las dosis bajas de la literatura se aplican 24 h, no 1 h.
4. **Potencia estadística** con n = 9 por condición, ya declarado en el plan de análisis.
5. **Régimen de campo alto vs. RPM** (Sección 3.3 del marco teórico): el mecanismo de pares de radicales es más sensible a campos bajos y satura en campos altos.

El nulo del neodimio nivel 3 sería el más interesante de reportar, porque ahí sí hay precedente directo con la misma dosis y el mismo tiempo.

---

## 7. Papers resumidos y no citados en el documento

Estos doce tienen resumen pero no entrada en `bib.bib`. Los marcados con ★ son los que este cruce vuelve útiles:

- ★ **Sharma_2020_magneto** — revisión de magneto-priming, 125 mT/24 h (régimen (b))
- ★ **DominguezPacheco_2010** — 160 y 560 mT, 30–480 min, maíz
- ★ **Racuciu_SMF** — 50–250 mT continuo, maíz, respuesta proporcional a B
- ★ **Sharma_2017** — 100 mT/2 h en maíz, compara SMF vs PMF
- ★ **Torres_2019b** — segundo trabajo de Torres
- ★ **Rosalba_2014** (Zepeda-Bautista) — 480 mT, rendimiento y *Fusarium*
- ★ **ZeaMais_MFstudy** (2002) — maíz
- **Saletnik_2022_fields** — revisión sobre frutos
- **Ahamed_2013**, **Alattar_2021**, **Odewole_2022** — *Capsicum*, otra especie
- **Dante_2014** — ciclo celular, marco teórico

Los siete con ★ son de maíz y aportan puntos de dosis. Convendría incorporarlos al `bib.bib` para la Discusión.
