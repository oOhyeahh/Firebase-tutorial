import sys
import pyrebase
from requests import HTTPError

from credential import FIREBASECONFIG


if __name__ == "__main__":
    firebase = pyrebase.initialize_app(FIREBASECONFIG)
    auth = firebase.auth()
    email = input("email: ")
    password = input("password: ")
    create_user_response = None
    # create user
    #
    # try:
    #     create_user_response = auth.create_user_with_email_and_password(email=email, password=password)
    #     print("User create successfully")
    # except HTTPError as error:
    #     print(error)

    # user sign in
    try:
        signin_response = auth.sign_in_with_email_and_password(email=email, password=password)
        print(f"User signin successfully. The token is {signin_response['idToken']}")
    except HTTPError:
        print("incorrect email or pasaword")
        sys.exit(0)
        

    # send verification email
    # verification_email_response = auth.send_email_verification(signin_response.get('idToken', ""))
    # print("Verification has been sent")

    # reset password
    # reset_password_response = auth.send_password_reset_email(email=email)
    # print("reset password email has been sent")



