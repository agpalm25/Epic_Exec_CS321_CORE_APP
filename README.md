# Epic_Exec_CS321_CORE_APP

This is a Community Advisor (CA) application management system for a college or university. It allows students to submit applications for CA positions, schedule interviews, and provides an admin dashboard for managing applications.

## Features

1. Application Submission: Students can submit detailed applications for CA positions.
2. Interview Scheduling: Applicants can schedule interview appointments.
3. Admin Dashboard: Administrators can view and manage applicant information, including application status, interview status, and assessment status.
4. Email Notifications: The system sends confirmation emails for application submissions and interview scheduling.

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/your-username/Epic_Exec_CS321_CORE_APP.git
   cd Epic_Exec_CS321_CORE_APP
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```
   flask db init
   flask db migrate
   flask db upgrade
   ```

5. Create a `.env` file in the root directory and add the following:
   ```
   SECRET_KEY=your_secret_key_here
   ```

## Running the Application

To run the application, use the following command:

```
flask run
```

The application will be available at `http://localhost:5000`.


## Project Structure

- `app.py`: Main application file
- `models.py`: Database models
- `views.py`: Route definitions and view functions
- `email_sender.py`: Email notification functionality
- `templates/`: HTML templates
- `static/`: Static files (CSS, JavaScript)

## License

This project is licensed under the MIT License.