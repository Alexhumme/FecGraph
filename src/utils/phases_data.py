import flet as ft
# phases: Listado de informacion sobre cada fase
data: list = [
    {
        "name": "Austenita",
        "symbol": "γ",
        "description": "La austenita es una solución sólida de carbono en hierro gamma, con una estructura cristalina cúbica centrada en las caras (FCC).\nPuede disolver hasta 2.14% de carbono a 1147°C, es no magnética y relativamente dúctil y tenaz.",
        "line_x": [0, 0.3, 2.11, 0.8, 0],
        "line_y": [1390, 1450, 1147, 723, 900],
        "color": "#EE6055",
        "img": "austenita.png"
    },
    {
        "name": "Ledeburita",
        "symbol": "L",
        "description": "La ledeburita es una mezcla eutéctica de austenita y cementita que se forma en la intersección del 4.3% de carbono y 1147°C en el diagrama hierro-carbono.\nEs extremadamente dura y frágil debido a la presencia de cementita, lo que la hace inadecuada para la mayoría de las aplicaciones industriales.",
        "line_x": [1.76, 6.67, 6.67, 1.76],
        "line_y": [1130, 1130, 723, 723],
        "color": "#60D394",
        "img": "ledeburita.png"
    },
    {
        "name": "Ferrita",
        "symbol": "α",
        "description": "La ferrita es una solución sólida de carbono en hierro alfa, que tiene una estructura cristalina cúbica centrada en el cuerpo (BCC).\nTiene una baja solubilidad de carbono (máximo 0.022% a 727°C) y es relativamente blanda y dúctil.",
        "line_x": [0, 0.15, 0.2, 0.15, 0],
        "line_y": [900, 780, 723, 630, 0],
        "color": "#AAF683",
        "img": "ferrita.png"
    },
    {
        "name": "Perlita",
        "symbol": "α + Fe3C",
        "description": "La perlita es una microestructura que consiste en láminas alternas de ferrita y cementita.\nSe forma a partir de la austenita cuando se enfría lentamente por debajo de 727°C. Es más dura que la ferrita pura, pero más dúctil que la cementita pura.",
        "line_x": [0.8, 1.76, 1.76, 0.8],
        "line_y": [723, 723, 0, 0],
        "color": "#FF9B85",
        "img": "austenita.png"
    },
    {
        "name": "Cementita",
        "symbol": "Fe3C",
        "description": "La cementita es un compuesto intermetálico de hierro y carbono con la fórmula Fe₃C.\nEs muy dura y frágil, con una estructura ortorrómbica. No es útil por sí sola en aplicaciones industriales debido a su fragilidad, pero forma parte de otras microestructuras importantes como la perlita y la ledeburita.",
        "line_x": [1.76, 6.67, 6.67],
        "line_y": [723, 723, 0],
        "color": "#FFD97D",
        "img": "cementita.png"
    },
    {
        "name": "Liquido",
        "description":"El estado líquido en el diagrama hierro-carbono representa la fase en la que el hierro y el carbono están completamente fundidos.\nLa temperatura de fusión del hierro puro es de 1538°C, pero la adición de carbono reduce esta temperatura. El punto eutéctico del diagrama se encuentra en el 4.3% de carbono y 1147°C, donde la mezcla se solidifica en ledeburita.",
        "img": "liquido.png"
    },
]
