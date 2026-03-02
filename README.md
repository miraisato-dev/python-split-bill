# Split Bill Calculator (Python + tkinter)

A simple GUI-based split bill calculator built with Python.
This project demonstrates progressive feature development and code refactoring.

---

## 🚀 Project Overview

This application calculates how to split a bill among participants.
It includes rounding options and an organizer-free mode.

Built with:
- Python
- tkinter (standard GUI library)

---

## 📈 Version History

### v1 – Basic GUI Version
- Implemented basic bill splitting logic
- Simple input fields for number of people and total amount
- Basic rounding to 100 yen
- Minimal GUI layout

Focus: Make it work.

---

### v2 – Rounding Options Added
- Added selectable rounding units:
  - 100 yen
  - 10 yen
  - 1 yen
- Introduced radio buttons
- Improved user interaction

Focus: Feature expansion.

---

### v3 – Organizer-Free Mode
- Added option to exclude organizer from payment
- Recalculated total among remaining participants
- Added validation (minimum 2 people for organizer-free mode)
- Switched participant input to dropdown (1–20)

Focus: Practical real-world functionality.

---

### v4 – Refactored Structure
- Separated calculation logic into dedicated functions:
  - `calc_payment()`
  - `calc_organizer_free()`
- Improved exception handling (`ValueError`)
- Cleaned up execute function
- Enhanced readability and maintainability

Focus: Code quality and structure improvement.

---

## 🧠 What This Project Demonstrates

- Progressive feature development
- GUI design using tkinter
- Input validation and error handling
- Refactoring and separation of concerns
- Writing cleaner, maintainable Python code

---

## 💻 How to Run

```bash
python v4_refactored_logic.py
