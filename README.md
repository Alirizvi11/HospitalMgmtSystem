# Hospital Management System

A simple Hospital Management System using *Oracle Database* for backend and *Tkinter* for the frontend.

## Features
- User registration.
- Store patient data in Oracle Database.
- View and update records.

## Requirements
- *Python 3.6+*
- *Oracle Instant Client*: [Download from Oracle](https://www.oracle.com/database/technologies/instant-client.html)
- *Oracle Database*: A running Oracle instance (can be local or remote).
- *Libraries*:
  - cx_Oracle - To connect to Oracle database.
  - tkinter - For the frontend UI.

## Setup Instructions

### 1. Install Oracle Instant Client
   - Follow the instructions to install [Oracle Instant Client](https://www.oracle.com/database/technologies/instant-client.html).

### 2. Install Dependencies
   - Install Python dependencies using:
     bash
     pip install -r requirements.txt
     

### 3. Configure Oracle Connection
   - Modify db_connection.py or the connection settings in register_ui.py to match your Oracle database credentials (username, password, hostname, port, and service name).

### 4. Run the Application
   - To run the user registration UI, use the following command:
     bash
     python register_ui.py
     
   - This will open a window where you can input a username, password, and email, and then register a new user into the database.

## Database Setup

The project assumes you have a table named users with the following schema:

```sql
CREATE TABLE users (
    user_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    username VARCHAR2(100),
    password VARCHAR2(100),
    email VARCHAR2(100)
);