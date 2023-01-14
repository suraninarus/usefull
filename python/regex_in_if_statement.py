from re import match

import re

# regex = r"\s*Proof.\s*"
# contents = ['Proof.\n', '\nProof.\n']
# for content in contents:
#     assert re.match(regex, content), f'Failed on {content=} with {regex=}'
#     if re.match(regex, content):
#         print(content)


## ======================7

regex = r"^\d.*"
contents = ['Proof.\n', '\nProof.\n']
for content in contents:
    assert re.match(regex, content), f'Failed on {content=} with {regex=}'
    if re.match(regex, content):
        print(content)
