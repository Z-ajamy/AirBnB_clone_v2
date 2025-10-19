# 0x04. AirBnB clone - Web framework

## Description
This project is part of the AirBnB clone series, focusing on building a web framework using Flask. You'll learn how to create dynamic web applications, work with routes, templates, and integrate with your existing storage engine. This marks the transition from command-line interfaces to web-based user interfaces.

## Concepts
For this project, you should understand:
- **Web frameworks fundamentals**
- **Flask framework**
- **Routing in Flask**
- **Template engines (Jinja2)**
- **HTML/CSS basics**
- **HTTP methods (GET, POST)**
- **RESTful API principles**

## Background Context
In this project, you'll build the web interface for your AirBnB clone. You'll start by creating simple Flask applications and progressively add more complexity, including database integration and dynamic content rendering.

### What is Flask?
Flask is a lightweight WSGI web application framework written in Python. It's designed to make getting started quick and easy, with the ability to scale up to complex applications.

### What is a Web Framework?
A web framework is a software framework designed to support the development of web applications including web services, web resources, and web APIs. It provides a standard way to build and deploy web applications.

## Learning Objectives
At the end of this project, you should be able to explain:
- What is a Web Framework
- How to build a web framework with Flask
- How to define routes in Flask
- What is a route
- How to handle variables in a route
- What is a template
- How to create an HTML response in Flask by using a template
- How to create a dynamic template (loops, conditions…)
- How to display in HTML data from a MySQL database

## Requirements

### Python Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have documentation
- All your classes should have documentation
- All your functions (inside and outside a class) should have documentation
- A documentation is not a simple word, it's a real sentence explaining the purpose

### HTML/CSS Files
- Allowed editors: `vi`, `vim`, `emacs`
- All your files should end with a new line
- A `README.md` file at the root of the folder of the project is mandatory
- Your code should be W3C compliant and validate with W3C-Validator
- All your CSS files should be in `styles` folder
- All your images should be in `images` folder
- You are not allowed to use `!important` or `id` (`#...` in the CSS file)
- All tags must be in uppercase
- Current screenshots have been done on Chrome 56.0.2924.87
- No cross browsers

## Project Structure

```
web_flask/
├── __init__.py
├── 0-hello_route.py
├── 1-hbnb_route.py
├── 2-c_route.py
├── 3-python_route.py
├── 4-number_route.py
├── 5-number_template.py
├── 6-number_odd_or_even.py
├── 7-states_list.py
├── 8-cities_by_states.py
├── 9-states.py
├── 10-hbnb_filters.py
├── 100-hbnb.py
├── templates/
│   ├── 5-number.html
│   ├── 6-number_odd_or_even.html
│   ├── 7-states_list.html
│   ├── 8-cities_by_states.html
│   ├── 9-states.html
│   ├── 10-hbnb_filters.html
│   └── 100-hbnb.html
└── static/
    ├── styles/
    │   ├── 3-common.css
    │   ├── 3-header.css
    │   ├── 3-footer.css
    │   ├── 4-common.css
    │   ├── 4-filters.css
    │   ├── 6-filters.css
    │   └── 8-places.css
    └── images/
        ├── icon.png
        └── logo.png
```

## Tasks

### 0. Hello Flask!
**File:** `0-hello_route.py`

Write a script that starts a Flask web application listening on `0.0.0.0`, port `5000`.

**Routes:**
- `/`: display "Hello HBNB!"

**Requirements:**
- You must use the option `strict_slashes=False` in your route definition

**Example:**
```bash
$ python3 -m web_flask.0-hello_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

```bash
$ curl 0.0.0.0:5000 ; echo ""
Hello HBNB!
```

---

### 1. HBNB
**File:** `1-hbnb_route.py`

Write a script that starts a Flask web application.

**Routes:**
- `/`: display "Hello HBNB!"
- `/hbnb`: display "HBNB"

**Example:**
```bash
$ curl 0.0.0.0:5000/hbnb ; echo ""
HBNB
```

---

### 2. C is fun!
**File:** `2-c_route.py`

Write a script that starts a Flask web application.

**Routes:**
- `/`: display "Hello HBNB!"
- `/hbnb`: display "HBNB"
- `/c/<text>`: display "C " followed by the value of the text variable (replace underscore `_` symbols with a space)

**Example:**
```bash
$ curl 0.0.0.0:5000/c/is_fun ; echo ""
C is fun
$ curl 0.0.0.0:5000/c/cool ; echo ""
C cool
```

---

### 3. Python is cool!
**File:** `3-python_route.py`

Write a script that starts a Flask web application.

**Routes:**
- `/`: display "Hello HBNB!"
- `/hbnb`: display "HBNB"
- `/c/<text>`: display "C " followed by the value of the text variable
- `/python/<text>`: display "Python ", followed by the value of the text variable (default value of text is "is cool")

**Example:**
```bash
$ curl 0.0.0.0:5000/python/is_magic ; echo ""
Python is magic
$ curl 0.0.0.0:5000/python ; echo ""
Python is cool
```

---

### 4. Is it a number?
**File:** `4-number_route.py`

Write a script that starts a Flask web application.

**Routes:**
- `/`: display "Hello HBNB!"
- `/hbnb`: display "HBNB"
- `/c/<text>`: display "C " followed by the value of the text variable
- `/python/<text>`: display "Python ", followed by the value of text
- `/number/<n>`: display "n is a number" only if n is an integer

**Example:**
```bash
$ curl 0.0.0.0:5000/number/89 ; echo ""
89 is a number
$ curl 0.0.0.0:5000/number/8.9
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
```

---

### 5. Number template
**Files:** `5-number_template.py`, `templates/5-number.html`

Write a script that starts a Flask web application.

**Routes:**
- All previous routes
- `/number_template/<n>`: display an HTML page only if n is an integer
  - H1 tag: "Number: n" inside the tag BODY

**Example:**
```bash
$ curl 0.0.0.0:5000/number_template/89 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 89</H1>
    </BODY>
</HTML>
```

---

### 6. Odd or even?
**Files:** `6-number_odd_or_even.py`, `templates/6-number_odd_or_even.html`

Write a script that starts a Flask web application.

**Routes:**
- All previous routes
- `/number_odd_or_even/<n>`: display an HTML page only if n is an integer
  - H1 tag: "Number: n is even|odd" inside the tag BODY

**Example:**
```bash
$ curl 0.0.0.0:5000/number_odd_or_even/89 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 89 is odd</H1>
    </BODY>
</HTML>
```

---

### 7. Improve engines
**Files:** `7-states_list.py`, `templates/7-states_list.html`

Before using Flask to display our HBNB data, you will need to update some parts of our engine.

Update `FileStorage` to:
- Add `close()` method that calls `reload()` method for deserializing the JSON file to objects

Write a script that starts a Flask web application.

**Routes:**
- `/states_list`: display an HTML page with the list of all State objects present in DBStorage sorted by name (A->Z)

**Example:**
```html
<UL>
    <LI>California</LI>
    <LI>Arizona</LI>
    ...
</UL>
```

---

### 8. List of states
**Files:** `8-cities_by_states.py`, `templates/8-cities_by_states.html`

Write a script that starts a Flask web application.

**Routes:**
- `/cities_by_states`: display an HTML page with the list of all State objects with their cities

**Example:**
```html
<UL>
    <LI>California
        <UL>
            <LI>San Francisco</LI>
            <LI>Los Angeles</LI>
        </UL>
    </LI>
    <LI>Arizona
        <UL>
            <LI>Phoenix</LI>
        </UL>
    </LI>
</UL>
```

---

### 9. States and State
**Files:** `9-states.py`, `templates/9-states.html`

Write a script that starts a Flask web application.

**Routes:**
- `/states`: display an HTML page with the list of all State objects
- `/states/<id>`: display an HTML page with info about the state with that id

---

### 10. HBNB filters
**Files:** `10-hbnb_filters.py`, `templates/10-hbnb_filters.html`, `static/`

Write a script that starts a Flask web application.

**Routes:**
- `/hbnb_filters`: display the HTML page with filters (states, amenities)

**Requirements:**
- Use the AirBnB static files
- Load states and amenities from DBStorage

---

### 11. HBNB is alive!
**Files:** `100-hbnb.py`, `templates/100-hbnb.html`, `static/`

Write a script that starts a Flask web application.

**Routes:**
- `/hbnb`: display the full AirBnB clone HTML page with filters and places

---

## Flask Basics

### Installing Flask

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Linux/Mac
# or
venv\Scripts\activate  # On Windows

# Install Flask
pip install Flask

# Install other dependencies
pip install -r requirements.txt
```

### Basic Flask Application

```python
#!/usr/bin/python3
"""Start a Flask web application"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """Return a greeting"""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
```

### Running Flask Applications

```bash
# Method 1: Direct execution
python3 -m web_flask.0-hello_route

# Method 2: Using Flask command
export FLASK_APP=web_flask.0-hello_route
flask run --host=0.0.0.0 --port=5000

# Method 3: Debug mode
python3 -m web_flask.0-hello_route
# In the code, set: app.run(host='0.0.0.0', port=5000, debug=True)
```

---

## Flask Routing

### Basic Routes

```python
@app.route('/')
def index():
    return "Index Page"

@app.route('/hello')
def hello():
    return "Hello, World!"
```

### Variable Rules

```python
@app.route('/user/<username>')
def show_user(username):
    return f'User: {username}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post: {post_id}'
```

### Converter Types

- `string`: (default) accepts any text without a slash
- `int`: accepts positive integers
- `float`: accepts positive floating point values
- `path`: like string but also accepts slashes
- `uuid`: accepts UUID strings

### Default Values

```python
@app.route('/python/')
@app.route('/python/<text>')
def python_route(text='is cool'):
    return f'Python {text}'
```

### Strict Slashes

```python
# Without strict_slashes=False
@app.route('/projects/')  # Only /projects/ works

# With strict_slashes=False
@app.route('/projects/', strict_slashes=False)
# Both /projects and /projects/ work
```

---

## Jinja2 Templates

### Basic Template Usage

```python
from flask import render_template

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)
```

### Template File (`templates/hello.html`)

```html
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Hello {{ name }}!</H1>
    </BODY>
</HTML>
```

### Template Variables

```python
@app.route('/user/<username>')
def user_profile(username):
    user = {'username': username, 'email': f'{username}@example.com'}
    return render_template('profile.html', user=user)
```

```html
<H1>{{ user.username }}</H1>
<P>Email: {{ user.email }}</P>
```

### Template Loops

```python
@app.route('/states')
def states_list():
    states = storage.all(State).values()
    return render_template('states.html', states=states)
```

```html
<UL>
{% for state in states %}
    <LI>{{ state.name }}</LI>
{% endfor %}
</UL>
```

### Template Conditionals

```html
{% if number % 2 == 0 %}
    <H1>Number: {{ number }} is even</H1>
{% else %}
    <H1>Number: {{ number }} is odd</H1>
{% endif %}
```

### Template Filters

```html
<!-- Uppercase -->
<H1>{{ name|upper }}</H1>

<!-- Length -->
<P>Length: {{ states|length }}</P>

<!-- Default value -->
<P>{{ value|default('N/A') }}</P>

<!-- Sort -->
{% for state in states|sort(attribute='name') %}
    <LI>{{ state.name }}</LI>
{% endfor %}
```

---

## Static Files

### Directory Structure

```
static/
├── styles/
│   ├── common.css
│   └── header.css
├── images/
│   └── logo.png
└── scripts/
    └── main.js
```

### Linking Static Files in Templates

```html
<!-- CSS -->
<LINK rel="stylesheet" type="text/css" href="{{ url_for('static', filename='styles/common.css') }}">

<!-- Images -->
<IMG src="{{ url_for('static', filename='images/logo.png') }}" alt="Logo">

<!-- JavaScript -->
<SCRIPT src="{{ url_for('static', filename='scripts/main.js') }}"></SCRIPT>
```

---

## Database Integration

### Importing Storage

```python
from models import storage
from models.state import State
```

### Fetching Data

```python
@app.route('/states_list')
def states_list():
    """Display list of states"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template('states_list.html', states=sorted_states)
```

### Teardown Context

```python
@app.teardown_appcontext
def teardown_db(exception):
    """Close storage after each request"""
    storage.close()
```

### Accessing Relationships

```python
@app.route('/cities_by_states')
def cities_by_states():
    """Display states with their cities"""
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    return render_template('cities_by_states.html', states=states)
```

```html
<UL>
{% for state in states %}
    <LI>{{ state.name }}
        <UL>
        {% for city in state.cities|sort(attribute='name') %}
            <LI>{{ city.name }}</LI>
        {% endfor %}
        </UL>
    </LI>
{% endfor %}
</UL>
```

---

## Testing Your Flask Application

### Using cURL

```bash
# GET request
curl http://0.0.0.0:5000/
curl http://0.0.0.0:5000/states_list

# View headers
curl -I http://0.0.0.0:5000/

# Follow redirects
curl -L http://0.0.0.0:5000/redirect

# Verbose output
curl -v http://0.0.0.0:5000/
```

### Using Browser

Simply navigate to `http://0.0.0.0:5000/` or `http://localhost:5000/`

### Using Python Requests

```python
import requests

response = requests.get('http://0.0.0.0:5000/')
print(response.text)
print(response.status_code)
```

---

## HTML/CSS Requirements

### HTML Uppercase Tags

```html
<!-- Correct -->
<HTML>
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Hello</H1>
    </BODY>
</HTML>

<!-- Incorrect -->
<html>
    <head>
        <title>HBNB</title>
    </head>
</html>
```

### CSS Organization

```
static/
└── styles/
    ├── 3-common.css      # Common styles
    ├── 3-header.css      # Header styles
    ├── 3-footer.css      # Footer styles
    ├── 4-filters.css     # Filter styles
    └── 8-places.css      # Places styles
```

### W3C Validation

```bash
# Validate HTML
# Use https://validator.w3.org/

# Validate CSS
# Use https://jigsaw.w3.org/css-validator/
```

---

## Debug Mode

### Enabling Debug Mode

```python
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
```

**Benefits:**
- Auto-reload on code changes
- Interactive debugger in browser
- Detailed error messages

**Warning:** Never use debug mode in production!

---

## Common Issues and Solutions

### Issue 1: Port Already in Use
```
OSError: [Errno 98] Address already in use
```

**Solution:**
```bash
# Find process using port 5000
lsof -i :5000

# Kill the process
kill -9 <PID>

# Or use a different port
app.run(host='0.0.0.0', port=5001)
```

### Issue 2: Template Not Found
```
jinja2.exceptions.TemplateNotFound: template.html
```

**Solution:**
- Ensure `templates/` directory exists
- Check template filename spelling
- Verify file is in correct location

### Issue 3: Static Files Not Loading

**Solution:**
```python
# Ensure using url_for
<LINK rel="stylesheet" href="{{ url_for('static', filename='styles/common.css') }}">

# Not hardcoded path
<LINK rel="stylesheet" href="/static/styles/common.css">
```

### Issue 4: Import Errors

**Solution:**
```bash
# Ensure you're in the project root
export PYTHONPATH="${PYTHONPATH}:/path/to/AirBnB_clone_v2"

# Or run as module
python3 -m web_flask.0-hello_route
```

### Issue 5: Database Connection Issues

**Solution:**
```python
# Ensure storage is properly initialized
from models import storage

# Close storage after each request
@app.teardown_appcontext
def teardown_db(exception):
    storage.close()
```

---

## Best Practices

### 1. Route Organization
```python
# Group related routes together
# Use blueprints for larger applications

# Use descriptive function names
@app.route('/states/<id>')
def show_state(id):
    """Display a specific state"""
    pass
```

### 2. Error Handling
```python
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500
```

### 3. Template Inheritance
```html
<!-- base.html -->
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>{% block title %}HBNB{% endblock %}</TITLE>
    </HEAD>
    <BODY>
        {% block content %}{% endblock %}
    </BODY>
</HTML>

<!-- states.html -->
{% extends "base.html" %}
{% block content %}
    <H1>States</H1>
    <UL>
    {% for state in states %}
        <LI>{{ state.name }}</LI>
    {% endfor %}
    </UL>
{% endblock %}
```

### 4. Security
```python
# Never expose debug mode in production
app.run(debug=False)

# Use environment variables for secrets
import os
app.secret_key = os.environ.get('SECRET_KEY')

# Sanitize user input
from markupsafe import escape
@app.route('/user/<username>')
def show_user(username):
    return f'User: {escape(username)}'
```

---

## Resources

- [What is a Web Framework?](https://intelegain-technologies.medium.com/what-are-web-frameworks-and-why-you-need-them-c4e8806bd0fb)
- [Flask Official Documentation](https://flask.palletsprojects.com/)
- [Jinja2 Documentation](https://jinja.palletsprojects.com/)
- [Flask Quickstart](https://flask.palletsprojects.com/en/2.3.x/quickstart/)
- [Routing in Flask](https://flask.palletsprojects.com/en/2.3.x/quickstart/#routing)
- [Rendering Templates](https://flask.palletsprojects.com/en/2.3.x/quickstart/#rendering-templates)
- [HTML Validator](https://validator.w3.org/)
- [CSS Validator](https://jigsaw.w3.org/css-validator/)

## Author
This project is part of the ALX Software Engineering Program - AirBnB Clone Project Series.

## License
This project is licensed under the terms of the ALX Software Engineering Program.
