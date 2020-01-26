# Simple API Restful with Flask from Python

The api.py file have a simple code for API Restful with the Flask package. Then, before run the API, do you need install the Python 3, and the Flask package with pip.

<span style="font-family:Courrier">sudo apt install python3</span>
<span style="font-family:Courrier">sudo apt install python3-pip</span>
<span style="font-family:Courrier">pip3 install Flask</span>
<span style="font-family:Courrier">pip3 install Flask-RESTful</span>

After install the Python and Flask, do you can run the api.py file and in your browser go to URL [http://localhost:5000/api](http://localhost:5000/api).

# Explain the code

## A API have four basic methods: GET, POST, PUT and DELETE.

### GET

The GET method use for get information, in line 17, the method GET return the datas about the ID informated in request query string. 

<span style="font-family:Courrier">
    def get(self):
        return {
            'name': 'Mateus Oliveira',
            'escola': "IFRN/Par",
            'orientador': "Jurandy",
            'curso': 'Informática',
            'email': 'matews5522@gmail.com',
            'phone': '084998177501',
        }
</span>

For example:

go to URL: [http://localhost:5000/api?id=1](http://localhost:5000/api?id=1). And a JSON object is returned for you with the informations for the user with ID 1.

### POST

## Data Bases

In this simple code, I didn't use data bases, because I did show the API and her methods for a frontend applications use the API. But if you will implement a data bases, I recommend the NoSQL Data Bases MongoDB, and you can use the MongoDB in Python with the [PyMongo](https://api.mongodb.com/python/current/) package.