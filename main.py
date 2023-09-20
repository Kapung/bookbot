def count_words(s):
    print(f"{len(s.split())} words found in the document\n")

def count_letters(s):
    counter = {}
    for i in s:
        i = i.lower()
        counter[i] = counter.get(i, 0) + 1
    dL = list(counter.items())
    dL.sort()
    for i in dL:
        if i[0].isalpha():
            print(f"The '{i[0]}' character was found {i[1]} times")



with open("books/frankenstein.txt") as f:
    file_contents = f.read()

    print("--- Begin report of books/frankenstein.txt ---")
    count_words(file_contents)
    count_letters(file_contents)
    print("--- End report ---")