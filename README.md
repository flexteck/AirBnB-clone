# AirBnB Clone

## Description
The **AirBnB Clone** project is a command-line application that simulates the back-end functionalities of the AirBnB web platform. This is the first step towards developing a full web application, handling data serialization, persistence, and a command interpreter for object manipulation.

The main objectives of this project are:
- Build a **custom command-line interpreter** to manage the objects of the system.
- Implement the logic to create, retrieve, update, and delete objects (CRUD operations).
- Store data persistently using JSON serialization/deserialization.
- Lay the foundation for future implementation of a **web application** with a front-end interface.

---

## Command Interpreter
The **Command Interpreter** serves as the core interface to interact with the system’s back-end.

### Features:
- Interactive and non-interactive modes.
- Supports object management: create, show, destroy, update.
- Handles different data models such as **User, Place, City, State, Amenity, Review.**

---

## How to Start It
Clone this repository to get started:
```sh
$ git clone https://github.com/your-username/AirBnB_clone.git
$ cd AirBnB_clone
```
Make sure the script is executable:
```sh
$ chmod +x console.py
```
Run the command interpreter in interactive mode:
```sh
$ ./console.py
(hbnb)
```
Or use it in non-interactive mode:
```sh
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
```

---

## How to Use It
### Basic Commands

| Command | Description |
|---------|-------------|
| `help` | Displays a list of available commands |
| `quit` | Exits the command interpreter |
| `EOF` | Exits the program using Ctrl+D |
| `create <class>` | Creates a new instance of a class |
| `show <class> <id>` | Displays the string representation of an object |
| `destroy <class> <id>` | Deletes an instance |
| `all [class]` | Displays all instances or instances of a specific class |
| `update <class> <id> <attr> <value>` | Updates an attribute of an instance |

### Example Usage
```sh
$ ./console.py
(hbnb) create User
7d027c22-25d5-42bf-a734-2e8f22de8a92
(hbnb) show User 7d027c22-25d5-42bf-a734-2e8f22de8a92
[User] (7d027c22-25d5-42bf-a734-2e8f22de8a92) {'id': '7d027c22-25d5-42bf-a734-2e8f22de8a92', 'created_at': '2025-02-19T12:00:00', 'updated_at': '2025-02-19T12:00:00'}
(hbnb) all User
[User] (7d027c22-25d5-42bf-a734-2e8f22de8a92) {'id': '7d027c22-25d5-42bf-a734-2e8f22de8a92', 'created_at': '2025-02-19T12:00:00', 'updated_at': '2025-02-19T12:00:00'}
(hbnb) destroy User 7d027c22-25d5-42bf-a734-2e8f22de8a92
(hbnb) quit
```

---

## AUTHORS
All contributors to this project are listed in the `AUTHORS` file at the root of the repository. The format follows Docker’s standard, including names and emails.
```sh
$ cat AUTHORS
John Doe <johndoe@example.com>
Jane Smith <janesmith@example.com>
```

---

## GitHub Workflow
To collaborate effectively:
- **Use branches** to separate features: `git checkout -b feature-branch`
- **Make pull requests** for code review and approval before merging to `main`
- **Write clear commit messages** to document progress

Example:
```sh
$ git commit -m "Implemented create command for User class"
$ git push origin feature-branch
$ gh pr create --title "Add User class creation" --body "Implemented the create command for User instances."
```

---

## License
This project is licensed under the MIT License.

---

## Contact
- GitHub: [flexteck](https://github.com/flexteck)
- Email: andrewandrenzanthony.com


