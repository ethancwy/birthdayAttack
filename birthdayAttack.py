import hashlib


def calculate_hash(file_path):
    with open(file_path, "rb") as file:
        file_content = file.read()
    sha256_hash = hashlib.sha256(file_content).hexdigest()
    return sha256_hash


# Appends newlines to confession_fake.txt until the last {digit_count} digits are the same as in confession_real.txt
def match(fake_path, real_path, digit_count):
    real_hash = calculate_hash(real_path)
    fake_hash = ""
    newline_count = 0
    while fake_hash[-digit_count:] != real_hash[-digit_count:]:
        with open(fake_path, "a") as fake_file:
            fake_file.write("\n")
            newline_count += 1
            fake_hash = calculate_hash(fake_path)

    print(f"\nMATCH {digit_count} LAST DIGITS:\n")
    print(f"Updated Fake: {fake_hash}")
    print(f"Real: {real_hash}")
    print(f"Newlines appended count: {newline_count}")


fake_path = "confession_fake_copy.txt"
real_path = "confession_real.txt"


match(fake_path, real_path, 2)
match(fake_path, real_path, 3)
match(fake_path, real_path, 4)
# match(fake_path, real_path, 5)
# match(fake_path, real_path, 6)

# restore to original state
original_fake_path = "confession_fake.txt"

with open(original_fake_path, "r") as original_fake_file:
    original_content = original_fake_file.read()

with open(fake_path, "w") as fake_file:
    fake_file.write(original_content)
