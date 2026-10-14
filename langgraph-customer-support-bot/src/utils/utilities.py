from langchain_core.messages import ToolMessage
from langchain_core.runnables import RunnableLambda
from langgraph.prebuilt import ToolNode
from pydantic import BaseModel, Field



class CompleteOrEscalate(BaseModel):
    cancel: bool = True
    reason: str

class ToFlightBookingAssistant(BaseModel):
    request: str 

class ToBookCarRental(BaseModel):
    
    request: str 



class ToHotelBookingAssistant(BaseModel):
    request: str 


class ToBookExcursion(BaseModel):
    
    request: str 