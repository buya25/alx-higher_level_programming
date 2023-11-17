# README: Python Object-Relational Mapping Project

## Overview

This project focuses on implementing Object-Relational Mapping (ORM) using Python and MySQL, with an emphasis on managing relationships between State and City objects in a database. The project includes scripts to perform various tasks such as selecting, filtering, updating, and deleting records from the database.

## Project Structure

The project is organized into multiple tasks, each addressing specific objectives. Here is a brief overview of each task:

### Task 0: Get all states

- Script: `0-select_states.py`
- Objective: Retrieve and display all states from the database `hbtn_0e_0_usa`.

### Task 1: Filter states

- Script: `1-filter_states.py`
- Objective: Filter and display states with names starting with 'N' from the database `hbtn_0e_0_usa`.

### Task 2: Filter states by user input

- Script: `2-my_filter_states.py`
- Objective: Allow user input to filter and display states from the database `hbtn_0e_0_usa`.

### Task 3: SQL Injection...

- Script: `3-my_safe_filter_states.py`
- Objective: Address SQL injection vulnerabilities while filtering and displaying states.

### Task 4: Cities by states

- Script: `4-cities_by_state.py`
- Objective: List all cities along with their corresponding states from the database `hbtn_0e_4_usa`.

### Task 5: All cities by state

- Script: `5-filter_cities.py`
- Objective: List all cities for a given state from the database `hbtn_0e_4_usa`.

### Task 6: First state model

- Scripts: `6-model_state.py`, `model_state.py`
- Objective: Implement a State class and establish a database connection using SQLAlchemy.

### Task 7: All states via SQLAlchemy

- Script: `7-model_state_fetch_all.py`
- Objective: Retrieve and display all State objects from the database `hbtn_0e_6_usa` using SQLAlchemy.

### Task 8: First state

- Script: `8-model_state_fetch_first.py`
- Objective: Retrieve and display the first State object from the database `hbtn_0e_6_usa` using SQLAlchemy.

### Task 9: Contains `a`

- Script: `9-model_state_filter_a.py`
- Objective: Retrieve and display State objects containing the letter 'a' from the database `hbtn_0e_6_usa` using SQLAlchemy.

### Task 10: Get a state

- Script: `10-model_state_my_get.py`
- Objective: Retrieve and display the ID of a State object based on user input from the database `hbtn_0e_6_usa` using SQLAlchemy.

### Task 11: Add a new state

- Script: `11-model_state_insert.py`
- Objective: Add a new State object ("Louisiana") to the database `hbtn_0e_6_usa` using SQLAlchemy.

### Task 12: Update a state

- Script: `12-model_state_update_id_2.py`
- Objective: Update the name of a State object with ID 2 to "New Mexico" in the database `hbtn_0e_6_usa` using SQLAlchemy.

### Task 13: Delete states

- Script: `13-model_state_delete_a.py`
- Objective: Delete all State objects containing the letter 'a' from the database `hbtn_0e_6_usa` using SQLAlchemy.

### Task 14: City relationship

- Scripts: `relationship_city.py`, `relationship_state.py`, `100-relationship_states_cities.py`
- Objective: Implement a relationship between State and City classes, creating and displaying a sample relationship in the database `hbtn_0e_100_usa` using SQLAlchemy.

### Task 15: List relationship

- Script: `101-relationship_states_cities_list.py`
- Objective: List all State and corresponding City objects from the database `hbtn_0e_101_usa` using SQLAlchemy.

## Instructions for Running Scripts

1. Clone the GitHub repository:

   ```
   git clone https://github.com/your-username/alx-higher_level_programming.git
   ```

2. Navigate to the project directory:

   ```
   cd alx-higher_level_programming/0x0F-python-object_relational_mapping
   ```

3. Run the desired script with the appropriate arguments (MySQL username, password, and database name):

   ```
   ./script_name.py mysql_username mysql_password database_name
   ```

   Replace `script_name.py` with the name of the script you want to execute.

## Notes

- Ensure that you have MySQL and the necessary Python modules installed before running the scripts.
- Follow best practices for securely handling user input to prevent SQL injection vulnerabilities.
- For Task 15 (List relationship), ensure the database `hbtn_0e_101_usa` is set up with the provided
