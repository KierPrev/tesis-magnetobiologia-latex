# ============================================================
#  Configuración de compilación
#
#  Deliberadamente mínima: los auxiliares quedan junto a las fuentes.
#  Se intentó mandarlos a build/ con $out_dir para esquivar a MEGA, pero
#  esa configuración agregaba varias piezas (emulate_aux, make_path,
#  BIBINPUTS) y resultaba frágil. Contra MEGA la solución simple es
#  pausar la sincronización mientras se compila.
#
#  Uso:  latexmk -xelatex tesis.tex     -> tesis.pdf
#        latexmk -c                     -> borra auxiliares, conserva el PDF
#        latexmk -C                     -> borra todo, incluido el PDF
# ============================================================

$pdf_mode = 5;          # 5 = xelatex
$postscript_mode = 0;
$dvi_mode = 0;

# Forzar la ejecución de biber para biblatex.
# Con el valor por omisión (1.5) latexmk solo lo corre si logra localizar
# el .bib por su cuenta; si no lo encuentra saltea el paso en silencio y
# la bibliografía queda vacía sin ningún error visible.
$bibtex_use = 2;

# Los .aux de \include{secciones/...} se escriben junto a cada archivo.
# Se listan como generados para que «latexmk -c» los limpie.
push @generated_exts, 'bcf', 'run.xml';
