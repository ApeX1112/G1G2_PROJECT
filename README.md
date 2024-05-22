# G1G2_PROJECT

## Description
The main objective of the project, as stated before, is the development of a model to predict the additional time an aircraft will spend in the airport due to the deicing period. There are, however, things surrounding such a model that also need to be created so it can be useful. Thus, it’s expected that, at the end of the project, the following list of deliverables be adequately completed:

An AI model to predict the deicing time of a plane An API to access such a model A visual way to show the previously mentioned AI model working

A document on how to use all of these programs, what their inputs and outputs are, will also be needed.

## Installation
To install this project, And Have Acces to the Interface:

1. Clone the repository:

    ```sh
    git clone https://github.com/ApeX1112/G1G2_PROJECT.git
    ```

2. Activate the Virtual Environment (Recommended)
-- for windows 

    ```sh
    env\Scripts\activate
    ```
3. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Navigate to the project directory:

    ```sh
    cd projetg1g2
    ```
5. Run the Server 

    ```sh
    python manage.py runserver 
    ```
6. open 'http://127.0.0.1:8000/'

## Usage

### For the Frontend

The usage of HTML, CSS, and JavaScript in Django for the frontend:

In addition to the ordinary HTML in Django, there are some new features: [Django Template Language](https://docs.djangoproject.com/en/5.0/ref/templates/language/)

#### Linking CSS and JS Files to an HTML Page

To link a CSS file to an HTML page, use the following code:

```html
{% load static %}
css : <link rel="stylesheet" href="{% static 'css/styles.css' %}">
js : <script src="{% static 'js/script.jsx' }"></script>

Make sure to include {% load static %} at the beginning of your HTML file to load the static files.





