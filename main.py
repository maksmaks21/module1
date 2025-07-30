from fastapi import FastAPI

app = FastAPI()

users ={
    'vova_1': {
        "name": "John Doe",
        "surename": "Smith",
        "birth_year": 1990
    },
    'vova_2': {
        "name": "John Doe2",
        "surename": "Smith2",
        "birth_year": 1991
    }
}

@app.get("/")
def read_root():
    return {"message": "Привіт, FastAPI!"}

@app.get('/user/get-all')
def get_all_users():
    return users

@app.post('/user/create')
def create_new_user(user_login, name,  surename, year):
    user={
        "name": name,
        "surename": surename,
        "birth_year": year
    }