from ninja import Schema
from datetime import datetime

from pydantic import EmailStr
class WaitListEntryCreateSchema(Schema):
    #create =>data
    #waitlistentryDataIn
    email:EmailStr
    
    

class WaitListEntryListSchema(Schema):
      #list =>data
    #waitlistentryDataIn'
    id:int
    email:EmailStr



class WaitListEntryDetailSchema(Schema):
      #get =>data
    #waitlistentryDataIn
    email:EmailStr
    timestamp:datetime
            
        