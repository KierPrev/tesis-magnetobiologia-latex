# Effect of Static Magnetic Fields on *Zea mays* Germination

**Undergraduate thesis (Licenciatura en Física) — Universidad Nacional de San Luis**
Laboratorio de Magnetobiología (MBLab), Departamento de Física
Thesis student: Kiernan Elizabeth Preve · Director: Leonardo Makinistián · Co-director: Daniel Guerreiro

> 🚧 Work in progress — experimental phase ongoing, expected completion late 2026.

## Overview

This thesis investigates whether static magnetic fields affect germination and early growth in corn (*Zea mays*) seeds, a question in **magnetobiology** connected to the radical pair mechanism. Seeds were exposed to permanent magnets (ferrite ceramic and neodymium) during the first 72 hours of germination, and growth was quantified as percentage change in wet weight.

The experimental design prioritizes statistical rigor over anecdotal effect: three independent 72-hour negative-control runs (n = 81 trays total) were used to characterize the spatial variability of the setup itself before any treatment comparison, followed by systematic treatment experiments with estimated effect sizes and statistical significance.

## What's in this repo

Beyond the written thesis, this project required building the experimental infrastructure from scratch:

- **Physical setup** — 3D-printed (Tinkercad / build123d) sample holders and containment structures designed for reproducible magnet exposure.
- **Magnetic characterization** — experimental and numerical characterization of the ferrite and neodymium magnets used for treatment.
- **Image acquisition pipeline** — a purpose-built system for standardized image capture of seed trays, used to track growth over time.
- **Data analysis tooling** — custom software to automate sample organization and statistical analysis of results.

## Structure

```
secciones/          thesis chapters (intro, theory, methods, results, discussion, conclusions)
datos/               experimental data
resumenes/           summaries / working notes
marco teorico/       background material and reference papers
bitacora-tesis.md    lab notebook / progress log
tesis.tex, tesis.pdf full compiled thesis
```

## Abstract

The effect of static magnetic fields on the germination and early growth of *Zea mays* seeds was assessed. Three independent 72-h negative-control experiments (n = 81 trays in total) were carried out to characterise the spatial variability of the experimental setup, followed by treatment experiments using north-pole ferrite ceramic magnets, with the seeds exposed during the first 72 h of germination. The primary response variable was the percentage change in wet weight.

The study aimed to identify exposure conditions associated with improvements in early growth variables, prioritising a systematic, controlled and quantitative experimental design. Effect sizes, statistical significance and reproducibility of the results were estimated under controlled germination conditions.

**Keywords:** magnetobiology, magnetopriming, static magnetic field, *Zea mays*, germination, radical pair mechanism.

---

## Resumen (español)

Se evaluó el efecto de campos magnéticos estáticos sobre la germinación y el crecimiento inicial de semillas de *Zea mays*. Se realizaron tres controles negativos de 72 h cada uno (n = 81 bandejas en total) para caracterizar la variabilidad espacial del sistema experimental, seguidos de experimentos con imanes cerámicos de ferrita en configuración polo norte, exponiendo a las semillas durante las primeras 72 h de germinación. La variable principal de análisis fue el cambio porcentual en peso húmedo.

El estudio buscó identificar condiciones asociadas a mejoras en variables de crecimiento temprano, priorizando un diseño experimental sistemático, controlado y cuantitativo. Se estimaron tamaño de efecto, significancia estadística y reproducibilidad de los resultados bajo condiciones controladas de germinación.

**Palabras clave:** magnetobiología, magnetopriming, campo magnético estático, *Zea mays*, germinación, mecanismo de pares de radicales.
