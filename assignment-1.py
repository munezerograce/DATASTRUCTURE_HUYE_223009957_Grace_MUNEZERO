from collections import deque
events_list = deque(["umuganura talk","umushyiikirano","public talk"])

def cancelTicket():
    if events_list:
        events_list.pop()
    else:
        print("No Event Found")

def processTicket():
    if events_list:
        events_list.popleft()
    else:
        print("No Event Found")


cancelTicket()
processTicket()
print(f"All Available events: {events_list}")
