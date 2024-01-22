Yet Another Powerset Package?
=============================

There appear to be an abundance of power set packages,
along with many code samples.
So it is fair to ask why I created this one.

I have not done an extensive review of the packages
I happened to see, but the ones that I did look at were seemed unsatisfactory.

I did not see other packages that produced a Generator.
Thus those packages will produce complete powersets that can be very large.
But by using using a generator, 

.. code-block:: python

    m = ps.generate_subsets([n for n in range(32)])

`m` does not consume many gigabytes of memory.

I also noticed that packages and proposed examples did not understand that both the empty set and the set itself are members of a power set.
Their behavior in that regard may be what users wanted, but it isn't what I wanted when I use the term "power set".

Nor did they deal consistently (or in documented fashion) regarding inputs.
Finally, they were typically defined specifically for lists instead of collections more broadly.

None of this may be sufficient reason in *your view* for me to create yet another powerset package, but it was suffient for *me*.


Wouldn't a gist be enough?
--------------------------

The actual function is just a few lines of very simple code,
so it may well be overkill to make an entire package for such a simple thing.
A GitHub Gist seems sufficient.
Indeed, that is how this started.
Three things tipped the balance for me to make this a package:

1. I wanted to include more documentation than would be appropriate for a docstring.

2. I wanted to include separate test files.

3. I wanted to create my first Python package, and doing so with some very simple code seemed like a way to start.


I also wanted to try my hand a creating a Python package.
Doing so around a very simple bit of code has its conveniences.
And while the very initial versions of this started
aa a GitHub gist, I wanted to add tests and more extensive documentation.
