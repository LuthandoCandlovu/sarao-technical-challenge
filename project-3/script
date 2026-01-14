import string


def ispangram(str1, alphabet=string.ascii_lowercase):
    """
    Check whether a given string is a pangram.

    :param str1: Input string to check
    :param alphabet: Set of characters to check against (default: a-z)
    :return: True if pangram, False otherwise
    """
    # Convert string to lowercase and remove spaces
    cleaned = str1.lower().replace(" ", "")

    # Check if all alphabet characters are present in the string
    return set(alphabet).issubset(set(cleaned))


if __name__ == "__main__":
    # Test with a classic pangram
    print(ispangram("The quick brown fox jumps over the lazy dog"))
