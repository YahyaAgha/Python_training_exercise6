# Python_training_exercise6

Python File Handling and Serialization
This repository contains Python programs that demonstrate file handling, including reading from files and understanding file modes, as well as serialization and deserialization of Python objects using the pickle module.
Read from File and File Handling Modes
Python provides built-in functions to read and write files. Here's a brief overview of file handling modes:
'r' - Read mode (default): Opens a file for reading.
'w' - Write mode: Opens a file for writing, creates a new file if it doesn't exist, or truncates the file if it does.
'a' - Append mode: Opens a file for appending at the end of the file without truncating it. Creates a new file if it doesn't exist.
'b' - Binary mode: Opens a file in binary mode (e.g., 'rb', 'wb').
'+' - Updating mode: Opens a file for updating (reading and writing).
Python's context managers are commonly used to handle files, which ensures that resources are properly released after use:

with open('example.txt', 'r') as file:
    content = file.read()

    Serialization and Deserialization with Pickle
Serialization is the process of converting a Python object into a byte stream to save it to a file or send it over a network, and deserialization is the reverse process. The pickle module in Python is used for serializing and deserializing objects.
Using Pickle to Serialize a Dictionary:
To serialize a dictionary to a file:

import pickle

my_dict = {'key': 'value'}

with open('dict.pickle', 'wb') as file:
    pickle.dump(my_dict, file)

    Deserializing with Pickle:
To deserialize the dictionary back from the file:

with open('dict.pickle', 'rb') as file:
    loaded_dict = pickle.load(file)

    The pickle module is powerful but isn't secure against erroneous or maliciously constructed data. It should never be used to unserialize data received from an untrusted source.
