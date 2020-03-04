# Text Wrap

import textwrap

def wrap(string, max_width):
    text_wrapped = textwrap.wrap(string, max_width)

    result = ""
    for i in text_wrapped:
        result = result + i + "\n"

    return result

print(wrap(input(), int(input())))


