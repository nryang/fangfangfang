import re


def replace_all(str: str, substitutions: dict):
    """Replaces multiple substrings in a string.

    Keyword arguments:
    str -- the string to search and replace in
    substitutions -- a dictionary that contains mappings of the original
        substring to the replacement substring
    """
    if not substitutions:
        return str
    return re.sub('|'.join(re.escape(key) for key in substitutions.keys()),
                  lambda k: substitutions[k.group(0)], str)
