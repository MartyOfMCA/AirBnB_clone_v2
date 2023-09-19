# 0x02. AirBnB clone - MySQL
This is a command-line interpreter that enables users to enter command with arguments (whenever necessary) to perform special tasks. Users get to create objects using this tool, manipulate the already existing objects, retrieve details on exisiting as well and delete objects which are created.

This directory contains source code files on the AirBnB clone console project with newer and improved features over our [previous AirBnB console](https://github.com/MartyOfMCA/AirBnB_clone/tree/master). This project was created as part of our course requirement at ALX.

## Features
This project is a command-line interpreter that enables users to perform some defined operations. The core features are similar to [previous](https://github.com/MartyOfMCA/AirBnB_clone/tree/master#features) implementation details. Newer features include:
* Usage of MySQL to persist data

## Concepts
Concepts from [previous](https://github.com/MartyOfMCA/AirBnB_clone/tree/master#concepts) implementation are used in this version as well as:
* MySQL
* ORM
* SQLAlchemy
* Environment variables in Python

## Prerequisites
Additional tools needed alongside [previous tools](https://github.com/MartyOfMCA/AirBnB_clone/tree/master#prerequisites) include:
* MySQL 8.0 [Download](https://dev.mysql.com/downloads/installer/)
* MySQLdb [Download](https://stackoverflow.com/questions/25865270/how-to-install-python-mysqldb-module-using-pip)
* SQLAlchemy [Download](https://pypi.org/project/SQLAlchemy/)

## How To's
### Starting the command-line interpreter
The command-line tool can be started from any terminal on any of the supported OS. Use the following snippet to start the program in the interactive mode:

`./console.py`

This will start the command-line interface showing a prompt. This signals that the tool is ready to process the commands the user provides infinitely until the user chooses to end the session.

The tool can also be started in the non-interactive mode using the following snippet:

`echo "help" | ./console.py`

### Using the command-line interpreter
After starting the tools you can perform diverse operations directly from the command-line interface.
You can type `help` to see a list of all the available commands. You can also obtains information on how to use any of the listed commands using the following snippet:

`help command_name`

### Examples
```
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
create  help	add  change  quit

Undocumented commands:
======================
(hbnb) help create
```
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
```
