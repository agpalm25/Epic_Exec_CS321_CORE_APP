# Epic_Exec_CS321_CORE_APP

This is a Community Advisor (CA) application management system for a college or university. It allows students to submit applications for CA positions, schedule interviews, and provides an admin dashboard for managing applications.

## Features

1. Application Submission: Students can submit detailed applications for CA positions.
2. Interview Scheduling: Applicants can schedule interview appointments.
3. Admin Dashboard: Administrators can view and manage applicant information, including application status, interview status, and assessment status.
4. Email Notifications: The system sends confirmation emails for application submissions and interview scheduling.
5. Search Functionality: Admins can search for applicants by name.

## Project Structure

- `app.py`: Main application file, sets up the Flask app and database
- `models.py`: Database models (Admin, Appointment, ApplicantInformation, ApplicantPreferences, AdditionalInformation)
- `views.py`: Route definitions and view functions for main application logic
- `auth.py`: Authentication-related routes and functions
- `email_sender.py`: Email notification functionality
- `test_db.py`: Database initialization and testing script
- `test_sqlite.py`: SQLite database testing script
- `templates/`: HTML templates for rendering pages
- `static/`: Static files (CSS, JavaScript, images)

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

4. Set up environment variables:
   Create a `.env` file in the root directory and add the following:
   ```
   SECRET_KEY=your_secret_key_here
   JAWSDB_URL=your_database_url_here
   SENDER_EMAIL=your_email@example.com
   SENDER_PASSWORD=your_email_password
   ```

5. Initialize the database:
   ```
   python test_db.py
   ```

## Running the Application

To run the application, use the following command:

```
python app.py
```

The application will be available at `http://localhost:5000`.



## Testing

To run tests for the SQLite database setup:

```
python test_sqlite.py
```


## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.
