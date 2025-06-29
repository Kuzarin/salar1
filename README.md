# Salaries API

This is a REST API for viewing salary information and the date of the next raise, with authentication.

## How to run

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Kuzarin/salaries.git
    cd salaries
    ```

2.  **Create a virtual environment and activate it (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application using Uvicorn:**
    ```bash
    uvicorn main:app --reload
    ```

    The API will be available at `http://127.0.0.1:8000`.

## API Endpoints

*   **POST /login:** Authenticate with username and password to get an access token.
*   **GET /salary:** Get salary information and next raise date. Requires a valid access token.

## Models

*   **UserLogin:** Input model for user login (username, password).
*   **Token:** Output model for authentication token (access_token, token_type).
*   **SalaryInfo:** Output model for salary details (current_salary, next_raise_date). 