import json

class Event: 
    def __init__(self, name, start, length):
        self.name = name
        self.start = start
        self.length = length

class Task:
    def __init__(self, name, priority, length):
        self.name = name
        self.priority = priority
        self.length = length

def parseInput(jsonFile):
        with open(jsonFile, 'r') as file:
            input = json.load(file)

        result = {}
        result["events"] = []
        result["tasks"] = []

        for chunk in input:
            if chunk == "events":    
                for event in input[chunk]:
                    newEvent = Event(event["name"], event["start"], event["length"])            
                    result["events"].append(newEvent)
            elif chunk == "tasks":
                for task in input[chunk]:
                    newTask = Task(task["name"], task["priority"], task["length"])            
                    result["tasks"].append(newTask)

        #for x in result["events"]:
        #    print(x.name)

        #for x in result["tasks"]:
        #    print(x.name)

        return result

def scheduleTasks(events, tasks):

    tasks.sort(key=lambda x: x.priority, reverse=True)

    newEvents = []

    for event in events:
        newEvent = Event(event.name, event.start, event.length)
        newEvents.append(newEvent)
    
    newEvents.sort(key=lambda x: x.start)

    for task in tasks:
        gapStart, gapLength = _findGap(newEvents, task)
            # gapLength = 0, no gap add at end
            # gapLength > task.length, schedule task at gapStart for task.length
            # gapLength < task.length, schedule task for gapLength, repeat 

        if gapLength == 0:
            newEvent = Event(task.name, gapStart, task.length)
            newEvents.append(newEvent)
            print("Added at end: "+str(task.name))
            continue

        remainingLength = task.length

        while gapLength < remainingLength:
            gapStart, gapLength = _findGap(newEvents, Task(task.name, task.priority, remainingLength))
            newEvent = Event(task.name, gapStart, gapLength)
            newEvents.append(newEvent)
            print("Added partial task: "+str(task.name)+", Length: "+str(gapLength)+" Gap length: "+str(gapLength))
            remainingLength = remainingLength - gapLength
            gapStart, gapLength = _findGap(newEvents, Task(task.name, task.priority, remainingLength))
        else:
            gapStart, gapLength = _findGap(newEvents, task)
            newEvent = Event(task.name, gapStart, remainingLength)
            newEvents.append(newEvent)
            print("Added final task: "+str(task.name)+", Length: "+str(remainingLength)+" Gap length: "+str(gapLength))

    newEvents.sort(key=lambda x: x.start)

    return newEvents

def scheduleOnlyTasks(events, tasks):

    tasks.sort(key=lambda x: x.priority)

    newEvents = []
    newTasks = []

    for event in events:
        newEvent = Event(event.name, event.start, event.length)
        newEvents.append(newEvent)
    
    newEvents.sort(key=lambda x: x.start)

    for task in tasks:
        gapStart, gapLength = _findGap(newEvents, task)
            # gapLength = 0, no gap add at end
            # gapLength > task.length, schedule task at gapStart for task.length
            # gapLength < task.length, schedule task for gapLength, repeat 

        if gapLength == 0:
            newEvent = Event(task.name, gapStart, task.length)
            newEvents.append(newEvent)
            newTasks.append(newEvent)

            print("Added at end: "+str(task.name))
            continue

        remainingLength = task.length

        while gapLength < remainingLength:
            gapStart, gapLength = _findGap(newEvents, Task(task.name, task.priority, remainingLength))
            newEvent = Event(task.name, gapStart, gapLength)
            newEvents.append(newEvent)
            newTasks.append(newEvent)
            print("Added partial task: "+str(task.name)+", Length: "+str(gapLength)+" Gap length: "+str(gapLength))
            remainingLength = remainingLength - gapLength
            gapStart, gapLength = _findGap(newEvents, Task(task.name, task.priority, remainingLength))
        else:
            gapStart, gapLength = _findGap(newEvents, task)
            newEvent = Event(task.name, gapStart, remainingLength)
            newEvents.append(newEvent)
            newTasks.append(newEvent)
            print("Added final task: "+str(task.name)+", Length: "+str(remainingLength)+" Gap length: "+str(gapLength))

    newTasks.sort(key=lambda x: x.start)

    return newTasks

def printEvents(events):
    for event in events:
        print(event.name)
        print(event.start)
        print(event.length)
        print(event.length+event.start)


def _findGap(events, task):

    events.sort(key=lambda x: x.start)

    lastEnd = 0

    for event in events:
        if lastEnd == 0:
            lastEnd = event.start + event.length
            continue
            
        gapStart = lastEnd
        gapLength = event.start - lastEnd
        
        if (gapLength) > 0:
            return gapStart, gapLength
        
        lastEnd = event.start + event.length

    gapStart = lastEnd
    gapLength = 0

    return gapStart, gapLength


    return

def returnJson(events):

    jsonString = ""

    newEvents = {"events": []}

    for event in events:
        newEvent = event.__dict__
        newEvents["events"].append(newEvent)

    jsonString = json.dumps(newEvents, separators=(',', ':'), indent=None)
        
    return jsonString

def returnJsonNormal(events):

    jsonString = ""

    newEvents = []

    for event in events:
        newEvent = event.__dict__
        newEvents.append(newEvent)

    # jsonString = json.dumps(newEvents, separators=(',', ':'), indent=None)
    jsonString = json.dumps(newEvents)
        
    return jsonString

items = parseInput("input.json")

events = scheduleTasks(items["events"], items["tasks"])

tasks = scheduleOnlyTasks(items["events"], items["tasks"])

printEvents(events)

# printEvents(tasks)

output = returnJsonNormal(events)

print(output)