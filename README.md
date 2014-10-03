payshop
=======

A Flask wrapper around the Paylogic Shopping API.

Getting started
---------------
Create a virtual environment and install the requirements.

```bash
> virtualenv env
> source env/bin/activate
> pip install -r requirements.txt
```

Create a file (e.g. `privates.py`) which will contain the `API_KEY` and `API_SECRET` with which you can access the
Paylogic Shopping API. Optionally, you can include the `DEBUG` flag. The contents of the file should look like this:

```
API_KEY = '<api_key>'
API_SECRET = '<api_secret>'
DEBUG = False
```

Next create an env variable with the name `PAYSHOP_SETTINGS` that will point to this file. We use this env variable during the configuration of the `app`.

```bash
export PAYSHOP_SETTINGS=~/path/to/privates.py
```

And finally run the app from the root directory.

```bash
python run.py
```
