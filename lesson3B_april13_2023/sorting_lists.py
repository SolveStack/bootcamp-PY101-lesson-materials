best_hire_values = ['Authenticity', 'Achievement', 'Adventure', 'Authority', 'Autonomy', 'Balance', 'Beauty', 'Boldness', 'Compassion', 'Challenge', 'Citizenship', 'Community', 'Competency', 'Contribution', 'Creativity', 'Curiosity', 'Determination', 'Fairness', 'Faith', 'Fame', 'Friendships', 'Fun', 'Growth', 'Happiness', 'Honesty', 'Humor', 'Influence', 'Inner Harmony', 'Justice', 'Kindness', 'Knowledge', 'Leadership', 'Learning', 'Love', 'Loyalty', 'Meaningful Work', 'Openness', 'Optimism', 'Peace', 'Pleasure', 'Poise', 'Popularity', 'Recognition', 'Reputation', 'Respect', 'Responsibility', 'Security', 'Self-Respect', 'Service', 'Spirituality', 'Stability', 'Success', 'Status', 'Trustworthiness', 'Wealth', 'Wisdom', 'Perseverence', 'Patience', 'Debugging', 'Problem-solving', 'Debugging', 'Problem-solving']
best_hire_values.sort()
print(best_hire_values)

best_hire_values.sort(reverse=True)
print(best_hire_values) 


numbers = [100, 50, 65, 82, 23]
numbers.sort(reverse=True)
print(numbers)


foo = 'Foo'.lower()
print(foo)

best_hire_values = ['Adventure', 'Authenticity', 'Authority', 'Autonomy', 'balance', 'Beauty', 'Boldness', 'challenge', 'Citizenship', 'achievement', 'Community', 'Compassion', 'Competency', 'Contribution', 'Creativity', 'Curiosity', 'Debugging', 'Determination', 'Fairness', 'Faith', 'Fame', 'Friendships', 'Fun', 'Growth', 'Happiness', 'Honesty', 'Humor', 'Influence', 'Inner Harmony', 'Justice', 'Kindness', 'Knowledge', 'Leadership', 'Learning', 'Love', 'Loyalty', 'Meaningful Work', 'Openness', 'Optimism', 'Peace', 'Pleasure', 'Poise', 'Popularity', 'Problem-solving', 'Recognition', 'Religion', 'Reputation', 'Respect', 'Responsibility', 'Security', 'Self-Respect', 'Service',  'Stability', 'Status', 'Success', 'Trustworthiness', 'Wealth', 'Wisdom']
best_hire_values.sort(key = str.lower)
print(best_hire_values)


# this does NOT copy, these are the same list!!!
numbers = [3, -8, 51, 63, -29]
integers = numbers

numbers.append(5)

print(numbers)
print(integers)

print(id(numbers))
print(id(integers))


numbers = [3, -8, 51, 63, -29]
integers = list(numbers)
integers.append(5)

print(id(numbers))
print(id(integers))

print(numbers)
print(integers)


numbers = [3, -8, 51, 63, -29]
integers = numbers.copy()
integers.append(5)

print(id(numbers))
print(id(integers))

print(numbers)
print(integers) 