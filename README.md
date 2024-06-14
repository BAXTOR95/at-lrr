# SIRDCAT: Information System for Data Compilation and Construction of Transmission Files

## Overview

SIRDCAT is a web application built with Django and Angular, designed as an internal tool for Citibank to automate the creation of regulatory reports. This application streamlines a process that was previously manual, reducing the time needed to generate reports from hours to seconds.

## Basic Workflow

1. **Upload Data**: Users upload the necessary data files (e.g., .txt, .xls) on the resource page for the report they want to generate.
2. **Data Processing**: The uploaded data is cleaned and prepared using pandas.
3. **Generate Report**: Users navigate to the Workflow page to generate the final report. Currently, the application supports the creation of the report 'AT04 - Cartera de Credito'.
4. **Download Report**: Users can download the report as a .txt file in the required regulatory format.

## Prerequisites

- Node.js v12
- Python 3.7

## Installation

### Backend

1. **Clone the repository**:

    ```sh
    git clone https://github.com/BAXTOR95/at-lrr.git
    cd at-lrr/backend
    ```

2. **Create and activate a virtual environment**:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required Python packages**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations**:

    ```sh
    python manage.py migrate
    ```

5. **Create a superuser**:

    ```sh
    python manage.py createsuperuser
    ```

6. **Run the backend server**:

    ```sh
    python manage.py runserver
    ```

### Frontend

1. **Navigate to the frontend directory**:

    ```sh
    cd ../frontend
    ```

2. **Install the required Node.js packages using Yarn**:

    ```sh
    yarn install
    ```

3. **Run the frontend server**:
    ```sh
    yarn start
    ```

## Usage

1. Open a web browser and navigate to `http://localhost:8000` for the backend and `http://localhost:4200` for the frontend.
2. Log in with your superuser credentials.
3. Upload the necessary data files on the resource page.
4. Navigate to the Workflow page to generate and download the 'AT04 - Cartera de Creditos' report.

## Additional Setup (Optional)

If you encounter any issues with proxy settings or specific package installations, refer to the detailed installation steps in the notes section of this README.

## Contributing

Feel free to submit issues, fork the repository and send pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
