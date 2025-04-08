from datetime import datetime 
from langchain.tools import Tool 

def get_current_date(): 
    today = datetime.today().strftime("%Y-%m-%d")
    return today 


current_date_tool = Tool(
    name = "get_current_date", 
    func = get_current_date, 
    description = "Useful for formatting current date. The date format is as follows: Year - Month - Day."
)

