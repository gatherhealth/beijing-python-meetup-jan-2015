==========================
Python Meetup January 2015
==========================

.. rst-class:: build

    * A week late this month, which means...
    * Only three weeks til the next meetup! (Feb 9)
    * Interested in giving a quick talk? Let Chris or John know!


.. slide:: Flexible Schema Columns in Django
    :level: 1


.. slide:: Normally, your database might look something like this...
    :level: 2

    .. rst-class:: build

        .. figure:: images/figure0.png

        **What if I told you...**

        * Sony TV has a resolution of 1920x1080
        * Kitchen-Aid blender has a max speed of 5000rpm


.. slide:: Option 1: Go wide...
    :level: 2

    .. rst-class:: build

        .. figure:: images/figure4.png

    .. note::

        * easy at first, you get an obj.max_rpm
        * eventually your table gets really, really wide
        * lots of fields on model
        * schema migrations often


.. slide:: Option 2: Join tables!
    :level: 2

    .. rst-class:: build

        .. figure:: images/figure1a.png

        .. figure:: images/figure1b.png


.. slide:: Option 3: NoSQL
    :level: 2

    .. rst-class:: build

        .. code-block:: json

            [
                {
                    "product_sku": "ZBAA762",
                    "price": 59.99,
                    "name": "Kitchen-Aid blender",
                    "specs": {
                        "Maximum RPM": 5000
                    }
                },
                {
                    "product_sku": "HUF8214",
                    "price": 1099.99,
                    "name": "SONY 72\" plasma TV",
                    "specs": {
                        "Horizontal resolution": 1920,
                        "Vertical resolution": 1080
                    }
                }
            ]


.. slide:: Option 4: Flex your schema
    :level: 2

    .. rst-class:: build

        .. figure:: images/figure3.png


.. slide:: Today's Options
    :level: 1

    * Framework (Django or an add-on)
    * Database (PostgreSQL or something else)


.. slide:: At the database level
    :level: 2

    * Any database can use JSON (e.g., with a "text" or "VARCHAR" field)
    * Postgres (at least 9.2+) support:
        * **json** ``{"a": 1, "b": {"x": "y"}}``
        * **HStore** ``"a"=>"1","b"=>"2"``


.. slide:: ``django-jsonfield``
    :level: 2

    https://github.com/bradjasper/django-jsonfield

    **Pros**

    * Handles serialization for you
    * Compatible across databases (SQLite, MySQL, etc.)

    **Cons**

    * `Doesn't take advantage of PostgreSQL json field type <https://github.com/bradjasper/django-jsonfield/issues/57>`__
        * Text indexing only!
    * ORM facilities limited

    ** ** ** **

    **Similar alternative**: `unchained <https://github.com/aychedee/unchained>`__


.. slide:: ``django-jsonfield``
    :level: 1

    (live demo)


.. slide:: ``django-hstore``
    :level: 2

    https://github.com/djangonauts/django-hstore

    **Pros**

    * `Richer ORM query language <http://djangonauts.github.io/django-hstore/#_python_api>`__
    * HStore supports indexing in PostgreSQL 9.3+

    **Cons**

    * PostgreSQL only
    * No nested dictionaries
    * Everything is a string! Unless you use `schema mode <http://djangonauts.github.io/django-hstore/#_model_setup>`__


.. slide:: ``django-hstore``
    :level: 1

    (live demo)


.. slide:: On the horizon
    :level: 2

    **json in PostgreSQL**

    * ``jsonb`` datatype with indexing in Postgres 9.4+

    ** ** ** **


    **HStore**

    * `Further improvements coming in Django 1.8 <https://docs.djangoproject.com/en/dev/releases/1.8/>`__


.. slide:: Thanks!
    :level: 2

    **I'd like to thank...**

    * Gather engineering team
    * Rocky Meza (https://github.com/rockymeza)

    ** ** ** **

    **This presentation powered by:**

    * Django 1.7.3, with:
        * django-hstore 1.3.5
        * django-jsonfield 0.9.13
        * unchained 1.1
    * PostgreSQL 9.3.5
    * hieroglyph + reStructuredText


.. slide:: Questions?
    :level: 2

    .. figure:: images/qrcode_sm.png

    P.S....
        * Find this whole presentation online at https://github.com/gatherhealth
        * We're hiring! Check out https://gatherhealth.com/careers


.. slide:: Appendix
    :level: 1


.. slide:: Another schema option...
    :level: 2

    .. rst-class:: build

        .. figure:: images/figure2.png
