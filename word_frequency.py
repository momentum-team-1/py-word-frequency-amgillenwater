STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

def clean_text(text):
    """
    Given a text, return the text with no spaces or punctuation and all lowercased.
    """
    text = text.lower()
    all_letters = "abcdefghijklmnopqrstuvwxyz "
    text_to_keep = ""
    for char in text:
        if char in all_letters:
            text_to_keep += char
    return text_to_keep

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    open_file=open(file)
    whole = open_file.read()
    cleaned_text = []
    cleaned_text.append(clean_text(whole).split(" "))
    print(remove_from_list(cleaned_text, STOP_WORDS))



   
def remove_from_list(list_of_items, items_to_remove):
    new_list = []
    for item in list_of_items:
        if not item in items_to_remove:
            new_list.append(item)
    return(new_list)

if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)