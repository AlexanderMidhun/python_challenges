import re

def main():
    pattern = "python"

    if re.match(pattern,"python is a high-level, interpreted programming language known for its simplicity and readability."):
        print("matched")
    else:
        print("not matched")

    if re.search(pattern,"Hello, this is python"):
        print("matched")
    else:
        print("not matched")

    print(re.findall(pattern,"This is python , hi python , python python"))

    pattern = r'inmakes'
    text = "hai inmakes, hello India"

    new = re.sub(pattern, "python", text)
    print(new)

    dot = "p.th.n"
    if re.match(dot,"python"):
        print("matched")
    else:
        print("not matched")

    character_class = r"[aeiou]"

    text = "Hello, This is python"

    matches = re.findall(character_class, text)
    print("Matches:", matches)


if __name__ == '__main__':
    main()
