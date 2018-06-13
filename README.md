# ucsd-bisb-unofficial
The unofficial information hub for students in the Bioinformatics and Systems Biology graduate program at UCSD.

## How to contribute
First, if you haven't yet, spend a few hours getting familiar with [HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML), [CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS), and [Flask](http://flask.pocoo.org). (Optionally, you might also want to look at [Bootstrap](https://getbootstrap.com/docs/4.1/getting-started/introduction/).) It might seem like a lot, but don't worry - all you need is a very basic understanding of how each of these things works. Most of the heavy lifting is taken care of by frameworks, so there's no need to read about all the details. It's better to just start developing!

Once you're ready, clone the repository and navigate to the working directory. When inside, do the following:
```
python3 -m venv venv
source venv/bin/activate
pip3 install -e .
pip3 install pytest coverage
pytest
coverage run -m pytest
coverage report
export FLASK_APP=ucsd_bisb_unofficial
export FLASK_ENV=development
flask init-db
flask run
```
You're now running the Flask development server, and you can view your local version of the site by navigating to [http://localhost:5000](http://localhost:5000) in a web browser.

## On the production server
```
python3 setup.py bdist_wheel
python3 -m venv venv
source venv/bin/activate
pip3 install dist/ucsd_bisb_unofficial-0.0.1-py3-none-any.whl
cd venv/lib/python3.6/site-packages/
export FLASK_APP=ucsd_bisb_unofficial
flask init-db
python3 configure_secret_key/__init__.py ../../../var/ucsd_bisb_unofficial-instance/
```
