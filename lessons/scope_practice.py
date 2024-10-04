def remove_chars(msg: str, char: str) -> str:
    """Returns a copy of msg with all instances of char removed"""
    copy: str = ""
    index: int = 0
    while index < len(msg):
        if char != msg[index]:
            copy += msg[index]
        index += 1
    return copy


print(remove_chars("football", "o"))
