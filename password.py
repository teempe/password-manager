import string
import random


def generate_password(n_letters=None, n_symbols=None, n_digits=None):
    """
    Generates random password.
    Function takes required numbers of letters, symbols and digits and generates random passowrd.
    If any of arguments is missing, it will be generated randomly.
    
    Paramaters:
        n_letters (int): Required number of letters
        n_digits (int): Required number of digits
        n_symbols (int): Required number od symbols

    Returns:
        str: Generated password
    """

    n_letters = random.randint(8, 10) if n_letters is None else n_letters
    n_symbols = random.randint(2, 4) if n_symbols is None else n_symbols
    n_digits = random.randint(2, 4) if n_digits is None else n_digits

    symbols=["!", "#", "$", "%", "&", "(", ")", "*", "+"]
    password = []
    # selecting letters
    password.extend([random.choice(string.ascii_letters) for _ in range(n_letters)])
    # selecting symbols
    password.extend([random.choice(symbols) for _ in range(n_symbols)])
    # selecting digits
    password.extend([random.choice(string.digits) for _ in range(n_digits)])
    random.shuffle(password)
    
    return "".join(password)


if __name__ == "__main__":
    print(generate_password())
