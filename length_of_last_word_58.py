def lastWordBlane(s: str):
    sList = s.strip().split(" ")
    return len(sList[-1])


def last_word_len(s):
    ls = s.split()
    return len(ls[-1])


if __name__ == "__main__":
    # Case 1

    print(last_word_len("Hello World"))
    print(lastWordBlane("Hello World"))
    print()

    # Case 2
    print(last_word_len("   fly me   to   the moon  "))
    print(lastWordBlane("   fly me   to   the moon  "))
    print()

    # Case 3
    print(last_word_len("luffy is still joyboy"))
    print(lastWordBlane("luffy is still joyboy"))
    print()
