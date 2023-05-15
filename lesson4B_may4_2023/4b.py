this_is_my_tuple = ("first", "second", "third", "fourth",) 
print(f"this object type is {type(this_is_my_tuple)} with value of {this_is_my_tuple}")

mixed_tuple = ("Sunshine", "Daisies", True, False, 0, 1, None)
print(f"If you see this message, what I just told you about mixed types is the truth: {mixed_tuple}")

lonely_tuple = ("forever alone",)
print(f"This is a lonely {type(lonely_tuple)}")

lonely_unknown_type = ("what even am I?" + " I'm not sure") + "and done!"
print(f"This is a lonely {type(lonely_unknown_type)}")  


print("Second:")
print(this_is_my_tuple[1])

# slicing a range of elements within a tuple
# first two (from 0 to 2 but not including 2)
print(this_is_my_tuple[0:2])


print(this_is_my_tuple[-1])

# will not run (TypeError)
# mixed_tuple[0] = "Cloudy"

mixed_tuple = ("Sunshine", "Daisies", True, False, 0, 1, None)

# if you really must make changes

# first change the tuple to a list using the previously mentioned
# list constructor
mixed_tuple_as_list = list(mixed_tuple)

# now that we have a list, we can do the normal shennanigans to 
# make whatever changes we want
# in this case, let's delete the last 4 values
del mixed_tuple_as_list[-5:]

# now let's change this back to a tuple
# using, you guessed it, the tuple constructor
mixed_tuple = tuple(mixed_tuple_as_list)
print(mixed_tuple)


tuple_to_convert_to_dictionary = (("foo", "bar"), ("status", "active"))
print(dict(tuple_to_convert_to_dictionary))

print(set(mixed_tuple))


# colors = ("cardinal red", "army green", "cornflower-blue")

# red_string, green_string, blue_string = colors

# print(red_string)
# print(green_string)
# print(blue_string)


colors = ("cardinal red", "army green", "cornflower-blue", "pumpkin spice")

red_string, green_string, *_ = colors

# print(red_string)
# print(green_string)
# arbitrary variable name of "_" - you can technically use it but don't
print(_)

# colors = ("cardinal red", "army green", "cornflower-blue", "pumpkin spice")

# (red, green, *rest_of_colors) = colors
# print(red)
# print(green)
# print(tuple(rest_of_colors))

dog_breeds = ("chihuahua", "boston terrier", "mastiff", "dachshund", "pekingese")

for breed in dog_breeds:
    print(f"I want a {breed} for a pet")

for i in range(len(dog_breeds)):
    print(dog_breeds[i])

tuple1 = (1, 2, 3, 4, 5)
