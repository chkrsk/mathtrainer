# Math Trainer

Math Trainer is a simple web application built with Django, designed to help users practice basic mathematical operations. The application generates random problems for users to solve, helping them improve their memory and skills in basic math. This project is in its early stages, with potential for future development, such as adding user accounts and saving results.

## Features

- Generates random math problems (addition, subtraction, multiplication, division).
- Aimed at helping users practice and reinforce their memory of basic math operations.
- Future plans may include saving results (database functionality might be added in the future).

## Technologies

- **Django** – A Python framework for building web applications.
- **HTML, CSS, JavaScript** – Frontend technologies for displaying the user interface.
- **Database** - SQLite (by default, but can be changed to PostgreSQL or MySQL if needed)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/chkrsk/mathtrainer.git
    ```

2. Navigate to the project folder:

    ```bash
    cd mathtrainer
    ```

3. Set up the .env file and configure SECRET_KEY (settings.py):

    ```
    SECRET_KEY=your_secure_key_here
    ```

4. Apply migrations:
    
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

4. Open the application in your browser at `http://127.0.0.1:8000/`.

## Future Features

- Adding ability to save results.
- Implementing more advanced modes for practicing math problems.
- Possibility of adding an API in the future.

## License

This project is available under the MIT license.
