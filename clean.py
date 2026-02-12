import re

input_path = "regulation.txt"
output_path = "regulation_clean.txt"

with open(input_path, "r", encoding="utf-8") as f:
    text = f.read()

# Remove page numbers like "Page 1", "1", "2", etc.
text = re.sub(r"\bPage\s+\d+\b", "", text)
text = re.sub(r"\b\d+\b", "", text)

# Remove multiple newlines
text = re.sub(r"\n\s*\n", "\n", text)

# Normalize spaces
text = re.sub(r" +", " ", text)

# Strip leading/trailing whitespace
text = text.strip()

with open(output_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Cleaned text saved to regulation_clean.txt")