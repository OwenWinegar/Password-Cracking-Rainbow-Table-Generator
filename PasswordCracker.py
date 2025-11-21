from itertools import combinations
import hashlib
import re
import unicodedata

unique_words = set()
sorted_words = set()

bob_hash = "7b0ca5c95a9398a2f32613d987428180"
dr_pearson_hash = "7e985df169d043112b23508a81e16538"

# Bob password requirements:
    # 5-10 characters in length (inclusive)
    # alphanumeric characters only, no symbols!

# Dr. Pearson password requirements:
    # 12-18 characters in length (inclusive)
    # alphanumeric characters only, no symbols!
    # at least one letter and at least one number
    # at least one uppercase letter and at least one lowercase letter

def process_file(file_path: str, finder: bool):
    global sorted_words
    with open(file_path, "r") as file:
        for line in file:
            # this splits at both : and ,
            words = re.split(r'[:,\s]+', line.strip())
            for word in words:
                if finder:
                    clean = word.lower()
                    unique_words.add(clean)
                else:
                    unique_words.add(word)
    sorted_words = sorted(unique_words)

def md5_hash(text: str):
    return hashlib.md5(text.encode("utf-8")).hexdigest()

def isnum(character: str) -> bool:
    if 48 <= ord(character) <= 57:
        return True
    else:
        return False


process_file("/Users/owenwinegar/PycharmProjects/Project 2 - Password Cracking/.venv/bob.txt", True)
# process_file( "/Users/owenwinegar/PycharmProjects/Project 2 - Password Cracking/.venv/dr_pearson.txt", False)

def hash_finderB(target_hash: str) -> str:
    num_attempts = 0

    for i in range(1, 7):
        for combo in combinations(unique_words, i):

            combo_text = ''.join(combo)

            no_symbol = not any(unicodedata.category(n).startswith('S') for n in combo_text)

            if not (5 <= len(combo_text) <= 10 and no_symbol):
                continue

            num_attempts += 1
            print(f"trying... text {num_attempts}, {combo_text}")

            hash_val = md5_hash(combo_text)

            with open('bobs_rainbow_table.txt', 'a') as file:
                file.write(f"trying... {combo_text}, {hash_val}\n")

            if hash_val == target_hash:
                return combo_text
    return "nothing found"


def hash_finderD(target_hash: str) -> str:
    num_attempts = 0
    for i in range(1, 7):
        for combo in combinations(unique_words, i):

            combo_text = ''.join(combo)

            if not (12 <= len(combo_text) <= 18):
                continue

            has_digit = any(isnum(n) for n in combo_text)
            has_upper = any(n.isupper() for n in combo_text)
            no_symbol = not any(unicodedata.category(n).startswith('S') for n in combo_text)

            if not (has_digit and has_upper and no_symbol):
                continue

            num_attempts += 1
            print(f"trying... text {num_attempts}, {combo_text}")

            hash_val = md5_hash(combo_text)

            with open('dr_pearsons_rainbow_table.txt', 'a') as file:
                file.write(f"trying... {combo_text}, {hash_val}\n")

            if hash_val == target_hash:
                return combo_text

    return "nothing found"

hash_finderB(bob_hash)
# hash_finderD(dr_pearson_hash)