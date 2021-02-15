#https: // github.com / DataGlacier / VC.git
import json, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

"""
In Python, you can get the location (path) of the running script file .py with __file__.
__file__ is useful for reading other files based on the location of the running file.
In Python 3.8 and earlier, __file__ returns the path specified when executing the python (or python3) command.
If you specify a relative path, a relative path is returned. If you specify an absolute path, an absolute path is returned.
In Python 3.9 and later, __file__ always returns an absolute path, regardless of whether the path specified with the python command is relative or absolute.

Use os.path.basename(), os.path.dirname() to get the file name and the directory name of the running file.
If you get the relative path with __file__, you can convert it to an absolute path with os.path.abspath().
Use os.chdir() to change the current working directory to the directory of the running file.
https://note.nkmk.me/en/python-script-file-path/
""" 

# User can add name and favourite sport in response.json
# default sport Cricket will be added incase user does not provide fav sport


""" 
JSON (JavaScript Object Notation) is a syntax for storing and exchanging data.
JSON is text, written with JavaScript object notation.
JSON is a format that encodes objects in a string.
Since the JSON format is text only, it can easily be sent to and from a server, and used as a data format by any programming language.
Serialization means to convert an object into that string, and deserialization is its inverse operation (convert string -> object).
When transmitting data or storing them in a file, the data are required to be byte strings, 
but complex objects are seldom in this format. Serialization can convert these complex objects into byte strings for such use. 
After the byte strings are transmitted, the receiver will have to recover the original object from the byte string. This is known as deserialization.
"""


def load_json():
    """
    Deserialize a file.object (a .read()-supporting text file 
    or binary file containing a JSON document) to a Python object.
    A dict object is returned by the funcion.
    """
    with open('../response.json') as json_obj:
        response = json.load(json_obj)
    return response

"""
It is good practice to use the with keyword when dealing with file objects. 
The advantage is that the file is properly closed after its suite finishes, even if an exception is raised at some point. 
Using with is also much shorter than writing equivalent try-finally blocks.
If you’re not using the with keyword, then you should call close() to close the file and immediately free up any system resources used by it.
""" 

response = load_json()

def write_json(data,filename = '../response.json'):
    """
    Serialize data as a JSON formatted stream to filename (a .write()-supporting file-like object)
    """
    with open(filename,'w') as file:
        json.dump(data,file,indent=0) # An indent level of 0, negative, or "" will only insert newlines. 
	


def call_sport():
    name = input("Please add your name: ")
    sport = input("Please add your favourite sports name: ")
    if (sport == ""):
        sport = 'Cricket'
    if (name):
        response[name] = sport
        write_json(response)


if __name__ == "__main__":
    call_sport()

call_sport()
