################################## Functions and globals. ####################
def main():
    path_to_file = "books/frankenstein.txt"
    book = getBookText(path_to_file)
    print(wordCount(book))

    characterCount = perCharacterCount(book)
    print(characterCount)

def getBookText(pathToBook):
    with open(pathToBook) as f:
        return f.read()

def wordCount(input):
    return len(input.split())

def perCharacterCount(input):
    characterCount = {}
    for char in input:
        lc = char.lower()
        if lc in characterCount:
            characterCount[lc] += 1
        else:
            characterCount[lc] = 1
    return characterCount

    # Oh my god, so unecessary:
    #def wordCount(input):
    # count = 0
    # lines = input.split("\n")
    # for line in lines:
    #     if len(line) > 0:
    #         wcount = 0
    #         words  = line.split()
    #         for word in words:
    #             if len(word) > 0:
    #                 wcount += 1
    #         count += wcount
    # return count


############################################################################## 
### Should have nothing but main() .....
##############################################################################
main()
