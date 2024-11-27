import string
from collections import Counter


decrypt_map = {
    'M': 'I',
    'N': 'M',
    'P': 'A',
    'A': 'S',
    'R': 'E',
    'E': 'N',
    'U': 'O',
    'I': 'R',
    'W': 'T',
    'L': 'C',
    'Z': 'H',
    'G': 'V',
    'J': 'Z',
    'O': 'G',
    'Y': 'F',
    'F': 'U',
    'X': 'D',
    'Q': 'P',
    'D': 'L',
    'S': 'W',
    'B': 'Y',
    'V': 'K',
    'K': 'B',
}



import string
from collections import Counter


def analyze_frequencies(text):
    """Analyze letter frequencies in the text"""
    # Remove non-letters and convert to uppercase
    clean_text = "".join(c.upper() for c in text if c.isalpha())

    # Count frequencies
    freq = Counter(clean_text)
    total = sum(freq.values())

    # Calculate percentages and sort by frequency
    freq_percent = {k: (v / total) * 100 for k, v in freq.items()}
    return dict(sorted(freq_percent.items(), key=lambda x: x[1], reverse=True))


def decrypt_with_mapping(ciphertext, mapping):
    result = ""
    for char in ciphertext:
        if char.upper() in mapping:

            if char.isupper():
                result += mapping[char.upper()]
            else:
                result += mapping[char.upper()].lower()
        else:
            result += char
    return result


def refine_mapping(ciphertext, current_mapping):
    """Interactively refine the substitution mapping"""
    mapping_copy = current_mapping.copy()
    while True:
        decrypted = decrypt_with_mapping(ciphertext, mapping_copy)
        print("\nCurrent decryption:")
        print(decrypted[:200] + "...")

        choice = input(
            "\nEnter substitution (e.g., 'A->B' to map A to B, or 'done' to finish): "
        )
        if choice.lower() == "done":
            return mapping_copy

        try:
            source, target = choice.split("-")
            mapping_copy[source.strip().upper()] = target.strip().upper()
            print(source.strip().upper() + "->" + mapping_copy[source.strip().upper()])
        except:
            print("Invalid input. Use format 'A->B' or type 'done'")


with open("stage_0.txt") as file:

    text = file.read()
    print(decrypt_with_mapping(text, decrypt_map))
