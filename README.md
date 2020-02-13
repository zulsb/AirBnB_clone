# AirBnB clone - The console

## Description 
Command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)

- Create your data model
- Manage (create, update, destroy, etc) objects via a console / command interpreter
- Store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between "My object" and "How they are stored and persisted". This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine

## Authors:
### Carlos Andres Garcia Morales
- Github: agzsoftsi
- Twitter: @karlgarmor

### Luz Sanchez
- Github: zulsb
- Twitter: @LuzSanchezB
