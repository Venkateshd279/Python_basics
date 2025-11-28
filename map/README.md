# MAP Function 
The `map()` function applies a given function to **every item** in a `list` (or any iterable) and returns a new result.
**Do this action to every item in the list.**

### Syntax
```hcl 
    map(function, iterable)
```

## Examples:
```hcl 
    numbers = [1, 2, 3, 4]

    # Double every number in the list
    doubled = map(lambda x: x * 2, numbers)

    print(list(doubled))  # Output: [2, 4, 6, 8]
```

