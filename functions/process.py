import json
import re
import multiprocessing
import pyrebase
import sys
from modules.firebase import *
from modules.utils import validateEmail, splitList,splitRange
sys.path.append("../")


class mulpy:

    def __init__(self, firebaseConfig):
        """Setting up firebase

        Args:
            firebaseConfig (json): firebaseconfig contains api key,domain etc.
        """
        self.firebase = pyrebase.initialize_app(firebaseConfig)
        self.db = self.firebase.database()
        self.auth = self.firebase.auth()
        self.storage = self.firebase.storage()

    def login(self, email, password):
        """For logging in to firebase

        Args:
            email (string)
            password (string)
        """
        assert not validateEmail(email), "Email is invalid"
        loginFirebase(email=email, password=password)

    def signup(self, email, password):
        """For signing up a new user on firebase

        Args:
            email (string)
            password (string)
        """
        assert not validateEmail(email), "Email is invalid"
        signupFirebase(email=email, password=password)


    def splitData(self, input_data, numberOfDevices=2, split_type='split'):
        """Used to split data between devices, 3 split types: split, range, absolute
        Raises:
            AssertionError: When input type is not supported or split_type is incorrect
        Returns:
            [list]: List contains data for all deivces. Eg: for device 0: list[0] will be the data and so on.
        """
        assert input_data != None, "Input is empty"
        assert numberOfDevices >= 2, "Devices cannot be less than 2"
        if(split_type == 'split'):

            if(type(input_data) == int):
                data = int(input_data/numberOfDevices)
                output_list = []
                output_list = [data]*numberOfDevices
                return output_list

            elif(type(input_data) == list):
                output_list = []
                output_list = splitList(input_data, numberOfDevices)
                return output_list
            else:
                raise AssertionError('Supported input data types: int,list')

        elif(split_type == 'range'):
            if(type(input_data) == int):
                n = int(input_data / numberOfDevices)
                output_list = []
                for _ in range(numberOfDevices):
                    output_list.append(n)
                    n = n + n
                return output_list

            if(type(input_data) == list):
                assert type(input_data[0]) == int and type(
                    input_data[1]) == int and len(input_data)==2, "range values should be an integer, list[0] is starting range(inclusive) and list[1] is ending range(non-inclusive)"
                output_list = []
                input_range = range(input_data[0],input_data[1])
                output_list = splitRange(input_range,numberOfDevices)
                return output_list

        elif(split_type == 'absolute'):
            output_list = [input_data]*numberOfDevices
            return output_list
        else:
            raise AssertionError('Incorrect parameters. split_type = split,range,absolute')

    def process(self, file_name, function_name, input_data, numberOfDevices=2, multiprocess=False):

        assert input_data != None, "Input is empty"
        assert function_name != None, "Function name is empty"
        assert numberOfDevices >= 2, "Devices cannot be less than 2"

        database = self.db
        storage = self.storage

        assert storage != None, "Storage is not mentioned"
        assert database != None, "Database is not mentioned"

        url = uploadfile(file_name, file_name)
        jsonData = []
        numberOfUsers = getnums()
        print("Number of users connected to database: ",numberOfUsers)
        for user in range(1,numberOfUsers):
            temp = json.dumps({'fileName': file_name, 'funcName': function_name, 'input_data': input_data[user],
                              'numberOfDevices': numberOfDevices, 'multiprocess': multiprocess})
            jsonData.append(temp)
        distributeprocess(jsonData)
        #todo
