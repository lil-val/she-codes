import re
text = "(note 1): my phone number is (541) 754-3010, your's is (555) 323-7121. I have 912 cellphones as you can see on page (414). This (071) 314-1592 is not a valid US phone number."
regex = r'(\([23456789][0-9]{2}\) \d{3}-\d{4})'

groups = re.findall(regex, text)
print(groups)
output = [int(x[6:9]) for x in groups]
print(output)


text1 = """This http://www.foo.com/gag.txt is a web URL. This other one HTTP://WWW.UPPERCASE.COM is too.
on the other hand httl://www.google.com/index.html and mailto:fooman@foo.com are not.
http://spaz.info/31415.html is quite OK too. http:///www.cnn.com is messed up."""

webURLregex = r"((http|HTTP)://([^/\s]+))"
groups = re.findall(webURLregex, text1)
print(groups)
thirdGroup = groups[2]
output = thirdGroup[2]
print(output)
