personal_values = ["Authenticity", "Achievement", "Adventure", "Authority", "Autonomy", "Balance", "Beauty", "Boldness", "Compassion", "Challenge", "Citizenship", "Community", "Competency", "Contribution", "Creativity", "Curiosity", "Determination", "Fairness", "Faith", "Fame", "Friendships", "Fun", "Growth", "Happiness", "Honesty", "Humor", "Influence", "Inner Harmony", "Justice", "Kindness", "Knowledge", "Leadership", "Learning", "Love", "Loyalty", "Meaningful Work", "Openness", "Optimism", "Peace", "Pleasure", "Poise", "Popularity", "Recognition", "Reputation", "Respect", "Responsibility", "Security", "Self-Respect", "Service", "Spirituality", "Stability", "Success", "Status", "Trustworthiness", "Wealth", "Wisdom"]
print(f"Starting length: {len(personal_values)}")

personal_values.insert(2, "Perseverence")
personal_values.insert(2, "Patience")
print(personal_values)
print(f"Ending length: {len(personal_values)}")

personal_values = ["Authenticity", "Achievement", "Adventure", "Authority", "Autonomy", "Balance", "Beauty", "Boldness", "Compassion", "Challenge", "Citizenship", "Community", "Competency", "Contribution", "Creativity", "Curiosity", "Determination", "Fairness", "Faith", "Fame", "Friendships", "Fun", "Growth", "Happiness", "Honesty", "Humor", "Influence", "Inner Harmony", "Justice", "Kindness", "Knowledge", "Leadership", "Learning", "Love", "Loyalty", "Meaningful Work", "Openness", "Optimism", "Peace", "Pleasure", "Poise", "Popularity", "Recognition", "Reputation", "Respect", "Responsibility", "Security", "Self-Respect", "Service", "Spirituality", "Stability", "Success", "Status", "Trustworthiness", "Wealth", "Wisdom"]
print(f"Starting length: {len(personal_values)}")

personal_values.append("Perseverence")
personal_values.append("Patience")
print(personal_values)
print(personal_values[-2:])
print(f"Ending length: {len(personal_values)}")


personal_values = ["Authenticity", "Achievement", "Adventure", "Authority", "Autonomy", "Balance", "Beauty", "Boldness", "Compassion", "Challenge", "Citizenship", "Community", "Competency", "Contribution", "Creativity", "Curiosity", "Determination", "Fairness", "Faith", "Fame", "Friendships", "Fun", "Growth", "Happiness", "Honesty", "Humor", "Influence", "Inner Harmony", "Justice", "Kindness", "Knowledge", "Leadership", "Learning", "Love", "Loyalty", "Meaningful Work", "Openness", "Optimism", "Peace", "Pleasure", "Poise", "Popularity", "Recognition", "Reputation", "Respect", "Responsibility", "Security", "Self-Respect", "Service", "Spirituality", "Stability", "Success", "Status", "Trustworthiness", "Wealth", "Wisdom"]
print(f"Starting length: {len(personal_values)}")

software_development_values = ["Perseverence", "Patience"]
personal_values.extend(software_development_values)
print(personal_values[-2:])

skills = ("Debugging", "Problem-solving")
personal_values.extend(skills)
best_hire_values = personal_values
print(best_hire_values[-2:])
print(f"Look, it's a list! {type(best_hire_values)}")