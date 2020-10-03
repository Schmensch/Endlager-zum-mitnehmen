import json
import urllib.request

data = open("story.json", "r")
game = json.loads(data.read())

decision = "start"

decision_data = game[decision]

print(decision_data["text"])
print(decision_data["question"])

while True:
    answer = input()
    answer = answer.lower
    if answer == "j" or answer == "n":
        break
    else:
        print("answer has to be <j> or <n>")

decision = decision_data[answer]

print("Nächste Entscheidung: " + decision)
