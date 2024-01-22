.. Powerset generator documentation master file, created by
   sphinx-quickstart on Sun Jan 21 21:13:16 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Powerset generator's documentation!
==============================================

**Powerset Generator** is a simply python package for creating power sets
of a collection.

.. code-block:: python

   import powerset_generator.powerset as ps
   for e in ps.generate_subsets( ["one", "two", "three", "three"])]:
      print(e)

should produce a result *similar to*

.. code-block:: python

   set()
   {'one'}
   {'three'}
   {'two'}
   {'one', 'three'}
   {'one', 'two'}
   {'three', 'two'}
   {'one', 'three', 'two'}

.. note::

   Note that the empty set, ``set()`` is included in the output;
   the function treats the duplicated input element `"three"` as if it appeared only once;
   and that the order of the elements of the results may vary.

     


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   usage
   yapp
   credits



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
