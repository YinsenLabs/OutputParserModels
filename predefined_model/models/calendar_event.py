from datetime import datetime
from pydantic import BaseModel, Field
from predefined_model.models.base import BaseOutputModel
from typing import Optional


class Time(BaseModel):
    dateTime: datetime = Field(description="Time value ISO 8601 datetime format")
    timeZone: str = Field(description="Time zone value e.g: America/Los_Angeles")

class CalendarEventModel(BaseOutputModel):
    """ Response class for calendar api """
    
    summary: str = Field(..., title="Summary", description="The generated summary to use as a title of calendar")
    description: str = Field(description='A short description of event as list to track')
    startTime: Time = Field(description='Time start')
    endTime: Time = Field(description='Time end')
