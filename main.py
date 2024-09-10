from fastapi import FastAPI 
from fastapi.responses import HTMLResponse
app = FastAPI()
app.title = "Mi aplicación con FastAPI"
app.version = "0.0.1"

movie_list = [
    {
        "id":1,
        "title": "Spiderman",
        "overview": "Un superheroe",
        "year": 2021,
        "rating": 5.0
    },
     {
        "id":2,
        "title": "Intensamente 2",
        "overview": "Emociones intensas 2",
        "year": 2021,
        "rating": 10.0
    },
      {
        "id":3,
        "title": "Mis huellas a casa",
        "overview": "Mascota",
        "year": 2020,
        "rating": 8.0
    }
    
]
@app.get('/', tags=['Home'])
def message():
    return HTMLResponse('<h1>¡Hola mundo!</h1>')
@app.get('/movies', tags=['Movies'])
def movies():
    return movie_list