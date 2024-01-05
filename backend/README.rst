Flaskr
======

The basic blog app built in the Flask `tutorial`_.

.. _tutorial: https://flask.palletsprojects.com/tutorial/


Install
-------

**Be sure to use the same version of the code as the version of the docs
you're reading.** You probably want the latest tagged version, but the
default Git version is the main branch. ::

    # clone the repository
    $ git clone https://github.com/pallets/flask
    $ cd flask
    # checkout the correct version
    $ git tag  # shows the tagged versions
    $ git checkout latest-tag-found-above
    $ cd examples/tutorial

Create a virtualenv and activate it::

    $ python3 -m venv .venv
    $ . .venv/bin/activate

Or on Windows cmd::

    $ py -3 -m venv .venv
    $ .venv\Scripts\activate.bat

Install Flaskr::

    $ pip install -e .

Or if you are using the main branch, install Flask from source before
installing Flaskr::

    $ pip install -e ../..
    $ pip install -e .


Run
---

.. code-block:: text

    $ flask --app src init-db
    $ flask --app src run --debug

Open http://127.0.0.1:5000 in a browser.


Test
----

::

    $ pip install '.[test]'
    $ pytest

Run with coverage report::

    $ coverage run -m pytest
    $ coverage report
    $ coverage html  # open htmlcov/index.html in a browser


API design
======

POST /file
0- Validar los inputs
1- Agregar un nuevo filex
2- Agregar una nueva estación relacionado con el filex del pto. 1
3- Agregar de pecho file.id y technician_id (desde el request) a tabla technician_file
4- Responder código HTTP

GET /file/<id>
0- Buscar por id en filex
1- Buscar la estación
2- Buscar técnico
3- Combinar todos los objetos
4- Responder todos los campos del expediente

GET /file?includeDeleted (Listar todo)
0- Obtener todos los filex con status=vigente
1- Armar una lista de objetos filex (JSON)
2- Armar respuesta HTTP con el JSON

POST /file/<id>/tech-measurement
0- Validar los inputs
1- Agregar un nuevo tech-measurement relacionado al id del path
2- Responder código HTTP

GET /file/<id>/tech-measurement
0- Buscar por id en tech-measurement
1- Armar un JSON
2- Responder JSON en respuesta HTTP

PUT /file/<id>
	Este endpoint implementa la edición pisando el objeto referenciado por <id>, pisando todos sus valores

DELETE /file/<id>
	Este endpoint implementa el borrado solo cambiando el atributo status=deleted



PUT /file/<id>/tech-measurement
POST /technician
GET /technician/<id>
DELETE /technician/<id>
GET /technician (Listar todo)