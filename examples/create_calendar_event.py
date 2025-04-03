from predefined_model.llm_clients.gemini_calls import call_gemini_calendar_event
from predefined_model.models.calendar_event import CalendarEventModel
from typing import List


response: List[CalendarEventModel] = call_gemini_calendar_event("Create 2 hello world event 2 days each task, timeZone: Asia/Ho_Chi_Minh")

for event in response:
    print(event.model_dump())
