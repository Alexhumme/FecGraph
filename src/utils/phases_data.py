import flet as ft
# phases: Listado de informacion sobre cada fase
data: list = [
    {
        "name": "Austenita",
        "symbol": "y",
        "crystal": "",
        "description": "En este estado, los aceros son maleabes y faciles de manipular, las altas temperaturas ayudan a su uso.",
        "properties": [
            {"name":"","val": "Dúctil"},
            {"name": "Rigidez", "val": "Blanda"},
            {"name":"","val": "Tenaz"},
        ],
        "line_x": [0, 0.3, 2.11, 0.8, 0],
        "line_y": [1390, 1450, 1147, 723, 900],
        "color": 'r',
        "img": "austenita.png"
    },
    {
        "name": "Ledeburita",
        "symbol": "y",
        "crystal": "",
        "description": "En este estado, los aceros son maleabes y faciles de manipular, las altas temperaturas ayudan a su uso.",
        "properties": [
            {"name":"","val": "Dúctil"},
            {"name": "Rigidez", "val": "Blanda"},
            {"name":"","val": "Tenaz"},
        ],
        "line_x": [0, 0.3, 2.11, 0.8, 0],
        "line_y": [1390, 1450, 1147, 723, 900],
        "color": 'r',
        "img": "ledeburita.png"
    },
    {
        "name": "Ferrita",
        "symbol": "a",
        "crystal": "",
        "description": "Es a fase mas blanda que aparece a temperatura abiente, ,lo que la hace muy importante a pesar de su poca cantidad.",
        "properties": [
            {"name": "solubilidad", "val": "0.02%"},
            {"name": "Rigidez", "val": "Blanda"},
        ],
        "line_x": [0, 0.15, 0.2, 0.15, 0],
        "line_y": [900, 780, 723, 630, 0],
        "color": 'b',
        "img": "ferrita.png"
    },
    {
        "name": "Cementita",
        "symbol": "Fe3C",
        "crystal": "",
        "description": "Compuesto intermetalico no apropiado para procesos de deformacion plastico",
        "properties": [
            {"name": "Dureza", "val": "Duro"},
            {"name": "Rigidez", "val": "Fragil"},
        ],
        "line_x": [0.2, 6.67, 6.67],
        "line_y": [723, 723, 0],
        "color": 'g',
        "img": "cementita.png"
    },
    {
        "name": "Perlita",
        "symbol": "a + Fe3C",
        "crystal": "",
        "description": "Se forma por la minas alternas de ferrita y cementita a menos de 723°C, posee posee propiedades de ambos.",
        "properties": [{"name": "Resistencia", "val": "Alta"}],
        "line_x": [0.8, 0.8],
        "line_y": [723, 0],
        "color": 'y',
        "img": "austenita.png"
    },
    {
        "name": "Liquido",
        "img": "liquido.png"
    },
]
