# 🧮 Flask Calculator App

A simple web-based calculator built with Flask. The application allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, and division through a user-friendly HTML interface.

---

## 🚀 Features

* Web UI for input and operation selection
* Backend powered by Flask
* Performs basic arithmetic:

  * Addition
  * Subtraction
  * Multiplication
  * Division
* JSON-based API response

---

## 🛠️ Technologies Used

* **Python 3**
* **Flask**
* **HTML (Jinja templates)**
* **Bootstrap (optional)**

---

## 📁 Project Structure

```
calculator-project/
│
├── templates/
│   └── index.html         # Frontend HTML form
│
├── main.py                # Flask application
└── README.md              # Project documentation
```

---

## 🔧 Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/calculator-flask-app.git
   cd calculator-flask-app
   ```

2. **Create a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install flask
   ```

4. **Run the application**

   ```bash
   python main.py
   ```

5. **Open in Browser**
   Visit `http://localhost:5000` to use the calculator.

---

## 📡 API Endpoint

**POST** `/calculator`
Form data:

* `x`: First number
* `y`: Second number
* `operation`: Operation to perform (`addition`, `substraction`, `multiplication`, `division`)

**Response:**

```json
{
  "status": "success",
  "result": 25
}
```

---

## ⚠️ Note

This app uses Python's `eval()` to parse form inputs. **Do not use this in production** without sanitizing user inputs.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
