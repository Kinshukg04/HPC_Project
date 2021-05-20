# HPC_Project

### Steps to use:
- Connect a firebase database:
    - Initiate mulpy(fireBaseConfig), firebaseConfig looks like:    
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
- Login or signup in database by, muply.login(userid,password) and muply.signup(userid,password) respectively.

- mulply.splitData(input_data, numberOfDevices, split_type) is used to split data between multiple devices:
    - input_data: Either list or integer data permitted. For other types of data, custom split function required.
    - numberOfDevices(int): Number of total devices 
    - split_type == 'split': 
        - If input_data is an integer, split_data = input_data/numberOfDevices.
        - If input_data is a list, it will split list contents into equal parts for all devices
    - split_type == 'range':
        - If input_data is an integer, data is split from 0-n in equal parts for all devices.
        - If input_data is a list, list[0] is starting range and list[1] is ending range
    - split_type == 'absolute':
        - No split is performed. All devices receive input_data as it is.
- mulpy.process(file_name, function_name, input_data, multiprocess=False)
    - file_name(string): Is the python file to be shared with secondary devices which contains the function to be run.
    - function_name(string): The function to be run on secondary devices.
    - input_data(any): Data recieved after splitting the orginal data.
    - numberOfDevices(int): Number of total devices 
    - multiprocess(Boolean): Whether multiprocessing shoull be used or not.
- Write a function to compile outputs recieved from secondary devices after using mulpy.process.
    
                            


