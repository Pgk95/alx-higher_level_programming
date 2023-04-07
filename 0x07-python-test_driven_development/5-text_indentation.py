#!/usr/bin/python3
def text_indentation(text):
    """
    Prints the text with 2 new lines after each '.', '?' and ':' character.

    Args:
        text (str): The text to be indented.

    Raises:
        TypeError: If the input text is not a string.

    Returns:
        None.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Remove spaces at the beginning and end of the text
    text = text.strip()

    # Initialize the result string
    result = ""

    # Iterate through each character in the text
    for i in range(len(text)):
        # Append the current character to the result string
        result += text[i]

        # If the current character is a '.', '?' or ':', add two new lines to the result string
        if text[i] in ('.', '?', ':'):
            result += '\n\n'

    # Print the indented text
    print(result)
