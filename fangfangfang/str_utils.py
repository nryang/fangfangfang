import re


def replace_all(str, substitutions):
    if not substitutions:
        return str
    return re.sub('|'.join(re.escape(key) for key in substitutions.keys()),
                  lambda k: substitutions[k.group(0)], str)
