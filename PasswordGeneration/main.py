import random
import string

upper_chars = string.ascii_uppercase
lower_chars = string.ascii_lowercase
digit_chars = string.digits
symbol_chars = string.punctuation

random_upper_chars = "".join(random.sample(upper_chars, 4))
random_lower_chars = "".join(random.sample(lower_chars, 4))
random_digit_chars = "".join(random.sample(digit_chars, 4))
random_symbol_chars = "".join(random.sample(symbol_chars, 4))


pass_string = (
    random_upper_chars + random_digit_chars + random_lower_chars + random_symbol_chars
)

pass_string = "".join(random.sample(pass_string, len(pass_string)))
print(pass_string)
