# Python Power set generator

```python

import powerset.powerset

a_list: list[str] = ["one", "two", "three"]
        for element in powerset(s):
            print(element)
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
