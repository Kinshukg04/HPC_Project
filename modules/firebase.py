import pyrebase
import time
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
userid =""
username=""

def reset():
    db = firebase.database()
    auth = firebase.auth()
    storage = firebase.storage()

# login
def loginFirebase(email ,password):
    try:
        global userid
        global username
        user=auth.sign_in_with_email_and_password(email, password)
        username=email.split('@')[0]
        db.child("users")
        db.child(username).remove()
        db.child("users")
        db.child(username).push(user)
        #db.child(username).child("process")
        print("signed in")
        userid=user['idToken']
        reset()

    except:
        print("failed")


# signup
def signupFirebase(email,password):
    try:
        global userid
        global username
        auth.create_user_with_email_and_password(email, password)
        user=auth.sign_in_with_email_and_password(email, password)
        username=email.split('@')[0]
        db.child("users")
        db.child(username).push(user)
        #db.child(username).child("process")
        print("account created ")
        userid=user['idToken']
        reset()
    except:
        print("failed to create an account")


def uploadfile(filename ,cfilename  ):

    storage.child(cfilename).put(filename)
    return storage.child(cfilename).get_url(None)


def geturl(cfilename):
    return storage.child(cfilename).get_url(None)


def downloadfile(filename):
    storage.child(filename).download("", filename)


def pushdata(data, mychild=None):
    if (mychild == None):
        db.push(data)
    else:
        db.child(mychild).push(data)

def getdata(mychild):
    reset()
    return db.child(mychild).get()

def deletedata(mychild):
    reset()
    db.child(mychild).remove()

# get the number of devices
def getnums():
    val = getdata("users")
    res=0
    for i in val:
        res=res+1
    return res

# to remove from registered devices , always do this otherwise error will happen
def exit():
    global username
    db.child("users")
    db.child(username).remove()
    reset()



def distributeprocess( listoftask):
    deletedata("output")
    itr=0
    assert len(listoftask)==getnums()
    val =getdata("users")
    reset()
    for i in val:
        print("pushed in ", i.key())
        db.child("users").child(str(i.key())).child("process")
        db.push(listoftask[itr])
        itr=itr+1
        reset()
    reset()

def ProcessRequestCheck():
    reset()
    done=False
    try:
        while(True):
            for i in db.child("users").child(username).child("process").get() :
                return (i.val())
    except:
        print("failed")
        return ProcessRequestCheck()



def SendOutput(MyOutput):
    reset()
    pushdata(MyOutput,"output")

def ConbineOutput():
    lst=[]
    for i in db.child("output").get():
        lst.append(i.val())
    if(len(lst)<getnums()):
        return ConbineOutput()
    return lst








