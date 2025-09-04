# 🏥 Hospital Management System

A full-featured desktop application built with Python and Oracle Database to streamline hospital operations — from patient registration to billing and PDF receipt generation.

---

## 🚀 Features

- 🔐 Role-based login system (admin, doctor, etc.)
- 🧑‍⚕️ Add and manage patient records
- 📅 Book and view appointments
- 💰 Generate bills with automatic timestamps
- 🧾 Download PDF receipts with patient details
- 💊 Track medications and doctor info
- 📊 Dashboard with modular navigation

---

## 🛠️ Tech Stack

| Layer        | Technology             |
|--------------|------------------------|
| Frontend     | Tkinter (Python GUI)   |
| Backend      | Python (modular files) |
| Database     | Oracle 19c             |
| PDF Engine   | ReportLab              |
| Auth System  | USERS table validation |

---

=======
## 📸 Screenshots

### 🔐 Login Page
![Login Page](screenshots/Login.png)

### 🏥 Dashboard
![Dashboard](screenshots/Dashboard.png)

### 🧑‍⚕️ Appointment
![BookAppointment](screenshots/BookAppointment.png)

### 💰 Billing Module
![Billing](screenshots/GenerateRecipt.png)

### 🧑‍⚕️ Patient Details
![Patient Details](screenshots/AddPatient.png)

### 🧾 Bill PDF Receipt
![Bill PDF](screenshots/BillReciptPdf.png)

---


=======
## 📂 Folder Structure
HospitalManagementSystem/ 
├── pycache/ # Python cache files (ignored) 
├── ui/
|   └── dashboard_ui.py 
|   └── welcome_ui.py  
|   └── login_page.py 
|   └── appointment_ui.py 
|   └── billing_ui.py  
|   └── patient_details.py 
|   └── doctor_ui.py 
|   └── medications_ui.py 
|   └── doctor_register.py  
|   └── user_login.py 
|   └── register_ui.py 
|   └── report_ui.py 
├── services/  # Backend logic and helpers  
|   └── auth_service.py
|   └── pdf_generator.py  
├── screenshots/ # UI screenshots for README  
|   └── Login.png
|   └── Dashboard.png
|   └── BookAppointment.png
|   └── GenerateRecipt.png
|   └── AddPatient.png
|   └── BillReciptPdf.png
└── main.py # Entry point for launching the app 
└── appointment.py # Appointment details
└── billing.py  # Bill generation and DB insert 
└── db.py  # Patient record management 
└── doctor.py # Doctor record management
└── patient.py  # Patient record management
└── test_pdf.py # Sample generated report
└── README.md  # Project documentation
└── .gitignore # Git ignore rules
└── requirements.txt # Requirements , Dependencies.
└── bill_receipt.pdf  # PDF receipt creation using ReportLab
     
---
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
<<<<<<< HEAD

## 🔄 How It Works

1. **Login System**  
   Users (admin, doctor, staff) log in using credentials stored in the Oracle `USERS` table.

2. **Dashboard Navigation**  
   After login, users access modules like Patient Management, Billing, Appointments, and Reports.

3. **Patient Registration**  
   New patients are added via a Tkinter form and stored in the `PATIENTS` table.

4. **Appointment Booking**  
   Appointments are scheduled and tracked using the `APPOINTMENTS` table.

5. **Billing & PDF Generation**  
   Bills are created with `SYSDATE`, stored in `BILLING`, and receipts are generated using ReportLab.

6. **Report & Medication Modules**  
   Doctors can view patient history, prescribe medications, and generate reports.

7. **Screenshots & PDF Receipts**  
   All UI flows are documented with screenshots, and receipts are downloadable as PDFs.

=======
>>>>>>> 01eaf7284449b80ef588c32554a6ed7e51ff0443
