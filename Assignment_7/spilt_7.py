import re

txt = "apple,banana;orange grape,pear"

# Split by commas, semicolons, or spaces
parts = re.split(r"[,;\s]+", txt)

print("Split tokens:", parts)