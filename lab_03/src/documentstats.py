# based on code from https://github.com/kevinwlu/iot/tree/master/lesson3
import string
import sys


def readFile(filename):
    with open(filename, "r") as fc:
        contents = fc.read()
    return contents


def wordCount(contents):
    wordCount = 0
    wordCountDict = {}
    lowerContents = contents.lower()
    listWords = lowerContents.split()
    stopWords = [
        "a",
        "and",
        "the",
        "are",
        "be",
        "is",
        "by",
        "for",
        "from",
        "in",
        "of",
        "on",
        "to",
        "with",
        "that",
        "which",
    ]
    for word in listWords:
        word = word.strip(string.punctuation)
        wordCount = wordCount + 1
        if word not in stopWords:
            if word in wordCountDict:
                wordCountDict[word] = wordCountDict[word] + 1
            else:
                wordCountDict[word] = 1
    print(f"Word Count: {wordCount}")
    return wordCountDict


def topTenWords(wordCountDict):
    topTenWords = sorted(wordCountDict.items(), key=lambda x: -x[1])[:10]
    print(f"Top Ten Words: {topTenWords}")


def main():
    filename = sys.argv[1]
    contents = readFile(filename)
    wordCountDict = wordCount(contents)
    topTenWords(wordCountDict)


if __name__ == "__main__":
    main()
