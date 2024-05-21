class EventException (Exception):
    def __init__(self,event_name):
        self.event_name = event_name
        
    def __str__ (self):
        return f"EventException: Invalid event '{self.event_name}'"
def process_event (event):
    valid_events =  ['click', 'hover', 'submit']
    
    if event not in valid_events:
        raise EventException(event)
try:
    process_event('scroll')
except EventException as e:
    print(e)