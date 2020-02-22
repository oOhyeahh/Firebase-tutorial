import pyrebase
from credential import FIREBASECONFIG

if __name__ == "__main__":
    firebase = pyrebase.initialize_app(FIREBASECONFIG)
    database = firebase.database()

    # create new data
    database.child("Drink").push(data={"name": "Coke"})
    database.child("Drink").push(data={"name": "Fanta"})
    database.child("Drink").push(data={"name": "7Up"})

    # update data
    drinks = database.child("Drink").get()
    drink_list = drinks.pyres
    coke_key, coke_value = drink_list[0].item
    database.child("Drink").child(coke_key).update(data={"name": "Sprite"})

    # remove data

    drinks = database.child("Drink").get()
    drink_list = drinks.pyres
    key, value = drink_list[0].item
    database.child("Drink").child(key).remove()

    # delete dataset
    drinks = database.child("Drink").remove()

