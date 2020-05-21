stop_words = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]
def remove_line_breaks(passage):
    no_line_break = []
    no_line_break = passage.rstrip()
    return no_line_break
    print(no_line_break)

def clean_text(text):
    """
    this will lowercase the text and throw out any punctuation, executes second
    """
    text = text.lower()
    all_letters = "abcdefghijklmnopqrstuvwxyz "
    text_to_keep = ""
    for char in text:
        if char in all_letters:
            text_to_keep += char
    return text_to_keep

def remove_from_list(list_of_items, items_to_remove):
    """this function we wrote in class should work directly, needs to remove the stop words after removing page breaks, lowercasing, etc"""
    new_list = []
    for item in list_of_items:
        if not item in items_to_remove:
            new_list.append(item)
    return(new_list)
    
def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    open_file=open(file)
    whole = open_file.read()
    text = clean_text(whole).split()
    # print(text)
    squeaky_clean_text = remove_from_list(text, stop_words)
    print(squeaky_clean_text)
    # step_one = remove_line_breaks(whole)
    # print(step_one)
    # cleaned_text = []
    # cleaned_text = step_one.append(clean_text(whole).split(" "))
    # print(cleaned_text)
    # now = remove_from_list(cleaned_text, STOP_WORDS)
    # print(now)

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