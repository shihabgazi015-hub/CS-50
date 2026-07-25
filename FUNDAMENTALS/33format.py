# name = input("Enter your name: ").strip()
# if ', ' in name:
#     last_name, first_name = name.split(', ', 1)
#     formatted_name = f"{first_name} {last_name}"
# else:
#     formatted_name = name
# # print(f"Hello, {formatted_name}!")

# import re
# name = input("Enter your name: ").strip()
# match = re.match(r'^(.*), (.*)$', name)
# if match:
#     formatted_name = f"{match.group(2)} {match.group(1)}"
#     # last_name, first_name = match.groups()
#     # formatted_name = f"{first_name} {last_name}"
# else:    
#     formatted_name = name
# print(f"Hello, {formatted_name}!")

import re
name = input("Enter your name: ").strip()
if matches := re.match(r'^(.*), (.*)$', name):
    formatted_name = f"{matches.group(2)} {matches.group(1)}"
else:    
    formatted_name = name
print(f"Hello, {formatted_name}!")# print(f"Hello, {formatted_name}!")