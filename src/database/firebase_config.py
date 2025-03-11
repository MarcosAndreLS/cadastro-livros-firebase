import pyrebase

firebaseConfig = {
  'apiKey': "AIzaSyDH2dgjWfKkmiGmb7crYEIC8hz373ReCmc",
  'authDomain': "cadastro-livros-firebase.firebaseapp.com",
  'projectId': "cadastro-livros-firebase",
  'storageBucket': "cadastro-livros-firebase.firebasestorage.app",
  'messagingSenderId': "47110958450",
  'appId': "1:47110958450:web:8134b82c92dc32ae1d81eb",
  'measurementId': "G-8RYWZJPEJ4",
  'databaseURL': "https://cadastro-livros-firebase-default-rtdb.firebaseio.com"
};

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()
db = firebase.database()
