import re

txt = "Please email secret@company.com or contact ceo@corp.org directly."

# Redact any email found in the text
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}"
redacted_text = re.sub(pattern, "[HIDDEN EMAIL]", txt)

print("Sanitized text:")
print(redacted_text)