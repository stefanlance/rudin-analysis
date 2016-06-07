#!/usr/bin/env python3
# Lints the files to give us a status update

import os

def answerKeyStatus(problemCount):
    status = dict()
    for chapter in problemCount:
        status[chapter] = { 
            str(problem): problemStatus(chapter, problem)
            for problem in range(1, problemCount[chapter] + 1)
        }
    return status

def problemStatus(chapter, problem):
    filename = os.path.join("chapters", chapter, "{}.tex".format(problem))
    status = {
        "exists": False,
        "statement": False,
        "solution": False
    }

    if os.path.isfile(filename):
        status["exists"] = True
        problemFile = open(filename).read()
        status["statement"] = "@statement" in problemFile
        status["solution"] = "@qed" in problemFile

    return status

def renderStatus(status):
    print("Rendering the status of each file.")
    print("----")
    print("exists:    Checks if the file exists.")
    print("statement: Checks if the file contains the phrase '@statement'")
    print("solution:  Checks if the file contains '@qed'")
    print("----")
    for chapter in sorted(status.keys(), key=int):
        for problem in sorted(status[chapter].keys(), key=int):
            print(
                "\033[0m{:<5} {}exists {}statement {}solution".format(
                    "{}.{}".format(chapter, problem),
                    "\033[32m" if status[chapter][problem]["exists"] else "\033[31m",
                    "\033[32m" if status[chapter][problem]["statement"] else "\033[31m",
                    "\033[32m" if status[chapter][problem]["solution"] else "\033[31m"
                )
            )
    print("\033[0m", end="")

if __name__ == "__main__":
    answerKey = answerKeyStatus({
        "1":  20,
        "2":  30,
        "3":  25,
        "4":  26,
        "5":  29,
        "6":  19,
        "7":  26,
        "8":  31,
        "9":  31,
        "10": 32,
        "11": 18
    })
    renderStatus(answerKey)
