# FecGraph – Herramienta Interactiva del Diagrama Hierro-Carbono

<center>
<img src="https://i.imgur.com/6d8iS62.png" alt="Logo FecGraph" width="200"/>

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Tkinter](https://img.shields.io/badge/Tkinter-%20Tkinter%20-blue.svg)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-blue.svg)
</center>

## Descripción

**FecGraph** es una aplicación de escritorio interactiva desarrollada en Python que permite visualizar y explorar el diagrama hierro-carbono de forma didáctica. Está diseñada para apoyar procesos de enseñanza y aprendizaje en el área de metalurgia, mostrando en tiempo real las diferentes fases (Austenita, Ferrita, Cementita, etc.) con información visual y textual relevante.

El programa está destinado al uso institucional dentro del plantel educativo de la Universidad de La Guajira, y su distribución está restringida a fines académicos.

## Funcionalidades

- Visualización del diagrama hierro-carbono con límites personalizables.
- Interacción con polígonos que representan las distintas fases metalográficas.
- Tooltips al pasar el cursor sobre cada fase, mostrando su nombre e imagen.
- Cambios visuales dinámicos en la opacidad de cada región al hacer hover.
- Visualización detallada de cada fase seleccionada en un panel lateral.

## Requisitos del sistema

- Sistema operativo: **Windows 10 o superior**
- Memoria RAM: **4 GB mínimo**
- Python 3.10+ (solo durante desarrollo)
- No requiere conexión a internet

> Nota: Aunque actualmente solo se encuentra disponible para Windows, se prevé en futuras versiones ofrecer soporte para otros sistemas operativos.

## Instalación

1. **Clona el repositorio:**

    ```sh
    git clone https://github.com/Alexhumme/FecGraph.git
    cd FecGraph
    ```

2. **Crea y activa un entorno virtual:**

    ```sh
    python -m venv .venv
    .venv\\Scripts\\activate  # En Windows
    ```

3. **Instala las dependencias:**

    ```sh
    pip install -r requirements.txt
    ```

## Ejecución del proyecto

Para iniciar la aplicación, ejecuta:

```sh
python ./src/main.py

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
Contributing

Contributions are welcome! Please create an issue or submit a pull request if you have any improvements or bug fixes.

## Contact

For any questions or suggestions, feel free to reach out to support@uniguajira.edu.co
