# SauceDemo Automation Framework (Playwright + Pytest)

## Overview

This project is an end-to-end test automation framework built using Playwright and Pytest.
It automates key user flows on the SauceDemo application, including login, product selection, cart validation, and checkout.
The project demonstrates a transition from manual testing to automation, focusing on clean structure, reusable components, and data-driven testing.


## Tech Stack

- Python
- Playwright
- Pytest
- Pytest-HTML (reporting)


## Project Structure

pages/            → Page Object Model classes  
tests/            → Test cases  
test_data/        → Test data (products dictionary)  
reports/          → Test execution reports  
conftest.py       → Fixtures (browser setup, login, etc.)  
pytest.ini        → Pytest configuration  


## How to Run

1. Install dependencies:
pip install -r requirements.txt

2. Install Playwright browsers:
playwright install

3. Run tests:
pytest

4. View report:
Open reports/report.html in your browser


## Test Coverage

- Login functionality (valid & invalid scenarios)
- Product listing validation
- Add/remove items from cart
- Cart validation
- Checkout process
- Data validation between cart and checkout overview
- Total price validation


## Key Features

- Page Object Model (POM) design
- Data-driven testing using dictionaries
- Dynamic locators for reusable components
- Validation of data consistency across pages
- End-to-end user journey automation


## Reporting

Test execution reports are generated using pytest-html and stored in the reports/ folder.


## Author

Jason Usswald  
Software Test Analyst transitioning into Automation Testing