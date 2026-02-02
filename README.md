# Ecommerce_DJANGOReact

A full-stack E-commerce application built with **Django** (Backend) and **React** (Frontend). This project implements a RESTful API to manage products, categories, and shopping cart functionality using a decoupled architecture.

---

## 🛠️ Tech Stack

* **Backend:** Python, Django, Django REST Framework
* **Frontend:** React.js, Axios
* **Database:** SQLite (default) / PostgreSQL
* **Styling:** TailwindCSS

---

## 🔌 API Endpoints

The backend provides the following API routes for the frontend to consume.

### Product Management
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/products/` | Fetch a list of all products |
| `GET` | `/products/<id>` | Fetch details of a single product |
| `GET` | `/categories` | Fetch all product categories |

### Shopping Cart
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/cart/` | Get current items in the user's cart |
| `POST` | `/cart/add/` | Add an item to the cart |
| `POST` | `/cart/remove/` | Remove an item from the cart |

---

## 🚀 Installation & Setup

Follow these steps to run the project locally.

### 1. Clone the Repository
```bash
git clone [https://github.com/mesailesh7/Ecommerce_DJANGOReact.git](https://github.com/mesailesh7/Ecommerce_DJANGOReact.git)
cd Ecommerce_DJANGOReact

### 2. Backend Setup (Django)

Navigate to the root directory where manage.py is located.

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Run the backend server
python manage.py runserver

```
The backend API will run at http://127.0.0.1:8000/

### 3. Frontend Setup (React)

Open a new terminal and navigate to the frontend directory.

cd frontend

# Install Node modules
npm install

# Start the React development server
npm start

The frontend application will run at http://127.0.0.1:3000/
