################################## Functions and globals. ####################
def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
        print(wordCount(file_contents))

def wordCount(input):
    count = 0
    lines = input.split("\n")
    for line in lines:
        if len(line) > 0:
            wcount = 0
            words  = line.split()
            for word in words:
                if len(word) > 0:
                    wcount += 1
            count += wcount
    return count

############################################################################## 
### Should have nothing but main() .....
##############################################################################
main()
