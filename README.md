# 🐛 Database Anomaly & Bug Execution Report

**Project:** Cinema Booking System  
**Environment:** Local PostgreSQL Container (Docker)  
**Executed By:** Automated Pytest Suite  

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
---
Created by Ainul idham
* **Impact:**  
  * **Booking ID 2:** Undercharged by **Rp 20,000** (Revenue Loss).
  * **Booking ID 4:** Undercharged by **Rp 450,000** (Revenue Loss).

* **Recommendation for Backend Engineer:**
  1. Implement a database `TRIGGER` or update the API endpoint logic to calculate `total_amount` strictly on the backend server before executing `INSERT INTO bookings`.
  2. Avoid trusting client-side payload for `total_amount`.
