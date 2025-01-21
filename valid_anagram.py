def isAnagram(s: str, t: str) -> bool:
    return sorted(list(s)) == sorted(list(t))


if __name__ == "__main__":
    print(isAnagram("rac", "car"))
    print(["car"])
