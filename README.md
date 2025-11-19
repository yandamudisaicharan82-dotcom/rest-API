# rest-API
**User Management REST API (Flask) – README**

 **Overview**
this project is a simple **REST API built using Flask** as part of the Python Developer Internship Task 4.
The API allows you to manage user data using **CRUD operations**:
* **GET** – Fetch users
* **POST** – Add users
* **PUT** – Update users
* **DELETE** – Delete users
User data is stored in an **in-memory dictionary** (no database).

 **Features**
* Create new users
* Retrieve all users
* Retrieve a specific user by ID
* Update user data
* Delete users
* Simple and beginner-friendly Flask structure

**Tech Stack**
 **Python**
* **Flask**
* **Postman / Curl** (for testing the API)
**Project Structure**
project
  >>app.py         
>>README.md       
**How to Run the Project**
**1. Install Flask**
pip install flask
 **2. Run the Application**
python app.py
### **1. Get all users**
GET /users
### **2. Get user by ID**
GET /users/<id>
### **3. Add a new user**
POST /users
**Body (JSON):**
json
{
  "id": "1",
  "name": "John",
  "email": "john@example.com"
}
### **4. Update user**
PUT /users/<id>
**Body (JSON):**
json
{
  "name": "Updated Name"
}
### **5. Delete user**
DELETE /users/<id>


If you want, I can also convert this into a **PDF**, **LinkedIn post description**, or help you **improve your project**!
