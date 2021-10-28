import sys
import json
import os


scr = []

# Main method, 
def manageInputs():
    
    global scr
    # Get the arguments that were given
    arguments = sys.argv[1:]

    # If there are no arguments, send error message else continue
    if arguments != []:

        # load the config for the scripts
        loadConfigFile()
        command = arguments[0]
        arguments = arguments[1:]
        
        # Standard help command, show the commands in config file, as well as 
        # "add" and "remove"
        if command == "--help":
            print("These are the different script options:\n")
            for command in scr:
                spacer = " " * (32 - len(command["name"]))
                print(command["name"] + spacer + command["desc"])
            print("add                             Add a script to the config file")
            print("remove                          Remove script from the config file")
        
        # Select the add command with following arguments:
        # Name: name of the script to be added
        # ScriptFile: Script to launch the script from the controller
        # Options: options that can be added
        # Desc: description of the script to be added
        elif command == "--add":
            print(arguments)
            add(arguments[0], arguments[1], arguments[2], arguments[3])
        
        elif command == "--remove":
            remove(arguments[0])
        
        else:
            scrCodes = [script["name"] for script in scr]
            zip_iterator = zip(scrCodes, scr)
            scriptDict = dict(zip_iterator)
            execute_script(scriptDict[command], arguments)

    else:
        print("If you need some help, run the command with --help as the first option")

def loadConfigFile():
    global scr
    with open("controllerConfig.json") as file:
        jsonConfig = json.load(file)
    for entry in jsonConfig["scripts"]:
        scr += [entry]

def add(name, scriptFile, options, desc):
    global scr
    data_set = {
            "name": name,
            "file": scriptFile,
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
        if sc["name"] != name:
            t += [sc]
        else:
            print(sc["name"])
        scr = t
    with open('controllerConfig.json', 'w') as outfile:
        json.dump({"scripts": scr}, outfile)

def execute_script(command, args):
    os.system(command["file"] + " " + ' '.join(args))

def edit():
    return 0

if __name__ == "__main__":
    manageInputs()
