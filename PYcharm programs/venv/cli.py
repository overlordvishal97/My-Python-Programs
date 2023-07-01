#1st method
#from functions import get_todos, write_todos
#2nd method.
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
Print("It is", now)


while True:
    #Get user input and strip space chars from it.
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

# we add el to if conditional to increase the speed of the program
    #if you want an explanation check 91st lecture
    elif user_action.startswith('show'):

        todos = functions.get_todos()

        #enumerate function is used to access the items and Index in the list
        for index, item in enumerate(todos):
            #with this item code you can delete extra space in the output
            # you can check it by commenting the code out
            #you can check this trick or more tricks in the lecture 71(udemy)
            item = item.strip('\n')
            #lets use an 'f' string to get the desired output
            row = f"{index + 1}-{item}"
            print(row)

            #2nd trick for break lines in the output using list comprehension
            # new_todos = [item.strip('\n') for item in todos]
    # we add el to if conditional to increase the speed of the program
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1
            #existing_todo= todos[number]
            #print(existing_todo)

            #the 'with' context manager closes the file after execution so it is not necessary to type file.close
            todos = functions.get_todos()

            print('Here is the existing', todos)

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            print('Here is the new', todos)

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            #you could use continue or user account from the 1 and 2 lines.
            continue

#we add el to if conditional to increase the speed of the program
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            #this variable enables you to see the list comprehsion you are about to pop
            todos_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)
            #This prints out the list comprehension you are about to pop.
            message = f"Todo {todos_to_remove} was removed from the list."

            print(message)
        except IndexError:
            print("There is no item with that number.")
            #continue function sets the cursor at starting again.
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not acceptable. ")    
print('bye')
