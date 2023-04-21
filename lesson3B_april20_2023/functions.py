def add_numbers(number_1: int, number_2: int):
  print(f"{number_1} + {number_2} = {number_1 + number_2}")

def sum(number_1: int, number_2: int) -> int:
  print(f"{number_1} + {number_2} = {number_1 + number_2}")
  return number_1 + number_2

def get_full_name(first_name: str, last_name: str) -> str:
  return f"{first_name} {last_name}"

# print("This is the arguments given in the wrong positions:")
# print(get_full_name("Tomboulian", "Ana"))

# # using the keyword argument style
# print(get_full_name(last_name="Tomboulian", first_name="Ana"))


# sum = add_numbers(500, 750)
# print(sum)

# add_numbers(100)

# add_numbers(500, 'foo') # typeerror
# add_numbers('bar', 'foo')


# def get_favorite_color(name_of_color: str) -> str:
#   return f"My favorite color is {name_of_color}"

# color_str = get_favorite_color("blue")
# print(color_str)


def favorite_color(name_of_color: str = 'blue') -> str:
  return f"My favorite color is {name_of_color}"


# first lets provide the argument
print(favorite_color("red"))


# then lets try without providing an argument
print(favorite_color())
