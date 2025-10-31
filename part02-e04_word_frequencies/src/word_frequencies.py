#!/usr/bin/env python3



def word_frequencies(filename):
    with open(filename, 'r') as f:
        lines = [line for line in f.readlines()]
        #print(lines)
        words = [word.strip("""!"#$%&'()*,-./:;?@[]_""") for line in lines for word in line.split()] 
        #print(words)

    def counting(w):
        return words.count(w)
    return {word: counting(word) for word in set(words)}

def main():
    word_frequencies("src/alice.txt")    

if __name__ == "__main__":
    main()
