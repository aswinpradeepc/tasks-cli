#!/usr/bin/env python3
import json
import sys,os

try:
    s = sys.argv[1]
except:
    print("tasks-cli is a todo list app. Type tc help to know more \n \n \nWritten to beat boredom :)\nWritten by aswinpradeepc")
    print("The app stores files in a json file called liststorage.json (incase you need to backup)")
    exit()

if s == 'help':
    print(
        """
The lists available are 
  1. todo 
  2. in_progress 
  3. done 
use list <list-name> \t to display tasks

add <task> \t add tasks
update <task index> <updated task text>
delete <task index>

mark-done <task index>
mark-inp <task index> 
finish <task index> \t finish task that was in_progress.
""")
    exit()

def writetofile(data):
    try:
        with open('temp.json','w') as file:
            json.dump(data,file)
            os.replace('temp.json','liststorage.json')
    except:
        print("error while writing to JSON!")

try:
    with open('liststorage.json','r') as jsfile:
        jsfile.seek(0)
        data = json.loads(jsfile.read())
        todo, in_progress, done = data["todo"], data["in_progress"],data["done"]

        #List
        if s == "list":
            try:
                if sys.argv[2]=="todo":
                    for index, item in enumerate(todo):
                        print( index+1,".",item)
                elif sys.argv[2][:2] == "in":
                    for index, item in enumerate(in_progress):
                        print(index+1,".",item)
                elif sys.argv[2] == "done":
                    for index, item in enumerate(done):
                        print(index+1,".", item)
                else:
                    print("enter valid input - todo, in_progress or done")
            except:
                print("please mention the list - todo, in_progress or done")

        #Add 
        elif s == "add":
            try:
                todo.append(sys.argv[2])
                writetofile(data)
            except:
                print("mention task to be added in single quotes in this syntax \n\t tc add 'buy shoes'")

        #mark-done
        elif s == 'mark-done':
            try:
                index = int(sys.argv[2])
                done.append(todo.pop(index-1))
                writetofile(data)
            except:
                print("Please enter a valid index")

        #mark-in_progress
        elif s[:7] == 'mark-in':
            try:
                index = int(sys.argv[2])
                in_progress.append(todo.pop(index-1))
                writetofile(data)
            except:
                print("Please enter a valid index")
        
        #finish task in_progress
        elif s == 'finish':
            try:
                index = int(sys.argv[2])
                done.append(in_progress.pop(index-1))
                writetofile(data)
            except:
                print("Please enter a valid index") 
        
        #Delete
        elif s == 'delete':
            try:
                index = int(sys.argv[2])-1
                if index <= len(todo):
                    todo.pop(index)
                    writetofile(data)
                else:
                    print("Provide correct index within range of todo list.")
            except:
                try: 
                    index = int(sys.argv[3])-1
                    if sys.argv[2] == "todo":
                        if index <= len(todo):
                            todo.pop(index)
                        else :
                            print("Provide correct index to delete.")
                    elif sys.argv[2][:2] == 'in':
                        if index <= len(in_progress) :
                            in_progress.pop(index)
                        else:
                            print("Provide correct index to delete.")
                    elif sys.argv[2] == 'done':
                        if index <= len(done):
                            done.pop(index)
                        else:
                            print("Provide correct index to delete.")
                    writetofile(data)
                except:
                    print("Please enter valid command. The syntax for delete command is \n\t tc delete <list name> <index of task to delete>")
                    print("if no <list name> is mentioned, it deletes the index from todo list.")
                

        #update
        elif s == 'update':
            try: 
                index = int(sys.argv[3])-1
                if sys.argv[2] == "todo":
                    if index <= len(todo):
                        todo[index] = sys.argv[4] 
                    else :
                        print("Provide correct index to update.")
                elif sys.argv[2][:2] == 'in':
                    if index <= len(in_progress) :
                        in_progress[index] = sys.argv[4] 
                    else:
                        print("Provide correct index to update.")
                elif sys.argv[2] == 'done':
                    if index <= len(done):
                        done[index] = sys.argv[4]
                    else:
                        print("Provide correct index to update.")
                writetofile(data)
            except:
                print("Please enter valid command. The syntax for update command is \n\t tc update <list name> <index to update> <updated task>")
        else:
            print("invalid input")
        jsfile.close()
except FileNotFoundError:
    print("file not found!")
except json.JSONDecodeError:
    print("json decode error!")
