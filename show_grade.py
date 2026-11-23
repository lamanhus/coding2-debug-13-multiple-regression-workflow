"""Display your Homework 2 mark: uv run python show_grade.py."""

from hashlib import sha256

SALT = "70e71c190bfdb88d2a4dd9fd29d0ce2e"
GRADE_HASH = "ff7a1ee5d3f4d08c0499c2bfc5e68acca17bb59b9b886d51f0be20762a2269fa"

# Match the stored hash against each possible whole-number mark.
for mark in range(101):
    candidate = sha256(f"{SALT}:{mark}".encode("utf-8")).hexdigest()
    if candidate == GRADE_HASH:
        print(f"Homework 2: {mark}/100")
        break
else:
    raise RuntimeError("The mark could not be verified. Please contact the instructor.")
