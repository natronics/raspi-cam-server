Raspberry Pi Camera Server
==========================


Simple python raspi web server that can take a picture.

Uses [Flask][flask] for the server, [subprocess][sub] to call [raspistill][raspistill].


Install
-------

Clone or download this repo, create a python virtual environment and run

    $ pip install -r requirements.txt


Run
---

    $ python app.py

Then open a browser an point it towards your raspi <http://raspberrypi:5000>
