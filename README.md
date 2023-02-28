# Ristek_web

## Installation

Follow these steps to install to your local machine:
1. Clone the GitHub repository to a location in your local development environment using git:
   ```shell
   git clone <URL of this repository> <path in local development environment>
   ```

2. Go to the location of the cloned repository:
   ```shell
   cd <path to the cloned repository>
   ```

3. Activate the virtual environment:
   ```shell
   python -m venv env
   # Windows
   .\env\Scripts\activate
   # Linux/Unix, e.g. Ubuntu, MacOS
   source env/bin/activate
   ```

4. Install the dependencies needed to build, test, and run the application:

   ```shell
   pip install -r requirements.txt
   ```

5. Run the migrations:
   ```shell
   python manage.py makemigrations
   python manage.py migrate
   ``` 

6. Run the Django Web application using local development server:

   ```shell
   python manage.py runserver
   ```

7. Open http://localhost:8000 in your favourite Web browser to see if the Web
   application is running.