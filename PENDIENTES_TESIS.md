# Pendientes del documento de tesis

Qué falta **escribir** en `tesis.tex` y sus secciones, y qué falta **calcular**
antes de poder escribirlo. Complementa a
`../tesis-magnetobiologia-software/INVENTARIO_RESULTADOS.md`, que dice qué datos y
figuras existen hoy.

Ordenado por dependencia. Estado al 2026-10-15.
Convención: `[ ]` pendiente · `[~]` parcial · `[x]` hecho

> **Atención**: el inventario quedó desactualizado en dos puntos importantes por
> lo que se descubrió el 2026-10-15 (regímenes de agua y experimentos
> reincorporados). Ver Etapa 0.

---

## Lo que se descubrió el 2026-10-15

Tres hechos que no estaban registrados en ningún archivo y que reordenan el
trabajo.

### 1. Hay dos regímenes de agua, y no están en los datos

| Campaña | Fechas | Agua | Condición |
|---|---|---|---|
| Cerámica N | 20260331, 20260608, 20260622 | **5 mL** | saturación |
| Neodimio N | 20260626, 20260721, 20260727 | **5 mL** | saturación |
| Neodimio N | 20260804, 20260907, 20260911 | **3 mL** | **estrés hídrico** |
| Control negativo | 20260404, 20260428, 20260507 | **5 mL** | saturación |
| Control positivo | 20260518, 20260522, 20260603 | 2 / 5 / 6 mL | por bandeja |

El cambio a 3 mL se decidió **a posteriori**, después de que cerámica diera nulo,
con el razonamiento de que bajo saturación de agua tal vez no se vea un efecto.
Está alineado con la subsección de Antecedentes *Efectos bajo estrés abiótico*.

**Ni `experiments_metadata.csv` ni los `trays.csv` registran el agua aplicada.**
El factor más influyente del ensayo (+0,064 de imbibición por mL según el control
positivo) no existe en los datos.

### 2. Los tres experimentos "descartados" son válidos

20260626, 20260721 y 20260727 figuraban como descartados en el inventario. Son
Neodimio N a 5 mL, válidos, y se habían dejado afuera porque no mostraron cambios
significativos — que es selección por resultado y no un criterio admisible.

Por los datos disponibles son **el mejor grupo de imán del proyecto**:

| Fecha | Imán | Agua | Control | Todas | SD | Bloques |
|---|---|---|---|---|---|---|
| 20260331 | Cerámica | 5 mL | 0,538 | 0,564 | 0,035 | **no balanceados** |
| 20260608 | Cerámica | 5 mL | 0,512 | 0,478 | 0,050 | |
| 20260622 | Cerámica | 5 mL | 0,414 | 0,440 | 0,034 | |
| 20260626 | Neodimio | 5 mL | 0,470 | 0,475 | 0,041 | completos |
| 20260721 | Neodimio | 5 mL | 0,482 | 0,478 | 0,031 | completos |
| 20260727 | Neodimio | 5 mL | 0,509 | 0,490 | 0,025 | completos |
| 20260804 | Neodimio | 3 mL | 0,378 | 0,381 | 0,016 | completos |
| 20260907 | Neodimio | 3 mL | 0,378 | 0,381 | 0,011 | completos |
| 20260911 | Neodimio | 3 mL | 0,371 | 0,381 | 0,008 | completos |

Sus controles van 0,470 / 0,482 / 0,509 (rango 0,039) contra 0,538 / 0,512 /
0,414 de cerámica (rango 0,124): tres veces más consistentes. Diseño completo y
balanceado, que cerámica no tiene. Solo tienen **imbibición**: sin conteo de
germinación y sin fotos.

El metadata de 20260721 ya fue corregido a `magnet_pole = N`.

### 3. Con ellos, el diseño se completa

|  | 5 mL (saturación) | 3 mL (estrés) |
|---|---|---|
| **Cerámica N** | 20260331, 20260608, 20260622 | — |
| **Neodimio N** | 20260626, 20260721, 20260727 | 20260804, 20260907, 20260911 |

Esto habilita dos comparaciones que hoy son imposibles:

- **Mismo agua (5 mL), dos imanes** → comparación limpia de tipo de imán.
- **Mismo imán (neodimio), dos aguas** → responde la pregunta que motivó el
  cambio de protocolo: *¿el efecto del imán es mayor bajo estrés hídrico?*

Hasta ahora esa comparación no se podía hacer, porque imán y agua cambiaban juntos.

### Sobre la línea de base: no hay deriva, hay variabilidad entre fechas

El escalón entre 5 mL y 3 mL es el agua, por diseño: contra la curva del control
positivo, 3 mL predice ~0,40 y lo observado es 0,376.

Agrupando por régimen, la línea de base es reproducible: las medias de los
controles de los dos grupos de imán a 5 mL son **0,4878** (cerámica) y **0,4872**
(neodimio), con imanes y meses distintos.

Pero **dentro del régimen de 5 mL no hay ninguna tendencia temporal**. Incluyendo
los controles negativos, que también fueron a 5 mL:

| Fecha | Grupo | Control | Todas |
|---|---|---|---|
| 20260331 | cerámica | 0,538 | 0,564 |
| 20260404 | ctrl negativo | 0,385 | 0,425 |
| 20260428 | ctrl negativo | 0,377 | 0,418 |
| 20260507 | ctrl negativo | 0,460 | 0,438 |
| 20260608 | cerámica | 0,512 | 0,478 |
| 20260622 | cerámica | 0,414 | 0,440 |
| 20260626 | neodimio | 0,470 | 0,475 |
| 20260721 | neodimio | 0,482 | 0,478 |
| 20260727 | neodimio | 0,509 | 0,490 |

Rebota entre 0,377 y 0,538 sin dirección. **No hay deriva del sistema**: hay
variabilidad entre fechas a agua constante, que es exactamente lo que el bloqueo
por fecha absorbe. Cada media de control se apoya en solo 3 bandejas (SE ≈ 0,02),
así que las diferencias puntuales entre fechas no deben sobreinterpretarse.

Queda descartada la hipótesis de envejecimiento del lote que se había planteado
antes de conocer los regímenes de agua.

### 20260804 es una discontinuidad de protocolo, no solo de agua

Cuatro cosas cambiaron juntas en esa fecha:

1. Agua 5 → 3 mL
2. **La dosificación se volvió exacta.** En las tandas anteriores se usó una
   cuchara que entregaba un volumen aproximadamente constante, no 20 semillas
   contadas
3. Empezó el conteo de germinación (aparece la columna `no_germinadas`)
4. Aparecen las fotos a 16 MP

El CV del peso seco por bandeja lo confirma:

| Grupo | CV del peso seco | Rango dentro de la fecha |
|---|---|---|
| Neodimio 3 mL | **2,5–3,2%** | 0,38–0,54 g |
| Cerámica 5 mL | 3,2–5,7% | 0,54–0,87 g |
| Control negativo 5 mL | 5,4–7,3% | 0,96–1,24 g |
| Neodimio 5 mL | **6,0–10,1%** | 1,25–1,73 g |

Con 20 semillas exactas el CV esperado de la bandeja es el CV de una semilla sobre
√20, o sea 2,2–3,4% para un CV de semilla del 10–15%. Neodimio 3 mL cae justo
ahí: conteo exacto. Los demás están por encima: dosificación volumétrica. En
neodimio 5 mL el rango llega a 1,73 g, unas ±4 semillas entre bandejas.

**Consecuencias para el texto:**

- La comparación 5 mL vs 3 mL **no es una comparación de agua sola**: las dos
  condiciones difieren también en el protocolo de armado. El test de interacción
  (p=0,30) es válido —los dos efectos son estimaciones no sesgadas de lo que pasó
  en cada régimen— pero el resultado no se puede atribuir al agua aisladamente.
  Hay que declararlo explícitamente
- Explica los errores estándar: 2,42% a 5 mL contra 1,20% a 3 mL, y el efecto
  mínimo detectable de 6,87% contra 3,40%. Dosificación más precisa, menos
  varianza residual
- `analisis_confirmatorio.py:44` tiene `N_SEMILLAS = 20` hardcodeado y calcula
  `germinadas = 20 − no_germinadas`. **Solo las tres fechas de neodimio 3 mL
  tienen germinación, y son justamente las de conteo exacto**, así que el
  denominador es correcto. Conviene dejarlo escrito para que nadie extienda la
  germinación a las tandas de cuchara sin advertirlo
- La sección de *Materiales y métodos* del dispositivo de dosificación tiene que
  decir que en las tandas de cuchara el número de semillas por bandeja era
  nominal, no exacto, y que la normalización por peso inicial es lo que hace
  comparables las bandejas

**Queda una caída dentro de cerámica, a 5 mL constantes**: 0,538 → 0,512 → 0,414.
La acompaña un aumento del 10% del peso seco por bandeja (3,67 → 4,04 g) con el
peso final casi quieto (5,73 → 5,81 g); agrupando la campaña, la imbibición
correlaciona con el peso seco en r = −0,57. Tiene sentido mecánico (con 5 mL fijos
el agua disponible está acotada), pero **dentro de cada fecha** las correlaciones
son inconsistentes (−0,42, −0,17, **+0,11**), así que con tres fechas no se puede
separar la carga seca de otros factores temporales. Se declara como limitación; el
bloqueo por fecha la absorbe. Neodimio no tiene este problema: peso seco constante
y r = −0,07.

- [x] **Verificar**: ¿por qué subió el peso seco por bandeja en cerámica? Son 20
      semillas contadas, así que es variación de masa por semilla o del dosificador.
- [x] Estos números se calcularon sobre los `trays.csv`, no salen de ningún
      `reporte.txt`. Decidir si se agregan al pipeline o se documentan en
      Reproducibilidad.

---

## Etapa 0 — Registrar el agua y recalcular `[~]`

**Toca el repositorio de software.** Bloqueaba todo lo demás. Hecho el 2026-10-15,
salvo los tres últimos ítems.

- [x] Columna `water_ml` en `data/experiments_metadata.csv`
- [x] `water_ml` en `METADATA_FIELDNAMES` de `src/Asignador.py`, con validador
      `normalizar_water_ml` (acepta vacío) y pregunta en el prompt de carga.
      **Sin esto el próximo experimento cargado borraba la columna en silencio**
- [x] `water_ml` en `METADATA_COLUMNS` de `src/AnalisisTrays.py` (queda fuera de
      las obligatorias para no romper metadata viejo)
- [x] `agrupar_por_tipo` de `src/analisis_confirmatorio.py` agrupa ahora por
      `(experiment_type, magnet_pole, water_ml)`; un grupo sin agua declarada se
      omite con aviso en vez de analizarse mal
- [x] Salidas separadas: `confirmatorio_ceramica_n_5ml`,
      `confirmatorio_neodimio_n_5ml`, `confirmatorio_neodimio_n_3ml`
- [x] Flag `--fechas` en el script (antes la selección era solo por TUI
      interactiva, lo que impedía reproducir una corrida desde la línea de comandos)
- [x] **Arreglado un error de sintaxis preexistente en `src/AnalisisTrays.py`**:
      la línea `) -> tuple[pd.DataFrame, list[str]]:` estaba duplicada y el script
      no compilaba. Es el script que genera todas las figuras del control negativo
      que ya están en la tesis y el que `tab:repro` declara como su generador
- [x] Verificado que los reportes de cerámica y de neodimio 3 mL quedan
      **byte a byte idénticos** a los anteriores
- [x] Llevar el test de interacción al pipeline (hoy está en un script suelto)
- [x] `comparativa_dosis_respuesta` retirada del documento: juntaba dos regímenes
      de agua en un mismo modelo, asi que el coeficiente de imán no era
      interpretable. Su lugar lo ocupa el test de interacción (Sección 2.8).
      Queda pendiente decidir si se la quita del pipeline o se la separa por régimen
- [x] Actualizar `INVENTARIO_RESULTADOS.md`: dice que 20260626/0721/0727 están
      descartados, no menciona los regímenes de agua ni los directorios nuevos
- [x] Agua de los controles negativos: **5 mL**, ya cargada en el metadata
- [x] Borrar los directorios viejos `confirmatorio_ceramica_n/` y
      `confirmatorio_neodimio_n/` una vez que nada los referencie

---

## Etapa 1 — Reparar Materiales y métodos `[x]`

El Plan de análisis estadístico describe un análisis que no es el que se corrió.

- [x] Declarar los tres endpoints (imbibición, germinación, radícula) y la bandeja
      como unidad experimental
- [x] **Declarar el agua como factor del diseño**: dos regímenes, 5 mL y 3 mL, con
      el razonamiento del estrés hídrico y la referencia a Antecedentes
- [x] **Declarar que el régimen de 3 mL se agregó a posteriori**, después del
      resultado nulo de cerámica. Es legítimo y declararlo protege el valor del
      TOST; presentarlo como planificado no lo sería. El plan de análisis sí fue
      pre-especificado antes de ver los datos de neodimio: las dos cosas son
      compatibles y conviene decirlo explícitamente
- [x] Reescribir *Alcance efectivo de la medición de radículas* (dice que la
      fotografía se discontinuó; Neodimio N 3 mL tiene las 3 fechas, n=77)
- [x] Reconciliar la estructura del contraste con el modelo de bloques `C(bloque)`
- [x] Cambiar Benjamini-Hochberg por Holm (es lo que usa el pipeline). Es Holm lo
      que decide que el nivel 3 no sea un hallazgo
- [x] Sección propia para los experimentos de control positivo (n=38, 2/5/6 mL).
      Tiene doble rol: acredita la sensibilidad del ensayo **y** es la curva de
      calibración que permite ubicar el régimen de 3 mL
- [x] Reescribir el párrafo de potencia e introducir TOST y el margen de ±10%
      (+ citas de Schuirmann 1987 y Lakens 2017 en `bib.bib`, hoy no hay ninguna)
- [x] Declarar las limitaciones de Cerámica N: Shapiro p=0,0003, bloques no
      balanceados, y la caída de línea de base dentro de la campaña
- [x] Declarar las variables no registradas: agua (hasta que se corrija) y
      temperatura, registrada solo en 20260331 y 20260608 de 6 fechas. La cámara
      es termostatizada a 25 °C con control PID: setpoint declarado, registro parcial
- [x] **Declarar la reincorporación de 20260626/0721/0727** y por qué: la
      exclusión original se basaba en el resultado, no en una falla de protocolo
- [x] Fijar la nomenclatura: **nivel de tratamiento = 1–9**, **piso = A/B/C**
      (el inventario usa "piso" para 1–9, al revés: no copiar de ahí)

---

## Etapa 2 — Capítulo de Resultados `[x]`

Hoy `secciones/resultados.tex` tiene 282 líneas dedicadas **exclusivamente** al
control negativo. No hay ni una línea sobre los experimentos de imán ni sobre el
control positivo.

Orden propuesto: el control positivo va **primero**, para que el lector llegue al
resultado nulo sabiendo que el instrumento mide.

- [x] 2.1 Control positivo (n=38; +0,064 por mL, p=2,9e-07, R² aj. 0,59;
      contrastes 2 vs 5 mL Holm=0,004 y 2 vs 6 mL Holm=8,4e-05)
- [x] 2.2 Control negativo (ya escrito, reubicar en el orden del capítulo)
- [x] 2.3 Cerámica N, 5 mL (n=81; +1,43%, IC95 [−4,32; +7,18], p=0,62;
      TOST p=0,002; MDE 8,19%)
- [x] 2.4 Neodimio N, 5 mL — **grupo nuevo, ya calculado** (n=81; **−1,46%**,
      IC95 [−6,28; +3,36], p=0,55; **TOST p=0,00037 → equivalente**; MDE 6,87%;
      bloques completos y balanceados; `C(bloque)` F=1,08 p=0,39; sin tendencia
      dosis-respuesta p=0,74; Shapiro p=0,025). Solo imbibición
- [x] 2.5 Neodimio N, 3 mL — imbibición (n=81; +1,59%, IC95 [−0,80; +3,98],
      p=0,19; TOST p<1e-5; MDE 3,40%)
- [x] 2.6 Neodimio N, 3 mL — germinación (n=81; +6,2 pp, IC95 [−2,0; +14,5], p=0,14)
- [x] 2.7 Neodimio N, 3 mL — radícula (n=77; +0,60 mm = +9,3%, p=0,32; MDE 26,4%)
- [x] 2.8 **Comparación de regímenes — ya calculada.** Mismo imán (neodimio N),
      dos niveles de agua. Efecto del imán: **−1,46% a 5 mL** (SE 2,42%) y
      **+1,59% a 3 mL** (SE 1,20%). Término de interacción
      `con_iman:C(agua)`: coef −0,0131, SE 0,0126, t=−1,04, **p=0,30**, IC95
      absoluto [−0,038; +0,012].
      **No hay evidencia de que el estrés hídrico modifique el efecto del imán.**
      Es la respuesta directa a la hipótesis que motivó el cambio de protocolo, y
      conviene que cierre el capítulo.
      **Declarar el límite**: las dos condiciones difieren en el agua y también en
      el protocolo de armado (ver la discontinuidad del 20260804), así que el
      resultado nulo no se atribuye al agua aisladamente

### Cuidados al escribir

- **Nunca** presentar el nivel 3 (77 mT) como hallazgo: radícula p=0,012 crudo
  pero **Holm=0,093**. Es hipótesis a testear.
- `fig_radicula_boxplot.pdf` **no está en mm absolutos**: el eje Y es desvío
  respecto del bloque. Si se citan mm, tomarlos del `reporte.txt` (control = 6,42 mm).
- `pct_change` es **imbibición**, no biomasa.
- El coeficiente de imán de `comparativa_imanes` (−0,112, p<0,001) **no es un
  efecto del imán**: era la diferencia de régimen de agua. Esa figura hay que
  rehacerla o retirarla.
- Usar siempre el `.pdf` de cada figura, nunca el `.png`.

---

## Etapa 3 — Discusión `[x]`

- [x] Qué mide un control negativo (analogía de Young y las ratas, Feynman)
- [x] El estrés hídrico como hipótesis y su respuesta
- [x] Interpretación del resultado nulo: equivalencia, no ausencia de evidencia
- [x] El efecto espacial: en Neodimio N 3 mL, agregar `position` al modelo baja el
      efecto de +1,59% a +0,52%. Es exactamente el efecto espacial que el control
      negativo había caracterizado — cierra el círculo con la sección de Feynman
- [x] La línea de base y el registro de variables: qué se aprende de que el factor
      más influyente del ensayo (el agua) no estuviera registrado, y de que el
      20260804 cambiara cuatro cosas a la vez. Es la continuación natural de la
      sección de Feynman: no es un resultado sobre imanes, es un resultado sobre el
      aparato. **Encuadre correcto**: no hay deriva temporal del sistema, hay
      variabilidad entre fechas a agua constante (0,377–0,538), que el bloqueo
      absorbe
- [x] Contraste con la literatura de magnetopriming (usar `resumenes/`)
- [x] Limitaciones y líneas futuras. Está ya escrito el párrafo del control de
      apilamiento que falta (torre sin imán); 20260721 **no** sirve para eso, es
      neodimio N

---

## Etapa 4 — Conclusiones, Resumen y Abstract `[x]`

- [x] `secciones/conclusiones.tex` — hoy son 9 líneas con un `\pendiente{}`
- [x] `secciones/resumen.tex` — Resumen y Abstract hablan solo de controles
      negativos y de *"imanes cerámicos de ferrita"*: no mencionan neodimio, ni
      germinación, ni radícula, ni el estrés hídrico, y no dan ningún resultado.
      Reescribir enteros

---

## Etapa 5 — Cierre del documento `[~]`

- [x] Descomentar en `tesis.tex` los `\include` de `discusion` y `conclusiones`
- [x] Descomentar `reproducibilidad` — **está terminado**, solo falta incluirlo
- [x] Agregar a la tabla `tab:repro` las filas de las figuras de imán y de control
      positivo (hoy solo lista control negativo y caracterización de campo)
- [ ] Actualizar los hashes de commit de `tab:repro` al cerrar la versión final
- [x] **PNG vs PDF**: `resultados.tex` incluye los `.png` del control negativo,
      pero `reproducibilidad.tex` declara `.pdf` para esas mismas figuras, que
      *solo existen como PNG* y no están versionadas (`.gitignore` bloquea
      `*.png`). En un clon limpio no compila
- [ ] Decidir si van **Apéndices** (`apendices.tex` es solo un `\pendiente{}`)
- [ ] Decidir si va `agradecimientos` (existe, está comentado)
- [x] Revisar epígrafes: el criterio del preámbulo dice 3 o 4 en toda la tesis y
      **ninguno en Resultados**

---

## Etapa 6 — Pasada de prosa sobre el resto del documento `[~]`

Criterio acordado: explicar cada término técnico la primera vez que aparece, usar
preguntas como señales para guiar al lector, y sacar las fórmulas rituales
(«corresponde señalar», «por lo tanto», «no obstante»). El objetivo es que lo
pueda leer un estudiante de licenciatura y también un jurado.

La métrica útil no es el largo de las frases ---ya eran más cortas que las del
texto previo--- sino la **densidad de jerga sin explicar**. En los pasajes ya
pasados bajó de 9,3 a 4,9 por mil palabras en Resultados y de 10,6 a 4,6 en el
plan de análisis.

- [x] Pasajes propios más densos de Materiales y métodos y Resultados
- [x] Criterio de inclusión y escalas de radícula
- [ ] Pasajes propios que quedan: control positivo en Resultados, las tres
      subsecciones por grupo, sensibilidad de radícula, comparación entre imanes
      y síntesis del capítulo (~2.500 palabras)
- [ ] **Materiales y métodos, secciones previas** (~7.000 palabras)
- [ ] **Resultados, capítulo del control negativo** (~1.800 palabras)
- [ ] **Antecedentes** (~1.968 palabras)
- [ ] **Introducción** (~271 palabras)
- [ ] **Marco teórico** (~2.060 palabras). **Decidir con cuidado**: contiene
      derivaciones físicas y una reescritura mal hecha puede introducir errores
      de contenido, no solo de estilo. Conviene dejarlo último, o no tocarlo

---

## Verificación final

```bash
# 1. Solo deben quedar los \pendiente{} deliberados
grep -n "pendiente{" secciones/*.tex | grep -v "newcommand\|pendientesoff"

# 2. El lote es el mismo en todos los experimentos: no atribuir nada a "lotes"
grep -rin "lote" secciones/*.tex

# 3. Compilar (pausar la sincronización de MEGA antes)
latexmk -xelatex tesis.tex     # sin errores y sin referencias ??
latexmk -c

# 4. Los dos repos se commitean por separado
git -C . status
git -C ../tesis-magnetobiologia-software status
```

Además: **cada número escrito en el documento tiene que poder señalarse en un
`reporte.txt`** de `data/analysis/`.

Antes de entregar, descomentar `\pendientesoff` en el preámbulo de `tesis.tex`
para ocultar los marcadores rojos que queden.
