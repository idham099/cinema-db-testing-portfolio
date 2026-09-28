# 🐛 Database Anomaly & Bug Execution Report

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
