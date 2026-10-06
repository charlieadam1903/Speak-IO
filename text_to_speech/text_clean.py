
import utility

test_inputs = {
    "Unicode Normalization": [
        "ﬁnancial",            # Ligature
        "élite",              # Combining accent
        "① Choice",           # Circled number
        "ℌello 𝕎orld",        # Fancy Unicode
    ],
    "Special Punctuation": [
        "“Hello”—he said…",
        "‘It’s fine,’ she replied.",
        "• Step 1: Start"
    ],
    "Whitespace Normalization": [
        "   Welcome     back!   ",
        "Line one\n\nLine two",
        "Word1\t\tWord2"
    ]
}

# Run and print results
for category, examples in test_inputs.items():
    print(f"\n=== {category} ===")
    for original in examples:
        cleaned = utility.clean_tts_input(original)
        print(f"Input:    {repr(original)}")
        print(f"Cleaned:  {repr(cleaned)}\n")
