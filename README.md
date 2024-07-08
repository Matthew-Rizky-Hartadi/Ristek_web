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

7. Open http://localhost:8000/web_app in your favourite Web browser to see if the Web
   application is running.


## Features

1. User Authentication: Register and Login functions for users
2. Add Post: User can add a post by writing in the text area and clicking post. User can post while being logged in or not.
If user is not logged in, it will be anonymous.
3. Edit Post: Authenticated users can edit post by clicking the pencil icon and entering a text in the textarea, and clicking edit.
4. Delete Post: Authenticated users can delete their own post by clicking the red trash icon.
5. User Profile: User have their own profile page which contains their own posts.

## Thank You
Thank you for trying the application, criticism and suggestions are very well appreciated.
