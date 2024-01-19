# Python Power set generator

```python
import powerset_generator.powerset as ps

for e in ps.powerset(["one", "two", "three"]):
    print(e)
```

produces

```txt
set()
{'one'}
{'three'}
{'two'}
{'one', 'three'}
{'one', 'two'}
{'three', 'two'}
{'one', 'three', 'two'}
```

## Yet another power set package

There appear to be an abundance of power set packages,
along with many code samples.
So it is fair to ask why I created this one.
I have not done an extensive review of them,
but the ones that I did look at were seemed unsatisfactory.

First, I wanted something that is a Generator to allow
for larger sets without consuming horrific amounts of memory.

In

```python
 m = ps.powerset([n for n in range(32)])
```

`m` does not consume many Gigabytes of memory

Secondly, I wanted type clarity and breadth.
Many of the examples that I saw were specific to lists,
and all lacked type annotations.

Finally, I wanted to try my hand a creating a Python package.
Doing so around a very simple bit of code has its conveniences.
