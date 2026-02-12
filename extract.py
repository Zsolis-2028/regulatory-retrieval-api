import fitz  # PyMuPDF

pdf_path = "regulation.pdf"
output_path = "regulation.txt"

doc = fitz.open(pdf_path)
text = ""

for page in doc:
    text += page.get_text()

with open(output_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Extracted text to regulation.txt")