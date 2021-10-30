# Beatport Top 100 API

Simple Django app API to automatically update Top 100 by style from Beatport website using scrapping (free API).<br>

![alt text](https://res.cloudinary.com/dhdgnx4mc/image/upload/v1632334920/media/GitHub/qmrsmhhkjtyjxclts18g.png)

## Installation

Install dependencies

```bash
pip install -r requirements.txt
```
If you get errors installing dependencies, use Python 3.9.

Use this website [Djecrety](https://djecrety.ir) to generate a new django secret key.<br>
Open ```settings.py``` and copy the new secret key and change DEBUG and ALLOWED_HOSTS

```python
SECRET_KEY = 'YOUR DJANGO SECRET KEY'
DEBUG = True
ALLOWED_HOSTS = []
```
## Usage

Go to the folder where is ```manage.py``` and migrate database
```bash
python3 manage.py migrate
```
Create Super User
```bash
python3 manage.py createsuperuser
```

Now we can start the server

```bash
python3 manage.py runserver
```
Go to http://127.0.0.1:8000/admin/ and login to open administrator interface

Run ```beatport_main.py``` for scrape Top 100 and POST to the Database
```python
if __name__ == "__main__":
    load_json(source='sources_data.json')
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

