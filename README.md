# GamesTEC

A video game catalog web app built with Streamlit as a university project.

## Features

- Game grid (four per row) with cover art and title
- Details page per game, with platforms and prices
- Discounts page
- Automatic "Included in Game Pass" tag for Xbox titles
- Custom dark theme with CSS and Google Fonts

## Tech

Python · Streamlit · pandas · JSON data files (`JuegosActualizado.json`, `imagenes.json`)

## Project structure

| Path | Role |
|---|---|
| `Principal.py` | Home page with the game grid |
| `pages/` | Details and discounts pages |
| `JuegosActualizado.json` | Game data (platforms, prices) |
| `imagenes.json` | Game name to cover image URL |

## Run it

```bash
pip install streamlit pandas
streamlit run Principal.py
```
