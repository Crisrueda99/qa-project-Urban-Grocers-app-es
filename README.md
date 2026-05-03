# QA Project for Urban Grocers Kit Creation

This project automates tests for the kit creation API, focusing on the 'name' field validation as per the provided checklist.

## How to run tests

1. Ensure Python and virtual environment are set up.

2. Install dependencies: pip install requests pytest

3. Update `configuration.py` with the actual server URL obtained after launching the server.

4. Run the tests: pytest create_kit_name_kit_test.py

The tests cover positive and negative scenarios for the 'name' field in kit creation requests.