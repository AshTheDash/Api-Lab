"""
API LAB: Calling Real Data from the Internet

GOAL:
Learn how to use an API to get real data from the internet using Python.

An API is just a URL that returns DATA instead of a webpage.
"""

# STEP 1: Choose an API
# I chose the Cat Facts API from the approved list:
# https://catfact.ninja/fact

import requests




url = "https://catfact.ninja/fact"


response = requests.get(url)


data = response.json()

print("FULL DATA RETURNED BY API:")
print(data)
print("-----------------------------------")



cat_fact = data["fact"]   # <- extracting one value
print("EXTRACTED FACT:")
print(cat_fact)
print("-----------------------------------")

# STEP 4: Do something with the data

# Print it in a sentence
print(f"Here is a random cat fact: {cat_fact}")
