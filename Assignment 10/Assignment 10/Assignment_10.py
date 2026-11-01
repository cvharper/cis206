
# so we can do what we need to
import re

# 1. check if string contains only a-z, A-Z and 0-9
strings = ["ABCDEFabcdef123450", "*&%@#!}{"]
for s in strings:
    print(bool(re.fullmatch(r"[a-zA-Z0-9]+", s)))
    print("")


# 2. match a followed by zero or more b's
strings = ["ab", "abc", "a", "ab", "abb"]
for s in strings:
    print(s, bool(re.fullmatch(r"ab*", s)))
    print("")


# 3. match a followed by mutiple b's
strings = ["ab", "abc", "a", "ab", "abb"]
for s in strings:
    print(s, bool(re.fullmatch(r"ab+", s)))
    print("")


# 4. find lowercase letters with an underscore
strings = ["aab_cbbbc", "aab_Abbbc", "Aaab_abbbc"]
for s in strings:
    print(re.findall(r"[a-z]+_[a-z]+", s))
    print("")


# 5. match a word at the beginning of a string
strings = [
    "The quick brown fox jumps over the lazy dog.",
    " The quick brown fox jumps over the lazy dog."
]
for s in strings:
    print(bool(re.match(r"\w+", s)))
    print("")


# 6. match a word containing z
strings = [
    "The quick brown fox jumps over the lazy dog.",
    "Python Exercises."

]
for s in strings:
    print(re.findall(r"\w*z\w*", s))
    print("")


# 7. remove leading zeros from an IP address
ip = "216.08.094.196"

print(re.sub(r"\b0+(\d)", r"\1", ip))
print("")


# 8. search for literal strings within a string
text = "The quick brown fox jumps over the lazy dog."
words = ["fox", "dog", "horse"]

for word in words:
    if re.search(re.escape(word), text):
        print(word, "found")
        print("")

    else:
        print(word, "not found")
        print("")


# 9. search for a literal string and find its location
text = "The quick brown fox jumps over the lazy dog."
word = "fox"
print("")

match = re.search(word, text)
if match:
    print("Found:", word)
    print("Position:", match.start())
    print("")

else:
    print("Not found")
    print("")


# 10. replace whitespaces with underscores and vice versa
text1 = "Regular Expressions"
text2 = "Code_Examples"

print(re.sub(r"\s", "_", text1))
print(re.sub(r"_", " ", text2))
print("")


# 11. extract year, month and date from this URL
url = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"

match = re.search(r"/(\d{4})/(\d{2})/(\d{2})/", url)
if match:
    print("Year:", match.group(1))
    print("Month:", match.group(2))
    print("Date:", match.group(3))
    print("")


# 12. find words starting with a or e
text = """The following example creates an ArrayList with a capacity of 50
elements. Four elements are then added to the ArrayList and the ArrayList
is trimmed accordingly."""
print("")

words = re.findall(r"\b[aeAE]\w*", text)
print(words)
print("")


# 13. replace spaces, commas and dots with colons
text = "Python Exercises, PHP exercises."
print(re.sub(r"[ ,.]", ":", text))
print("")


# 14 looks to be the same as 12 so I won't bother writing it twice


# 15. remove multiple spaces from a string
text = "Python    Exercises"
print(re.sub(r"\s+", " ", text))
print("")
