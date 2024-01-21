# Python Power set generator

```python
import powerset_generator.powerset as ps

for e in ps.generate_subsets(["one", "two", "three", "three"]):
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

Note that the empty set, `set()` is included in the output
and that the function treats the duplicated input element `"three"` as if it appeared only once.
This is correct behavior the mathematical notion of power set.

The code for the `powerset()` function is derived heavily from
[Allen Downey](https://stackoverflow.com/users/661626/allen-downey)'s
[Stack Overflow answer](https://stackoverflow.com/a/53726866/1304076).

## Yet another power set package?

There appear to be an abundance of power set packages,
along with many code samples.
So it is fair to ask why I created this one.
I have not done an extensive review of the packages
I happened to see, but the ones that I did look at were seemed unsatisfactory.

First, I wanted something that is a Generator to allow
for larger sets without consuming horrific amounts of memory.

In

```python
 m = ps.generate_subsets([n for n in range(32)])
```

`m` does not consume many gigabytes of memory.

Secondly, I wanted type clarity and breadth.
Many of the examples that I saw were specific to lists,
and all lacked type annotations.

I also wanted to try my hand a creating a Python package.
Doing so around a very simple bit of code has its conveniences.
And while the very initial versions of this started
aa a GitHub gist, I wanted to add tests and more extensive documentation.
