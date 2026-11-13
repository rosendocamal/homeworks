#set page(
    paper: "us-letter",
    margin: (x: 2.54cm, y: 2.54cm),
    header: [
        #set text(10pt)
        #smallcaps[Física General]
        #h(1fr) _Estática_
    ],
    numbering: "1",
)
#set text(
    lang: "es",
    font: "New Computer Modern",
    size: 12pt
)
#set par(
    justify: true,
    leading: 0.52em,
)

#show title: set text(size: 17pt)
#show title: set align(center)
#title[
    Cálculo de un vector resultante
]

#grid(
    columns: (1fr),
    align(center)[
        Rosendo Camal \
        Universidad Aztlán \
        #link("mailto:rosendocamal.edu@gmail.com") \
        13 de noviembre de 2026
    ]
)

#set document(title: [Cálculo de un vector resultante])

#let f1x = calc.round(50 * calc.cos(30deg), digits: 2)
#let f1y = calc.round(50 * calc.sin(30deg), digits: 2)

#let f2x = calc.round(80 * calc.cos(120deg), digits: 2)
#let f2y = calc.round(80 * calc.sin(120deg), digits: 2)

#let f3x = calc.round(40 * calc.cos(225deg), digits: 2)
#let f3y = calc.round(40 * calc.sin(225deg), digits: 2)

#let f4x = calc.round(60 * calc.cos(315deg), digits: 2)
#let f4y = calc.round(60 * calc.sin(315deg), digits: 2)

#let SigmaX = calc.round(f1x + f2x + f3x + f4x, digits: 2)
#let SigmaY = calc.round(f1y + f2y + f3y + f4y, digits: 2)

#figure(
    table(
        columns: (1fr, 2fr, 2fr, 3fr, 3fr),
        align: center + horizon,
        fill: (_, y) => if y == 0 or y == 5 { eastern },
        table.header[][*Fuerza \ ($F$, N*)][*$theta$ \ (Ángulo)*][*Componente \ $F_x = F cos(theta)$ \ (N*)][*Componente \ $F_y = F sin(theta)$ \ (N*)],
        table.cell(fill: teal, [$F_1$]), [50 N], [$30°$],  [#f1x], [#f1y],
        table.cell(fill: teal, [$F_2$]), [80 N], [$120°$], [#f2x], [#f2y],
        table.cell(fill: teal, [$F_3$]), [40 N], [$225°$], [#f3x], [#f3y],
        table.cell(fill: teal, [$F_4$]), [60 N], [$315°$], [#f4x], [#f4y],
        [*Total*],  table.cell(colspan: 2, [*Suma de \ componentes* ($Sigma$)]), [#SigmaX], [#SigmaY],
    ),
    caption: [Tabla de Componentes de Fuerza], 
) <tab-componentes-fuerza>

#set math.mat(row-gap: 0.75em)
El vector *resultante* es $ R = mat(SigmaX; SigmaY).$

#figure(
    image("geogebra-export.svg", width: 72%),
    caption: [
        _Diagrama Vectorial del Triángulo Final y y Cálculo de Fuerza Resultante_
    ],
) <svg-diagram>

#let magnitud = calc.round(calc.root(calc.pow(SigmaX, 2) + calc.pow(SigmaY, 2), 2), digits: 2)
La *magnitud* de la resultante es $ R = sqrt((Sigma F_x)^2 + (Sigma F_y)^2) = magnitud.$

#let direccion = calc.round(calc.atan(SigmaY / SigmaX).deg(), digits: 2)
La *dirección* de la resultante es $ theta_R = arctan((Sigma F_y)/(Sigma F_x)) = direccion°.$