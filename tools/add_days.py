from datetime import datetime 
from datetime import timedelta 
from langchain.tools import Tool 

def add_days_to_date(days : int): 
    end_date = timedelta(days = days) + datetime.today()
    end_date = end_date.strftime("%Y-%m-%d")
    return end_date 

day_addition_tool = Tool(
    name = "add_days_to_date", 
    func = add_days_to_date, 
    description = "Useful to add days to current date."
)