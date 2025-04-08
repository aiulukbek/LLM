import os 
from langchain.tools import Tool 

def list_files(dirname : str): 
    files = os.listdir(dirname)
    if not files: 
        raise ValueError("Directory is empty.")

    return files 


list_files_tool = Tool(
    name = "list_files", 
    func = list_files, 
    description = "List the files in the directory. Input should be the full path to the directory." 
)

