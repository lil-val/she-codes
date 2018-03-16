import re
text = "(note 1): my phone number is (541) 754-3010, yours is (555) 323-7121. I have 912 cellphones as you can see on page (414). This (071) 314-1592 is not a valid US phone number."
regex = r'(\([23456789][0-9]{2}\) \d{3}-\d{4})'

groups = re.findall(regex, text)
print(groups)
output = [int(x[6:9]) for x in groups]
print(output)
