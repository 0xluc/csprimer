# Validates card numbers using the luhn alg
def validate_credit_card(numbers: int):
    string_numbers = str(numbers)
    sum = 0
    for i in range(len(string_numbers), 0, -1):
        if i % 2 == 0:
            sum += int(string_numbers[i - 1])
        else:
            result = 2 * int(string_numbers[i - 1])
            if result > 9:
                result = result - 9
            sum += result
    if sum % 10 == 0:
        return True
    return False


print(validate_credit_card(5532445247038576))
