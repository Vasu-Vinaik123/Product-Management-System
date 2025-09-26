# Product Management System

A comprehensive, full-stack application designed for managing products. This system provides a complete front-end interface for sellers to handle their inventory and a robust backend API for managing product data efficiently.

## ✨ Features

### Front-End
- **User Authentication**: Secure login and signup system for sellers
- **Product Management**: Intuitive interface to create, read, update, and delete product listings
- **Responsive Design**: Seamless experience across desktop and mobile devices

### Back-End
- **Secure Authentication**: Password hashing for enhanced security
- **RESTful API**: Complete CRUD endpoints for product operations
- **FastAPI Framework**: Modern, fast, and asynchronous API development
- **Comprehensive Testing**: Full API testing suite using pytest

## 🛠️ Technologies Used

### Front-End
- HTML, CSS, JavaScript
- *Built using templates and AI-generated code for rapid development*

### Back-End
- **Python** with **FastAPI**
- **SQLite** database
- **SQLAlchemy** for ORM
- **Pydantic** for data validation
- **Passlib & BCrypt** for password hashing
- **Python-JOSE** for JWT tokens

### Dependencies
```
uvicorn
sqlalchemy
pydantic
passlib
bcrypt
python-jose
python-multipart
pytest
httpx
```

## 🚀 Getting Started

### Prerequisites
Ensure you have the following installed:
- Git
- Python 3.13

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Vasu-Vinaik123/Product-Management-System.git
   cd Product-Management-System
   ```

2. **Create and activate virtual environment**
   ```bash
   # Create the environment
   python -m venv myenv

   # Activate on Windows
   myenv\Scripts\activate

   # Activate on macOS/Linux
   source myenv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

Start the FastAPI server:
```bash
uvicorn apis.main:app --reload
```

🌐 **Access Points:**
- API Documentation (Swagger UI): http://127.0.0.1:8000/docs
- Application: http://127.0.0.1:8000

## 🧪 Testing

This project uses pytest for comprehensive backend testing of all FastAPI routes.

### Run All Tests
```bash
pytest -v
```
*The `-v` flag enables verbose mode, showing detailed test results*

### Test Structure
- **tests/test_seller.py** – Seller authentication and CRUD operations
- **tests/test_product.py** – Product CRUD operations

**Testing Notes:**
- Tests use in-memory SQLite database (`sqlite:///:memory:`)
- No impact on main database during testing
- Utilizes FastAPI's TestClient via httpx for realistic HTTP request simulation

## 📝 API Endpoints

The system provides RESTful endpoints for:
- User authentication (login/signup)
- Product CRUD operations
- Seller management

*Full API documentation available at `/docs` when running the server*

## 🙏 Credits

- **Frontend**: Built using templates and AI-generated code for rapid development
- **Backend**: Custom implementation including authentication, database integration, and API logic

## 📄 License

This project is open source and available under standard terms.

---

*For issues, feature requests, or contributions, please visit the GitHub repository.*