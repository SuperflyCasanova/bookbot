def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = wordcount(text)
    letters = countletter(text)
    sorted_list = get_sorted_list(letters)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()
    for item in sorted_list:
        if item["entry"].isalpha():
            print(f"The {item["entry"]} character was found {item["count"]} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def wordcount(text):
    words = text.split()
    return len(words)

def sort_on(d):
    return d["count"]

def get_sorted_list(char_dic):
    sorted_list = []
    for entry in char_dic:
        sorted_list.append({"entry": entry, "count": char_dic[entry]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    

def countletter(text):
    letters = {}
    lowered_text = text.lower()
    for letter in lowered_text: 
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters


main()
