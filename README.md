# AirBnB clone - The console
![Image](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUZGDONYM4%2F20200213%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200213T155019Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=2935cd43fbca6a2394467fde4298e43e1ebe1ea9978b98a10deafe52d7185958)
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
- Github: [agzsoftsi](https://github.com/agzsoftsi)
- Twitter: [@karlgarmor](https://twitter.com/karlgarmor)

### Luz Sanchez
- Github: [zulsb](https://github.com/zulsb)
- Twitter: [@LuzSanchezB](https://twitter.com/LuzSanchezB)
