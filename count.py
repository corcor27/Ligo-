from collections import Counter
def main():
    #use open() for opening file.
    #Always use `with` statement as it'll automatically close the file for you.
    with open(r'home/cory\Documents\posteriors_samples.txt') as f:
        #create a list of all words fetched from the file using a list comprehension
        words = [word for line in f for word in line.split()]
        print "The total word count is:", len(words)
        #now use collections.Counter
        c = Counter(words)
        for word, count in c.most_common():
           print word, count
main()
