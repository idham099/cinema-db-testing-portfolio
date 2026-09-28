# 🐛 Database Anomaly & Bug Execution Report
![Python](https://img.shields.io/badge/Python-312-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Testing-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![DBeaver](https://img.shields.io/badge/DBeaver-Database_Tool-382923?style=for-the-badge&logo=dbeaver&logoColor=white)

---

**Project:** Cinema Booking System  
**Environment:** Local PostgreSQL Container (Docker)  
**Executed By:** Automated Pytest Suite to Covers Data Integrity, Financial Reconciliation, and Race Condition Tests.

Here's the demo link: 👉 **[Demo Testing](https://youtu.be/uzTyumILce8)**

---

<img width="1917" height="1078" alt="image" src="https://github.com/user-attachments/assets/abedd0bf-d1b3-4afd-a8ae-a92e0dd70114" />
<img width="1917" height="1078" alt="image" src="https://github.com/user-attachments/assets/96505403-49c6-41be-b22f-512d6dbdf92b" />
<img width="1917" height="1078" alt="image" src="https://github.com/user-attachments/assets/a0da97bf-5797-4dfe-8452-7fb31adfac9a" />
<img width="1917" height="1078" alt="image" src="https://github.com/user-attachments/assets/3ee00996-4fc2-4816-ba6b-9855b44c52a2" />
<img width="1917" height="1078" alt="image" src="https://github.com/user-attachments/assets/82dc2f07-bb4e-4707-8bfc-492cc27be9fa" />
<img width="1917" height="1078" alt="image" src="https://github.com/user-attachments/assets/3aa48725-096c-4887-a34a-98d585f7efad" />
<img width="1917" height="1078" alt="image" src="https://github.com/user-attachments/assets/59dd7b3c-a446-40d3-8117-422b07cfff09" />
<img width="1535" height="862" alt="image" src="https://github.com/user-attachments/assets/d598c33a-720d-49bd-a997-a801c9380cd2" />

## 🛠️ How to Run Locally

Follow these instructions to set up the environment and run the automated database testing suite on your local machine.

### Prerequisites

Ensure you have the following installed on your system:
* **Docker & Docker Compose** (Desktop or CLI)
* **Python 3.10+**
* **Git**
* *(Optional)* **DBeaver** or any database GUI client for visual inspection

---

### Getting Started

#### 1. Clone the Repository
```bash
git clone [https://github.com/idham099/cinema-db-testing-portfolio.git](https://github.com/idham099/cinema-db-testing-portfolio.git)
cd cinema-db-testing-portfolio
```

##### 2. Set Up Virtual Environment & Dependencies
It is recommended to use a Python virtual environment:
```
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. Start the PostgreSQL Container
Spin up the isolated PostgreSQL database instance using Docker Compose:
```
docker-compose up -d
```
This will initialize the database container and automatically run the schema migration and initial seed data scripts.

#### 4. Verify Database Connection (Optional)
You can verify that the container is running with:
```
docker ps
```
* Host: localhost
* Port: 5432 (or your configured port)
* Database Name: cinema_db
* User/Password: postgres / postgres (adjust according to your .env / docker-compose setup)

---

🧪 Executing the Test Suite
Run all automated test cases using pytest:
```
# Run all database test cases
pytest

# Run tests with detailed console log output
pytest -v -s

# Run specific test modules (e.g., Financial Reconciliation)
pytest tests/test_reconciliation.py

# Run concurrency / race condition tests only
pytest tests/test_concurrency.py
```

---

#### Generating Test Reports
To generate an HTML test execution report:
```
pytest --html=report.html --self-contained-html
```

---

#### 🧹 Cleanup
To stop and remove the Docker container and reset the database state:
```
docker-compose down -v
```

---

## Bug Summary

| Bug ID | Test Case | Severity | Status | Summary |
| :--- | :--- | :--- | :--- | :--- |
| **BUG-01** | `test_reconciliation.py` | **CRITICAL** | OPEN | Discrepancy between `recorded_amount` and calculated total price in `bookings` table. |

---

## Detailed Findings

### BUG-01: Financial Discrepancy in Transaction Bookings

* **Description:**  
  Found mismatched financial records where `total_amount` in the `bookings` table does not match the actual calculation (`total_seats * ticket_price`).
  
* **Automated Test Output:**
  ```text
  AssertionError: DITEMUKAN BUG FINANSIAL! 
  Detail: [
    (2, Decimal('80000.00'), Decimal('100000.00'), Decimal('-20000.00')), 
    (4, Decimal('50000.00'), Decimal('500000.00'), Decimal('-450000.00'))
  ]
  ```

* **Impact:**  
  * **Booking ID 2:** Undercharged by **Rp 20,000** (Revenue Loss).
  * **Booking ID 4:** Undercharged by **Rp 450,000** (Revenue Loss).

* **Recommendation for Backend Engineer:**
  1. Implement a database `TRIGGER` or update the API endpoint logic to calculate `total_amount` strictly on the backend server before executing `INSERT INTO bookings`.
  2. Avoid trusting client-side payload for `total_amount`.

---
Created by Ainul idham
