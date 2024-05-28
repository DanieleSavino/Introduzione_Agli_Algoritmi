import os

DEFAULT = '''# Introduzione Agli Algoritmi
Collezione di esercizi su algoritmi e strutture dati tratti da vecchi scritti del corso **Introduzione Agli Algoritmi** della Sapienza.\n
'''

def listFiles(path):
    A = []
    for file in os.listdir(path):
        if file.startswith('__') or file.startswith('.'): continue
        newPath = os.path.join(path, file)

        if os.path.isfile(newPath):
            if newPath.endswith('.py'): A.append(file)
        else:
            A.extend(listFiles(newPath))

    return A

def mapFiles(path):
    d = {' '.join(word[0].upper() + word[1:] for word in s.split('_')) : listFiles(s) for s in os.listdir(path) if os.path.isdir(os.path.join(path, s)) and not s.startswith('.')}
    return d

def generateText(fileMap):
    A = []
    for k, v in fileMap.items():
        A.append(f'## {k}\n')
        for s in v:
            A.append(f'- {s}\n')
        A.append('\n')

    return ''.join(A)

def writeReadMe(text, path):
    with open(path, 'w') as f:
        f.write(DEFAULT + text)

def main(path, readmePath):
    fileMap = mapFiles(path)
    text = generateText(fileMap)
    writeReadMe(text, readmePath)

main(os.getcwd(), 'README.md')