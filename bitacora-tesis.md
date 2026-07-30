# Bitácora de la Tesis

> Cosas que voy tirando acá para después agregar al documento final.
> Fecha de creación: 13/05/26
> Última limpieza: 29/07/26 — se quitó todo lo que ya quedó incorporado al documento.

---

## Para la reunión con Leo

### Inhomogeneidad del campo dentro de una misma bandeja

Dispersión de \(|\vec{B}|\) dentro de una misma bandeja, como % del valor en el centro:

| Nivel | Cerámica | Neodimio |
|---|---|---|
| 1 | 24% | **74%** |
| 2 | 8% | 66% |
| 3 | 19% | 60% |
| 4 | 23% | 53% |
| 8 | 21% | 31% |

El cerámica define una dosis bastante bien determinada; el neodimio, mucho menos. Causa geométrica: el cajón tiene semiancho 32,8 mm y la cara del neodimio solo 25,4 mm, así que los compartimentos se salen del imán. En cerámica (100 × 80) entra holgado.

La dispersión relativa **baja con la distancia** en ambos imanes: los niveles altos son más débiles pero más homogéneos. Hay un compromiso intensidad/homogeneidad que vale mencionar en la Discusión.

Gradiente vertical en neodimio nivel 1: −10,5 mT/mm. Sobre una capa de ~5,6 mm, unos 59 mT según cómo caiga el grano.

**Preguntarle a Leo:** ¿conviene rediseñar el cajón para que entre dentro de la cara del neodimio, o reportar el neodimio con la dispersión declarada?

### Explicarle a Leo cómo se ajusta el modelo a lo medido

> Después, tarea de pasarlo al documento. Script: `src/simulate_magnet_field.py`.

**1. Un solo parámetro libre: \(B_r\).** Todo lo demás (dimensiones, geometría) viene medido. Se aprovecha que \(B_z\) es **lineal en \(B_r\)** por superposición: se simula con \(B_r = 1\) mT para obtener un "campo unitario", y el campo real es ese campo unitario multiplicado por \(B_r\).

**2. Mínimos cuadrados con solución cerrada** (`fit_remanence_centro`, líneas 113–131):

```
br_fit = sum(medido * unit) / sum(unit²)
```

Es la fórmula estándar para un ajuste lineal de un parámetro sin ordenada al origen.

**3. Solo se ajusta con el Centro, no con las esquinas.** El Centro está sobre el eje, donde el campo es más uniforme y menos sensible a errores geométricos. Las esquinas —sobre todo en neodimio— caen fuera de la cara, en la zona de campo de retorno, donde \(B_z\) cambia de signo y es hipersensible a la posición exacta y al promediado espacial de la sonda. Si entraran al ajuste contaminarían \(B_r\) con ruido geométrico en vez de reflejar el material.

**4. Las esquinas son validación independiente** (`validate_corners`, líneas 134–147): se mide con \(R^2\) y RMSE qué tan bien el \(B_r\) ajustado en el Centro predice las esquinas, sin retroalimentar el ajuste.

**5. Diagnósticos para cuando algo no cuadra:**

- `sweep_corner_radius` (150–181): barre la posición asumida de las esquinas, para distinguir geometría mal asumida de efecto de borde.
- `sweep_z_offset` (184–213): barre un offset sistemático de distancia, para descartar que un \(B_r\) fuera de rango físico venga de mala calibración de la sonda en vez del material.

El \(B_r\) ajustado (318,95 mT cerámica; 926,28 mT neodimio) es el que después usa `compute_treatment_doses.py` para el campo de cada nivel de la torre.

> **Para explicarle a Leo por qué \(B_r\) no es el campo del imán:** ni siquiera dentro del material \(B\) llega a \(B_r\) (cerámica \(0{,}30\,B_r\), neodimio \(0{,}41\,B_r\) en el centro). \(B_r\) es lo que el material sostendría si el flujo nunca tuviera que salir —un toroide sin entrehierro—. En un imán finito, las líneas se cierran atravesando el propio material en contra de su magnetización, y eso lo baja. Cuanto más chato el imán, más se opone a sí mismo: por eso el cerámica (espesor/ancho 0,30) queda más lejos de \(B_r\) que el neodimio (0,50). Analogía: \(B_r\) es la fem de una pila, lo medido es la tensión en bornes, y la geometría hace de resistencia interna.

### Br del neodimio por debajo del rango físico

El ajuste da \(B_r\) = 926,3 mT, y un neodimio comercial típico está entre 1,1 y 1,4 T.

El script tiene el diagnóstico `--diagnose-offset`, que barre un offset extra de distancia y refitea \(B_r\). La lógica: si un error de calibración de distancia explica el desvío, tiene que existir un offset que **simultáneamente** mejore el RMSE y lleve \(B_r\) a rango físico. Si ningún offset razonable hace las dos cosas a la vez, la causa es otra (material, dimensiones asumidas, calibración del gaussímetro).

```
python3 src/simulate_magnet_field.py --diagnose-offset
```

Falta correrlo, mirar el resultado y discutirlo con Leo.

### Falta el control de la torre de exposición

No se hizo. Nivel de apilamiento y dosis están completamente confundidos con la altura: cualquier gradiente vertical no magnético durante la hora de exposición sería indistinguible del efecto de campo.

Ya quedó escrito como limitación en la Sección 4.5, con las dos atenuantes (exposición breve sobre semilla seca; germinación en sistema aparte y aleatorizado). El control que lo cerraría: apilar los cajones en la torre **sin imán**, replicando el resto del protocolo.

---

## Pendientes del documento

### Secciones vacías

- `discusion.tex` — vacío
- `conclusiones.tex` — vacío
- `apendices.tex` — solo `\appendix`
- `resultados.tex` — solo controles negativos; faltan control positivo, cerámica norte y neodimio norte

### Heatmaps transversales de campo por nivel de tratamiento

**Pendiente de hacer.** Para cada nivel, un mapa del campo en el plano horizontal donde están las semillas (corte $xy$ a la altura de la capa), con la huella del cajón y los cuatro compartimentos superpuestos.

- 8 mapas para cerámica + 8 para neodimio.
- **En el documento va uno solo** — el más ilustrativo, probablemente neodimio nivel 1, que es donde la inhomogeneidad es máxima y donde se ve que los compartimentos se salen de la cara del imán.
- **Los 15 restantes van al apéndice.**

Es lo que falta para cerrar el argumento de homogeneidad: hoy está la dispersión como intervalo min–max en las tablas y en la figura de la torre, pero no se ve *dónde* dentro del cajón cae cada valor. El heatmap muestra si el gradiente es radial, si los cuatro compartimentos son equivalentes entre sí, y cuánto difiere el compartimento vacío de los tres usados.

Los datos ya salen de `compute_treatment_doses.py`; habría que agregar un script que evalúe la grilla $xy$ completa y la dibuje.

### Régimen de campo: marco teórico vs. imanes usados (para la Discusión)

El marco teórico (Sección 3.3) explica que el RPM es altamente sensible en **campos bajos (~1 mT)** y tiende a la saturación o a comportamiento no lineal en **campos altos**. Los imanes usados exponen a **cientos de mT** — régimen de campo alto.

Conectar explícitamente esa distinción en la Discusión. Si los resultados muestran respuestas no monótonas —o nulas—, la justificación teórica del capítulo 3 es la herramienta para explicarlo. No es excusa post-hoc: ya está escrita antes de los resultados.

### Menor

- El resumen (116 palabras) no refleja el contenido actual: no menciona la caracterización ni la simulación.
- Compilar **dos veces** antes de mandar el PDF, si no quedan los `??`.

---

## Higiene de datos

### Registro de temperatura faltante

`temps.csv` existe **solo** para el experimento del 31/03.

Importa porque el efecto de experimento en cerámica es enorme (56,4% → 47,8% → 44,0%, \(F_{2,70} = 62{,}2\)) y la explicación natural sería térmica (marzo vs. junio en San Luis), pero sin datos no se puede testear. Registrar temperatura en los experimentos que queden.

### Procedencia de los pesos del 3er control positivo (20260603)

**Pendiente de aclarar.** Los 15 `post_weight` de ese experimento tenían 6–7 decimales, cuando la balanza da 3. Redondeados a 3 el 29/07 (cambio máximo 0,0005 g, irrelevante numéricamente).

Pero antes de redondear quedó a la vista algo que sí importa: **el resto sobre los 3 decimales era exactamente constante dentro de cada nivel de agua**, sin ninguna variación:

| `treatment_floor` | agua | resto |
|---|---|---|
| 1 | 2 mL | 0,9625 |
| 2 | 5 mL | 0,6625 |
| 3 | 6 mL | 0,5125 |

Eso no puede provenir de una balanza: prueba que a cada bandeja se le sumó o restó **una constante propia de su nivel de agua**. Y esa constante está confundida con la variable que el experimento estudia.

Lo verificado: el archivo entró al repo ya así (commit `bf278ac`, «tercer control positivo»), y ningún script del repo escribe `post_weight` en `trays.csv` —todos escriben en `processed/`—, así que los valores se cargaron corregidos desde afuera.

Hipótesis: se pesó el conjunto y se le restó una tara de bandeja + papel húmedo medida una sola vez por nivel de agua. Con el método de tara actual (tarar con el cajón cargado y retirar las semillas) eso no haría falta, así que podría ser un protocolo anterior. **Los otros dos controles positivos tienen 3 decimales limpios, o sea que no recibieron el mismo tratamiento.**

Importa porque el control positivo es lo que acredita la sensibilidad del ensayo, y eso es lo que le da valor informativo a cualquier resultado nulo. El original está en git (`git show bf278ac:data/experiments/20260603/trays.csv`).

### Bandeja 20260522_A9 — resuelto

`pre_weight == post_weight == 3,557` (ganancia nula, fallo experimental). El `notebookControlPositivo.ipynb` ya la excluía explícitamente, así que las conclusiones del control positivo no estaban afectadas. El 29/07 se vació el `post_weight` en el CSV para que la exclusión valga en cualquier análisis, conservando la fila como registro de que la bandeja existió.

### Inconsistencias en `experiments_metadata.csv`

- `20260701` figura en el metadata pero **no tiene carpeta**. O falta la carpeta, o sobra la fila.
- `20260721` está tipado `IMAN_NEODIMIO` con `magnet_pole = NONE`. O es un control, o le falta el polo.

### Pipeline sin correr

`processed/` vacío en los tres controles positivos, en el 22/06 (3er cerámica) y en todos los de neodimio.

---

## Estado de experimentos (al 29/07/26)

| Condición | Estado |
|---|---|
| Control negativo | 3/3 hecho |
| Control positivo (poca/media/mucha agua) | 3/3 hecho |
| Imán cerámica norte | 3/3 hecho |
| Imán neodimio norte | 2 hechos, 3ro se retira el jueves 30/07 |
| Imán neodimio sur | a definir tras resultados de neodimio norte |

Deadline experimentos presenciales: **octubre 2026**.

---

## Decisiones de diseño y análisis

- Los pisos de germinación se rotan al azar → el efecto de piso detectado en controles negativos (A > B > C) queda promediado, no confunde el tratamiento.
- Cada experimento de 27 bandejas incluye **3 bandejas no tratadas** (control interno), que no entran a la torre de exposición.
- Contraste principal: tratado vs. sus 3 controles internos (mismo día, mismo lote). Los 81 controles negativos combinados quedan como referencia de variabilidad basal y validación.
- Variable medida: peso húmedo (seco antes, húmedo a 72 h). Limitación conocida: mezcla agua embebida con crecimiento real. Peso seco final no es viable (requiere horno). Medición a tiempos múltiples queda como línea futura, no para esta tesis.
