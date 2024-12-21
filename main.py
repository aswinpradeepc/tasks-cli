import json
import sys

s = sys.argv[1]

try:
    with open('liststorage.json','a+') as jsfile:
        jsfile.seek(0)
        data = json.loads(jsfile.read())
        todo, in_progress, done = data["todo"], data["in_progress"],data["done"]
        if s == "exit":
            exit()
        elif s == "list":
            if sys.argv[2]:
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
            else:
                print("please mention the list - todo, in_progress or done")
        elif s == "add":
            task = input("Enter task to add :")
            todo.append(task)
        else:
            print("invalid input")
            s = ""
        jsfile.close()
except FileNotFoundError:
    print("file not found!")
except json.JSONDecodeError:
    print("json decode error!")


