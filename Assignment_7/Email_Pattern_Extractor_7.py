import re

def extract_emails(text):
    # Breakdown:
    # [a-zA-Z0-9._%+-]+ : Username (letters, numbers, dots, hyphens, underscores)
    # @                 : Literal '@'
    # [a-zA-Z0-9.-]+    : Domain name
    # \.[a-zA-Z]{2,4}   : Domain extension (2-4 characters)
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}"
    return re.findall(pattern, text)

sample_data = """
For queries, contact support@domain.com or reach out to
prof.smith_12@college.edu. Alternate: test-account@org.net.
"""

emails = extract_emails(sample_data)

print(f"Total emails found: {len(emails)}")
for i, email in enumerate(emails, 1):
    print(f"  {i}. {email}")