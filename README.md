# 0x00. AirBnB clone - The console

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231209%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231209T140508Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0ae7f36103106089a0f691773278aac438e7d61e6bf2fe4c7407040dbec94efd)

## Project Description

> Welcome to the AirBnB clone project!
> Before starting, please read the AirBnB concept page.

First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
  create all unittests to validate all our classes and storage engine

## Command Interpreter

The command interpreter, implemented in `console.py`, is built using Python and the cmd module. It provides a simple and interactive interface for users to interact with the Airbnb application. The interpreter supports various commands to perform CRUD (Create, Read, Update, Delete) operations on different object types.

## How to Start

To start the Airbnb Console, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/airbnb-console.git

    Navigate to the project directory:



   ```

2. cd airbnb-console

   - ./console.py

   ```python
   (hbnb)

   Documented commands (type help <topic>):
   ========================================
   EOF  all  count  create  destroy  help  quit  show update
   (hbnb) create User
   Welcome User You instane have been created with a Unique_id =>> d043530b-2c4d-48aa-9a63-5a967daf07a0

   (hbnb) show User d043530b-2c4d-48aa-9a63-5a967daf07a0

   [User] (d043530b-2c4d-48aa-9a63-5a967daf07a0) {'id': 'd043530b-2c4d-48aa-9a63-5a967daf07a0', 'created_at': datetime.datetime(2023, 12, 9, 15, 30, 4, 33351), 'updated_at': datetime.datetime(2023, 12, 9, 15, 30, 4, 33396)}

   (hbnb) all

   ["[User] (1d952865-4e44-46de-8268-94d3bc6e0a39) {'id': '1d952865-4e44-46de-8268-94d3bc6e0a39', 'created_at': datetime.datetime(2023, 12, 9, 13, 35, 3, 414232), 'updated_at': datetime.datetime(2023, 12, 9, 14, 57, 49, 509761), 'name': 'tee'}", "[User] (d043530b-2c4d-48aa-9a63-5a967daf07a0) {'id': 'd043530b-2c4d-48aa-9a63-5a967daf07a0', 'created_at': datetime.datetime(2023, 12, 9, 15, 30, 4, 33351), 'updated_at': datetime.datetime(2023, 12, 9, 15, 30, 4, 33396)}"]

   (hbnb) update User d043530b-2c4d-48aa-9a63-5a967daf07a0 name "omotayo"

   (hbnb) show User d043530b-2c4d-48aa-9a63-5a967daf07a0

   [User] (d043530b-2c4d-48aa-9a63-5a967daf07a0) {'id': 'd043530b-2c4d-48aa-9a63-5a967daf07a0', 'created_at': datetime.datetime(2023, 12, 9, 15, 30, 4, 33351), 'updated_at': datetime.datetime(2023, 12, 9, 15, 31, 9, 509446), 'name': 'omotayo'}
   (hbnb)
   (hbnb) (hbnb) count User
   2
   (hbnb) quit
   ```

How to Use

Once the console is running, you can use the following commands:

    create: Create a new instance of a specified class.
    Example: create User

    show: Display details of a specific instance.
    Example: show User 123

    destroy: Delete a specified instance.
    Example: destroy User 123

    all: Display all instances or instances of a specific class.
    Example: all or all User

    update: Update an instance with new attribute values.
    Example: update User 123 first_name "John"

    count: Retrieve the number of instances of a specified class.
    Example: count User

    quit or EOF: Exit the console.

# Contributors

The following people contributed to this repository.

- [Omotobora omotayo](https://github.com/Teeclever)

  - Added support for user authentication.
  - Fixed a bug in the update functionality.

- [Aniekan-abasi](https://github.com/dgamee)

  - Implemented the `count` command for various object types.
  - Updated documentation for clarity.

If you'd like to contribute to this project, please refer to our [Contribution Guidelines](CONTRIBUTING.md).

