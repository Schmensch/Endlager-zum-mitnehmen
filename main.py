import json
import urllib.request

data = open("story.json", "r")
game = json.loads(data.read())

decision = "start"

decision_data = game[decision]

print(decision_data["text"])
print(decision_data["question"])
answer = input()

decision = decision_data[answer]

print("Nächste Entscheidung: " + decision)
