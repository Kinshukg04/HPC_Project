import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyC8u9ocZsnDeNqRR-j4e7GJfazS558gw-c",
    "authDomain": "hpc-procect-2021.firebaseapp.com",
    "databaseURL": "https://hpc-procect-2021-default-rtdb.firebaseio.com/",
    "projectId": "hpc-procect-2021",
    "storageBucket": "hpc-procect-2021.appspot.com",
    "messagingSenderId": "716203312467",
    "appId": "1:716203312467:web:28809fd0b1668af9e0cda6",
    "measurementId": "G-E4SM5CMNFP"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
auth = firebase.auth()
storage = firebase.storage()


# login
def loginFirebase(email ,password):
    try:
        auth.sign_in_with_email_and_password(email, password)
        print("signed in")
    except:
        print("failed")


# signup
def signupFirebase(email,password):
    try:
        auth.create_user_with_email_and_password(email, password)
        print("account created ")
    except:
        print("failed to create an account")


def uploadfile(filename ,cfilename  ):

    storage.child(cfilename).put(filename)
    return storage.child(cfilename).get_url(None)


def geturl(cfilename):
    return storage.child(cfilename).get_url(None)


def downloadfile(filename):
    storage.child(filename).download("", filename)


def pushdata(data, mychild):
    if (mychild == None):
        db.push(data)
    else:
        db.child(mychild).push(data)

def getdata(mychild):
    return db.child(mychild).get()

def deletedata(mychild):
    db.child(mychild).remove()




