REST API Flask Integration with MySQL
===
Overview
----
Simple flask web application to add and retrieve products from database.
This application has only been tested on an Ubuntu environment.

Requirements
---
* [Ubuntu server on Windows](https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-11-with-gui-support#1-overview) - _follow this guide for installing Linux Server on Windows_ (**Windows Only**)  
* [Python 3](https://www.python.org/downloads/) (`sudo apt install python3` - **Linux**)
* [pipenv] (`pip install --user pipenv` - **Linux**)
* [mySQL server] (`sudo apt install mysql-server` - **Linux**)

Cloning Repo
---
To clone this repository:
* `git clone https://github.com/muhammadbsalman/restAPI_flask.git`

Running a Simulation
----
1. Enter the folder where the project was cloned to
2. Enter the following commands (Linux)
   * `pipenv shell`
   * `pipenv install`
   * `python3 app.py`
4. Use POSTMAN to test the following endpoints
   * `POST @ 127.0.0.1:5000/product`
      *`{"name":"string", "price":int, "qty":int}`
   * `GET @ 127.0.0.1:5000/product` 
---