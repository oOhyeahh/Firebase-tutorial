import pyrebase
from credential import FIREBASECONFIG, TOKEN

if __name__ == "__main__":
    firebase = pyrebase.initialize_app(FIREBASECONFIG)
    storage = firebase.storage()
    storage.child("images/newimages.jpg").put("football.jpg", TOKEN)