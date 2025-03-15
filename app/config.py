import firebase_admin
from firebase_admin import credentials
import pyrebase

cred = credentials.Certificate("../serviceAccountKey.json")
firebase_admin.initialize_app(cred)

firebaseConfig = {
    "apiKey": "",
    "authDomain": "dropx-7e14e.firebaseapp.com",
    "databaseURL": "https://dropx-7e14e-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "dropx-7e14e",
    "storageBucket": "dropx-7e14e.firebasestorage.app",
    "messagingSenderId": "523892550059",
    "appId": "1:523892550059:web:5ffade982d7838da1d8aee",
    "measurementId": "G-SR4Q90XXCY",
}

firebase = pyrebase.initialize_app(firebaseConfig)
