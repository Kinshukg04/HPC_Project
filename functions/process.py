import json
import re
import multiprocessing
import pyrebase
import sys
from modules.utils import validateEmail, splitList,splitRange
sys.path.append("../")


class mulpy:

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
    # def readJson(jsonDict,numberOfDevices = 2):
    #     x = json.loads(jsonDict)
    #     for _ in numberOfDevices:
    #         data = x[0]
    #         filename = data['filename']
    #         funcName = data['funcName']
    #         input_data = data['input_data']
            
    def process(self, file_name, function_name, input_data, numberOfDevices=2, multiprocess=False):

        assert input_data != None, "Input is empty"
        assert function_name != None, "Function name is empty"
        assert numberOfDevices >= 2, "Devices cannot be less than 2"

        database = self.db
        storage = self.storage

        assert storage != None, "Storage is not mentioned"
        assert database != None, "Database is not mentioned"
        """
        url = uploadfile(file_name, file_name)
        jsonData = []
        numberOfUsers = getnums()
        print("Number of users connected to database: ",numberOfUsers)
        for user in range(1,numberOfUsers):
            temp = {}
            temp = {'fileName': file_name, 'funcName': function_name, 'input_data': input_data[user],
                              'numberOfDevices': numberOfDevices, 'multiprocess': multiprocess}
            jsonData.append(temp)
        output_json = json.dumps(jsonData)
        distributeprocess(jsonData)
        #todo
        """





