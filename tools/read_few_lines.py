from langchain.tools import Tool 
from pathlib import Path 

def read_few_lines(number_of_lines : int): 
    dirname = Path("data")
    filename = dirname / "shekspeare.txt"
    with open(filename, "rb") as f: 
        lines = [f.readline() for _ in range(number_of_lines)]
    return lines


few_lines_reader_tool = Tool(
    name = "read_few_lines", 
    func = read_few_lines, 
    description = "Few lines reader from .txt file." 
)



