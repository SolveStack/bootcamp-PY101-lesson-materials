best_hire_values = ['achievement', 'Adventure', 'Authenticity', 'Authority', 'Autonomy', 'balance', 'Beauty', 'Boldness', 'challenge', 'Citizenship', 'Community', 'Compassion', 'Competency', 'Contribution', 'Creativity', 'Curiosity', 'Debugging', 'Determination', 'Fairness', 'Faith', 'Fame', 'Friendships', 'Fun', 'Growth', 'Happiness', 'Honesty', 'Humor', 'Influence', 'Inner Harmony', 'Justice', 'Kindness', 'Knowledge', 'Leadership', 'Learning', 'Love', 'Loyalty', 'Meaningful Work', 'Openness', 'Optimism', 'Peace', 'Pleasure', 'Poise', 'Popularity', 'Problem-solving', 'Recognition', 'Religion', 'Reputation', 'Respect', 'Responsibility', 'Security', 'Self-Respect', 'Service',  'Stability', 'Status', 'Success', 'Trustworthiness', 'Wealth', 'Wisdom']




print(f"Starting length: {len(best_hire_values)}")
test_value = best_hire_values.remove("Faith")
best_hire_values.remove("Popularity")
best_hire_values.remove("Religion")
best_hire_values.remove("Wealth")
best_hire_values.remove("Status")
print(f"Ending length: {len(best_hire_values)}")

print(f"return value from .remove: {test_value} - it's None.")


# for value in best_hire_values:
#     print(value)

# print(f"Starting length: {len(best_hire_values)}")
# print("Last value:")
# print(best_hire_values[-1:])
# last_value = best_hire_values.pop()
# print(f"We got {last_value}!")
# print("Last value:")
# print(best_hire_values[-1:])
# print(f"Ending length: {len(best_hire_values)}")


# best_hire_values.append(last_value)
# print("Last value:")
# print(best_hire_values[-1:])
# print(f"Ending length: {len(best_hire_values)}")


# print(f"Starting length: {len(best_hire_values)}") 
# index = 2
# print(best_hire_values[2])
# popped_value = best_hire_values.pop(index)
# print(popped_value)
# print(f"Ending length: {len(best_hire_values)}")


print(best_hire_values)
junior_hire_values = best_hire_values.copy()

del junior_hire_values[6] # remove boldness
print(junior_hire_values)

# clear it all out
best_hire_values.clear()
print(best_hire_values)

del junior_hire_values

try:
    print(junior_hire_values)
except NameError:
    print(f"junior_hire_values is no longer a thing")
