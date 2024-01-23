.. Powerset generator documentation master file, created by
   sphinx-quickstart on Sun Jan 21 21:13:16 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Powerset generator's documentation!
==============================================

**Powerset Generator** is a simply python package for creating power sets
of a collection.

.. code-block:: python

   from powerset_generator import powerset
   for e in powerset.subsets( ["one", "two", "three", "three"])]:
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

   1. The empty set, ``set()``, is included in the output;

   2. The full set ``{'one', 'two', 'three'}`` is included in the output;

   3. The duplicated input element ``"three"`` is treated as if it appeared only once;
   
   4. The order in which the subsets are generated is not defined.

     


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
