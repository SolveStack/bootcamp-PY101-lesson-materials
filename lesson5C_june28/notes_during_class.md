
Your local repository at the end of class should look like this:

![Final Local Repository](local_repository.png "final local repository")

## `__init__.py`
Blank file with no text in it.


## `main.py`

contents:

```python
from models import Car

if __name__ == "__main__":
    my_car = Car("Jeep", "Wrangler", 2015)
    print(my_car)
    # TODO:
    # 1. instruct user to enter vehicle information
    # 2. Take in make, model, year, if a tow is required
    # 3. Choose an employee to assign to the vehicle
    # 4. Add symptoms to the vehicle based on customer's description
    #    for the technician's understanding
```