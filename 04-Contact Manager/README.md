# Contact Manager

A command-line contact management application built with Python and JSON file storage.

## Features

* Add contacts
* View all contacts
* Search contacts by name
* Update contact information
* Delete contacts
* Store contacts in a JSON file
* Load saved contacts when the application starts
* Handle invalid menu input

## Contact Information

Each contact contains:

* Contact ID
* Name
* Phone number
* Email address

## Concepts Practiced

* Python dictionaries
* Lists and loops
* JSON
* File handling
* `json.dump()`
* `json.load()`
* CRUD operations
* Searching
* Updating and deleting records
* Exception handling
* User input validation
* Menu-driven programs

## JSON Concepts

This project helped practice the difference between:

* `dump()` → Python data → JSON file
* `load()` → JSON file → Python data
* `dumps()` → Python data → JSON string
* `loads()` → JSON string → Python data

## Data Storage

Contacts are stored in:

`contacts.json`

## Technologies

* Python
* JSON
* File handling

## Example

```text
===== CONTACT MANAGER =====

1. Add contact
2. View contacts
3. Search contact
4. Update contact
5. Delete contact
6. Exit

Enter your choice: 1
Enter name: Ali
Enter phone: 03001234567
Enter e-mail: ali@example.com

Contact added successfully
```

Example of viewing the contact:

```text
ID: 1
Name: Ali
Phone No: 03001234567
Email: ali@example.com
```

## Purpose

This project was built to practice working with JSON data, file persistence, CRUD operations, exception handling, and user input through a practical command-line application.
