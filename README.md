# Logistics Package Delivery Tracker

## Project Overview
This project is a simple but functional logistics package delivery tracker built with Python. It helps manage and track packages, delivery statuses, delivery personnel, and schedules. The data is persistently stored using SQLite, making it easy to maintain package records and update delivery statuses in real time.

## Features
- Add new packages with sender and recipient details.
- Update package delivery status with timestamps.
- Retrieve package information for tracking purposes.
- Manage delivery personnel details.
- Uses a SQLite database for data persistence.

## Technologies Used
- Python 3.x
- SQLite3 for database management
- Standard Python libraries (datetime, sqlite3)

## Installation and Usage
1. Ensure Python 3.x is installed on your system.
2. Save the project Python file (e.g., package_tracker.py).
3. Run the script from the command line:
4. The database (logistics.db) will be created automatically on the first run.
5. Use the provided functions to add packages, update status, and get package info.

## How to Extend
- Add a GUI using Tkinter or a web frontend using Flask/Django.
- Integrate real-time GPS tracking for live package location.
- Implement route optimization for delivery scheduling.
- Add notification system for delivery status changes.

