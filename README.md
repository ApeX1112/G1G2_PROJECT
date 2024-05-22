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
### for the frontend :
    the usage of html , css , js in django for the frontend :

    in addition to the ordinary html in django there s some new features :  https://docs.djangoproject.com/en/5.0/ref/templates/language/

    to link a css , js file to a html page :

        css :  
                ```sh
                {% load static %}


                <link rel="stylesheet" href="{% static 'css/styles.css' %}">
            
                ```

        js:

            ```sh
            {% load static %}

            <script src="{% static 'js/script.jsx' }"></script>
            ```




