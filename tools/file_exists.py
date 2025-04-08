import os
from langchain.tools import Tool 

def is_file_exists(filename : str): 
    is_exists = os.path.exists(filename)
    if not is_exists: 
        raise FileNotFoundError("file {filename} does not exists.")
    return is_exists

file_exists_tool = Tool(
    name = "is_file_exists", 
    func = is_file_exists, 
    description = "Useful for checking if a file exists. Input should be the full path to the file."
)

