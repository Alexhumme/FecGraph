import flet as ft
# phases: Listado de informacion sobre cada fase
data: list = [
    {
        "name": "Austenita",
        "symbol": "y",
        "crystal": "",
        "description": "En este estado, los aceros son maleabes y faciles de manipular, las altas temperaturas ayudan a su uso.",
        "properties": [
            {"val": "Dúctil"},
            {"name": "Rigidez", "val": "Blanda"},
            {"val": "Tenaz"},
        ],
        "line_x": [0, 0.3, 2.11, 0.8, 0],
        "line_y": [1390, 1450, 1147, 723, 900],
        "line_properties": {"color": 'r'},
        "img": "austenita.png"
    },
    {
        "name": "Ferrita",
        "symbol": "a",
        "crystal": "",
        "description": "Es a fase mas banda que aparece a temperatura abiente, ,lo que la hace muy importante a pesar de su poca cantidad.",
        "properties": [
            {"name": "solubilidad", "val": "0.02%"},
            {"name": "Rigidez", "val": "Blanda"},
        ],
        "line_x": [0, 0.15, 0.2, 0.15, 0],
        "line_y": [900, 780, 723, 630, 0],
        "line_properties": {"color": 'b'},
        "img": "austenita.png"
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
        "line_properties": {"color": 'g'},
        "img": "austenita.png"
    },
    {
        "name": "Perlita",
        "symbol": "a + Fe3C",
        "crystal": "",
        "description": "Se forma por la minas alternas de ferrita y cementita a menos de 723°C, posee posee propiedades de ambos.",
        "properties": [{"name": "Resistencia", "val": "Alta"}],
        "line_x": [0.8, 0.8],
        "line_y": [723, 0],
        "line_properties": {"color": 'y', "dash_pattern": [5, 5]},
        "img": "austenita.png"
    },
    {
        "name": "Liquido",
        "img": "liquido.png"
    },
]