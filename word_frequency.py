STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]
import string
punctuation = string.punctuation

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    open_file=open(file)
    whole = open_file.read()
    # print(whole)
    for word in whole:
        word=whole.lower()
    print(word)

        

       
            
        
            

    

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



def remove_from_list(list_of_items, items_to_remove):
    new_list = []
    for item in list_of_items:
        if not item in items_to_remove:
            new_list.append(item)
    return(new_list)

