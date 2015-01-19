Beijing Python Meetup January 2015
==================================

.. contents::

This repository contains sample code and a slide deck from a presentation given on January 19th at the Beijing Python Meetup.

**View the slides** right here: https://gatherhealth.com/public/python-meetup-jan-2015.html

Any questions? Contact John (`jrdietrick <https://github.com/jrdietrick>`__ on GitHub) at j.r.dietrick@gmail.com.


``requirements.txt``
--------------------

Python libraries required to run this project, suitable for running with

::

    pip install -r requirements.txt


``slides``
----------

The slide presentation to accompany the talk, in RST source format. (Use `hieroglyph <https://github.com/nyergler/hieroglyph>`__ to compile.)


``code``
--------

A (very) simple Django project that was used for the live demos.

Below are some of the example commands that were run during the talk. You'll want to get in to a shell first::

    ./manage.py shell_plus


Examples - ``JSONFieldExample``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Store a JSON blob in the flexible column:

.. code-block:: python

    jfe = JSONFieldExample()
    jfe.flex_column = {'a': 1, 'b': [1, 3, 5.777]}
    jfe.save()

Fetch it back from the database, and your JSON has been fully serialized and deserialized, with no loss of type...

.. code-block:: python

    jfe2 = JSONFieldExample.objects.latest('created')
    print jfe2.flex_column['a']
    assert type(jfe2.flex_column['b'][2] == float)

Now let's try to query on a key within our column:

.. code-block:: python

    >>> JSONFieldExample.objects.filter(flex_column__contains='a')
    [<JSONFieldExample: JSONFieldExample object>]

Great! Looks like we have search functionality. But what if we do this?

.. code-block:: python

    >>> JSONFieldExample.objects.filter(flex_column__contains='5.777')
    [<JSONFieldExample: JSONFieldExample object>]

Oops! It looks like we're just doing a full-text search on the JSON string. Not ideal. Let's see the actual query:

.. code-block:: python

    >>> str(JSONFieldExample.objects.filter(flex_column__contains='5.777').query)
    'SELECT "flexcolumns_jsonfieldexample"."id", "flexcolumns_jsonfieldexample"."created", "flexcolumns_jsonfieldexample"."updated", "flexcolumns_jsonfieldexample"."recording_user", "flexcolumns_jsonfieldexample"."flex_column" FROM "flexcolumns_jsonfieldexample" WHERE "flexcolumns_jsonfieldexample"."flex_column"::text LIKE %5.777%'

Yep... just a regular ``LIKE``, nothing special. ORM support for special queries here is limited.


Examples - ``HStoreExample``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's try storing the same JSON blob:

.. code-block:: python

    hse = HStoreExample()
    hse.flex_column = {'a': 1, 'b': [1, 3, 5.777]}
    hse.save()

Great! It's saved. Right? Let's see what we get back when we query:

.. code-block:: python

    hse2 = HStoreExample.objects.latest('created')
    print hse2.flex_column['a']
    print hse2.flex_column['b'] # So far, so good...
    print type(hse2.flex_column['b']) # Says "string"... uh-oh!
    print hse2.flex_column['b'][2] # NOPE! Not what you were looking for.

OK, so we can't go more than one level deep. Anything below that gets serialized as a string.

On the bright side, we can do some cool queries:

.. code-block:: python

    # Find all records where "a" equals 1
    HStoreExample.objects.filter(flex_column__contains={'a': 1})

    # For comparison, try this...
    HStoreExample.objects.filter(flex_column__contains={'a': 2})

    # How about all records with a key "b"...
    HStoreExample.objects.filter(flex_column__contains=['b'])

You should already be able to see how this is more powerful than the JSON example above. For more examples, check out the `django-hstore docs <http://djangonauts.github.io/django-hstore/>`__.


Examples - ``HStoreSchemaExample``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Check out the schema defined in ``models.py``. It says that any value going in with key ``my_number`` is an int, and anything called ``my_float`` is a float.

Now we can do this:

.. code-block:: python

    hsse = HStoreSchemaExample()
    hsse.my_number = 999
    hsse.my_float = 3.5558
    hsse.save()

Let's query it back to prove it made the full round trip.

.. code-block:: python

    hsse2 = HStoreSchemaExample.objects.latest('created')
    assert type(hsse2.my_number) == int
    assert hsse2.my_number == 999
    assert type(hsse2.my_float) == float
    assert hsse2.my_float == 3.5558
    print hsse2.flex_column

Pretty cool! Is this the best of both worlds?
