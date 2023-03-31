personal_values = ["Authenticity", "Achievement", "Adventure", "Authority", "Autonomy", "Balance", "Beauty", "Boldness", "Compassion", "Challenge", "Citizenship", "Community", "Competency", "Contribution", "Creativity", "Curiosity", "Determination", "Fairness", "Faith", "Fame", "Friendships", "Fun", "Growth", "Happiness", "Honesty", "Humor", "Influence", "Inner Harmony", "Justice", "Kindness", "Knowledge", "Leadership", "Learning", "Love", "Loyalty", "Meaningful Work", "Openness", "Optimism", "Peace", "Pleasure", "Poise", "Popularity", "Recognition", "Religion", "Reputation", "Respect", "Responsibility", "Security", "Self-Respect", "Service", "Spirituality", "Stability", "Success", "Status", "Trustworthiness", "Wealth", "Wisdom"]
length = len(personal_values)
print("Printing the last value:")
print("Way 1: personal_values[length - 1]")
print(personal_values[length - 1])
print("Way 2: personal_values[-1]")
print(personal_values[-1])

if personal_values[length - 1] == personal_values[-1]:
    print("Both ways work!")

# personal_values[5:8]
# returns 3 values x
print(personal_values[5:8])

print(personal_values[:8])

print("are these 2 the same place in memory?")
print(id(personal_values))
print(id(personal_values[:]))

print(len(personal_values))
print(len(personal_values[:]))



# try:
#     print(personal_values[length])
# except IndexError as ie:
#     print("Pick a different index!")