# FastAPI Online Timer

This project is a simple online timer application built with FastAPI. It demonstrates basic web application structure and includes intentional style issues for educational purposes.

## Features

- Web-based timer with start, stop, and reset functionality
- FastAPI backend
- HTML/JavaScript frontend

## Prerequisites

- Python 3.7+
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/fastapi-online-timer.git
   cd fastapi-online-timer
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install fastapi uvicorn jinja2
   ```

## Usage

1. Start the FastAPI server:
   ```
   python app.py
   ```

2. Open a web browser and navigate to `http://localhost:8000`

3. Use the "Start", "Stop", and "Reset" buttons to control the timer.

## Project Structure

- `main.py`: The FastAPI application
- `templates/index.html`: The HTML template for the timer page

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


