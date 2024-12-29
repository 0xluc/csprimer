# Validates credit card numbers using the luhn alg
def validate_credit_card(numbers: int):
    string_numbers = str(numbers)
    sum = 0
    for i, n in enumerate(reversed(string_numbers)):
        if i % 2 == 0:
            sum += int(n)
        else:
            result = 2 * int(n)
            if result > 9:
                result = result - 9
            sum += result
    if sum % 10 == 0:
        return True
    return False


if __name__ == "__main__":
    assert validate_credit_card(5532445247038576)
    print("OK")
