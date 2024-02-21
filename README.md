# Bus Management System (Django)

Welcome to the Bus Management System, a web application i built using Django!

## Introduction
The Bus Management System is a comprehensive solution designed to streamline bus booking, scheduling, and management tasks. This system allows users to browse available buses, book tickets, manage schedules, and handle various administrative functions efficiently.

## Features
- **User Authentication:** Secure user authentication system with login and registration functionalities.
- **Bus Management:** Add, view, edit, and delete bus details such as name, color, number plate, and seating capacity.
- **Route Management:** Define routes with departure and arrival cities, distance, and estimated time.
- **Schedule Management:** Create schedules for buses with departure and arrival times, prices, and associated routes.
- **Ticket Booking:** Allow users to search for available buses, select seats, and book tickets for specific schedules.
- **Payment Processing:** Integration with payment gateways to facilitate secure online payments for booked tickets.
- **User Profiles:** Maintain user profiles with personal information, booking history, and contact details.
- **Administrative Panel:** Admin dashboard for managing buses, routes, schedules, payments, and user accounts.

## Installation
0. Fork this repository
1. Clone the repository: `git clone https://github.com/pha12thom/bus-management-system.git`
2. Navigate to the project directory: `cd busmanagementsystem`
3. Install dependencies: `pip install -r requirements.txt`
4. Perform database migrations: `python manage.py migrate`
5. Create a superuser for admin access: `python manage.py createsuperuser`
6. Run the development server: `python manage.py runserver`
7. Access the application in your web browser: `http://localhost:8000`

## Usage
1. Access the admin panel by navigating to `/admin` and login with your superuser credentials.
2. Manage buses, routes, schedules, payments, and user accounts through the admin dashboard.
3. Users can register, login, search for buses, book tickets, and make payments through the web interface.
4. Explore the various features and functionalities of the application to understand its capabilities fully.

## Contributors
- [Milugo Geofrey](https://github.com/pha12thom)


## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgements
- Special thanks to [Django](https://www.djangoproject.com/) for providing an excellent web framework.
- Inspired by the need for efficient bus management solutions in the transportation industry.

