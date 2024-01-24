Usage
======

The package provides a single function, ``subsets(collection)``, which returns a Generator for the subsets of of ``collection``.

.. autofunction:: powerset_generator.subsets

Additional notes
----------------

The number of subsets of a collection with *N* unique elements is 2^N.
You can compute that with

.. code-block:: python

    import collections 

    int(2 ** len(collections.Counter(collection)))

You can work around the limitation that the members of the Collecton must be Hashable by using dictionary keys.
For example, if your collection is a dictionary, you can just generate the powerset of the keys of your dictionary.










