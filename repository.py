def save(service, username, password):
    """Save data to text file."""

    entry_line = f"{service} | {username} | {password}\n"
    with open("data/passwds.txt", "a") as file:
        file.write(entry_line)