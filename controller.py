import sys
import json


scr = []

def manageInputs():
    global scr
    arguments = sys.argv[1:]
    if arguments != []:
        loadConfigFile()
        command = arguments[0]
        arguments = arguments[1:]
        if command == "--help":
            print("These are the different script options:\n")
            for command in scr:
                spacer = " " * (32 - len(command["name"]))
                print(command["name"] + spacer + command["desc"])
            print("add                             Add a script to the config file")
            print("remove                          Remove script from the config file")
        elif command == "add":
            print(arguments)
            add(arguments[0], arguments[1], arguments[2], arguments[3])
        elif command == "remove":
            remove(arguments[0])
        else:
            for script in commands.values():
                print(script["name"])
    else:
        print("If you need some help, run the command with --help as the first option")

def loadConfigFile():
    global scr
    with open("controllerConfig.json") as file:
        jsonConfig = json.load(file)
    for entry in jsonConfig["scripts"]:
        scr += [entry]

def add(name, code, options, desc):
    global scr
    data_set = {
            "name": name,
            "code": code,
            "options": options,
            "desc": desc
    }
    json_set = json.dumps(data_set)
    scr += [json.loads(json_set)]
    with open('controllerConfig.json', 'w') as outfile:
        json.dump({"scripts": scr}, outfile)

def remove(name):
    global scr
    t = []
    for sc in scr:
        print(name)
        print(sc["name"])
        if sc["name"] != name:
            t += [sc]
        scr = t
    with open('controllerConfig.json', 'w') as outfile:
        json.dump({"scripts": scr}, outfile)

def edit():
    return 0

manageInputs()
