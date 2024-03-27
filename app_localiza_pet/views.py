from django.shortcuts import render
import pyrebase

# Create your views here.

config = {
    "apiKey": "AIzaSyAyNbhLKgquclkcjXGH2J0Kstknq_PQ0ME",
    "authDomain": "projeto-teste-88605.firebaseapp.com",
    "databaseURL": "https://projeto-teste-88605-default-rtdb.firebaseio.com",
    "projectId": "projeto-teste-88605",
    "storageBucket": "projeto-teste-88605.appspot.com",
    "messagingSenderId": "270422512374",
    "appId": "1:270422512374:web:ac2c95f8c8fde9483bd2d7"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()


def home(request):
    nome_pessoa = database.child('Pessoa').child('Nome').get().val()
    altura_pessoa = database.child('Pessoa').child('Altura').get().val()
    peso_pessoa = database.child('Pessoa').child('Peso').get().val()
    return render(request, "usuarios/home.html", {
        "nome_pessoa": nome_pessoa,
        "altura_pessoa": altura_pessoa,
        "peso_pessoa": peso_pessoa
    })
