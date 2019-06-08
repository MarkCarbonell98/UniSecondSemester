def hhash(s):
    h = 0
    for k in s:
        h = 23*h + ord(k)
    return h


# Eine funktion dass alle mogliche Strings bestehend aus 4 charakteren erzeugt. Jedes String kann Groß-und Kleinbuchstaben erhalten, sowie zahlen. Gibt eine Liste zuruck mit alle mogliche Strings
def createAllPossibleKeys():
    alphabet = [chr(c) for c in range(48,123) if c not in range(91,97) and c not in range(58, 65)]
    print(alphabet)
    result = []
    for i in range(len(alphabet)):
        for j in range(len(alphabet)):
            for k in range(len(alphabet)):
                for l in range(len(alphabet)):
                    word = alphabet[i] + alphabet[j] + alphabet[k] + alphabet[l]
                    result.append(word)
    return result

def getKeysWithCollisionsLength(length):
    # Mit unsere Liste von Strings, konnen wir alle die Hashes fur jeder String suchen, und die in eine andere Liste umschreiben mit der dazugehorige hhash Wert als ein (String, Hash) tupel. Danach werden alle nach dem Wert des Hashes sortiert (*)
    words = createAllPossibleKeys()
    print(len(words))
    seenHashes = []
    for word in words:
        wordHash = hhash(word)
        seenHashes.append((word, wordHash)) 
    sortedHashes = sorted(seenHashes, key=lambda x: x[1]) # (*)

    # Jetzt konnen wird jeder neue Hash in ein Dict speichern, sodass keine Hash sich wiederholt und der Suchzeit von jeden Key konstant bleibt. Danach iterieren wir durch unsere sorted tupeln, und wenn der hash von einen wort gleich ist zu dem des nachstes Wortes, dann haben beide Strings den selben Hash-wert. (**)

    repeatedHashes = {}
    for i in range(len(sortedHashes)):
        prevHash, actualHash, actualWord,nextWord = sortedHashes[i-1][1], sortedHashes[i][1], sortedHashes[i-1][0], sortedHashes[i][0]
        if prevHash == actualHash: # (**)
            # Danach checken wir ob jedes neue Hashwert schon in unsere Dict gespeichert ist. Falls nicht, dann deklarieren wir den value von dem Key-Value paar als ein python-set mit beide Worter enthalten. Falls nicht, dann fügen wir einfach beide wörter in dem set. Der set gewahrleisted dass alle neue Strings nur einmal ins Set erscheinen konnen. Am ende geben wir einen Dictionary zuruck, wo nur die key-Value paare mit dem gewunschten Lange stehen
            if not prevHash in repeatedHashes.keys():
                repeatedHashes[prevHash] = set([actualWord, nextWord])
            else:
                repeatedHashes[prevHash].add(actualWord)
                repeatedHashes[prevHash].add(nextWord)
    return dict((key,value) for key,value in repeatedHashes.items() if len(value) == length) # (***)

wishedLength = 16
print(getKeysWithCollisionsLength(wishedLength))

