# Write a function print_freq_results(results). This function should take an argument results that is a list of tuples like the following:
results =  [
       ('her', 33),
       ('all', 12),
       ('which', 12),
       ('she', 7),
       ('their', 7),
   ]

def print_freq_results(results):
    for word, frequency in results.items():
        print(word)
        for count, number in frequency.items():
            print (count, number)

print_freq_results(results)