def is_big_number(num: int) -> bool:
    return num > 100

def is_middling_number(num: int) -> bool:
    return num > 50 and num < 2000

def is_both(num: int) -> bool:
    return is_big_number(num) and is_middling_number(num)

def start_with_a(word: str) -> str:
    if (word[0].lower() == "a"):
        return "Yeah"
    else:
        return "Nah"

def some_other(num: int, word: str) -> int:
    if is_big_number(num) or start_with_a(word) == "Yeah":
        return 10
    else:
        return 5