import requests

# input("Please enter healthcare title")
# title_input = input('')

# # Define the API endpoint (for example, getting the glossary content)
# url = 'https://www.healthcare.gov/api/glossary.json'

# # Send an HTTP GET request to the API
# response = requests.get(url)

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Parse the JSON response
#     data = response.json()
    
#     # Print the data (or process it further as needed)
#     print("Glossary content retrieved successfully:")
#     for entry in data['glossary']:
#         print(f"Title: {entry[str(title_input)]}")
#         print(f"Content: {entry['content']}")
#         # titles = []
#         # titles.append(entry['title'])
#         # print(titles)
#         # print(f"Title: {entry['title']}")
#         # print(f"Content: {entry['content']}")
#         # print(f"URL: {entry['url']}")
#         # print("-" * 50)
# else:
#     print(f"Failed to retrieve data. Status code: {response.status_code}")



# Prompt the user for a healthcare title
title_input = input('Please enter healthcare title: ')

# Define the API endpoint (for example, getting the glossary content)
url = 'https://www.healthcare.gov/api/glossary.json'

# Send an HTTP GET request to the API
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Flag to check if the title is found
    found = False

    # Print the data (or process it further as needed)
    print("Glossary content retrieved successfully:")
    for entry in data['glossary']:
        # Compare the user input with the title in the data
        if entry['title'].lower() == title_input.lower():
            print(f"Title: {entry['title']}")
            print(f"Content: {entry['content']}")
            print(f"URL: {entry['url']}")
            print("-" * 50)
            found = True
            break  # Stop once we've found the match
    
    if not found:
        print(f"No glossary entry found for the title: {title_input}")

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")