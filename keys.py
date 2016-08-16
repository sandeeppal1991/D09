"""
Write three functions:
sort1(langauges)
sort2(languages)
sort3(langauges)
Goal: Print exactly the below w/ three functions:
1:
    Arabic
    English
    Koine Greek
    Latin
    Romanian
    C++
    JavaScript
    Python
    R
2:
    R
    C++
    Latin
    Arabic
    Python
    English
    Romanian
    JavaScript
    Koine Greek
3:
    JavaScript
    R
    Latin
    Python
    Romanian
    Koine Greek
    English
    Arabic
    C++
"""

languages = {'JavaScript': 'P',
             'Arabic': 'N',
             'R': 'P',
             'Python': 'P',
             'C++': 'P',
             'Koine Greek': 'N',
             'Latin': 'N',
             'Romanian': 'N',
             'English': 'N'}
def sort1(languages):
    lst = sorted(sorted(languages) , key=languages.__getitem__)
    for x in lst:
        print(x)
def sort2(languages):
    lst = sorted(languages, key = len)
    for x in lst:
        print(x)
def sort3(languages):
    lst = sorted(sorted(languages), key = lambda x:x[-1].lower(), reverse = True)
    for x in lst:
        print(x)
print("1:\n\n")
sort1(languages)
print("\n\n")
print("2.\n\n")
sort2(languages)
print("\n\n")
print("3.\n\n")
sort3(languages)
