import sys
import json

scripts = set()

def manageInputs():
    arguments = sys.argv[1:]
    if arguments != []:
        loadConfigFile()
        command = arguments[0]
        arguments = arguments[:1]
        if command == "--help":
            print("These are the different script options:\n")
            for command in scripts.values():
                spacer = " " * (32 - len(command["name"]))
                print(command["name"] + spacer + command["desc"])
            print("add                             Add a script to the config file")
            print("remove                          Remove script from the config file")
        elif command == "add":
            print("add")
        elif command == "remove":
            print("remove")
        else:
            for script in commands.values():
                print(script["name"])
    else:
        print("If you need some help, run the command with --help as the first option")

def loadConfigFile():
    with open("controllerConfig.json") as file:
        jsonConfig = json.load(file)
    for entry in jsonConfig["scripts"]:
        scripts.add(entry)
manageInputs()
