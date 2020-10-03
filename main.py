import json
import urllib.request

url = 'https://raw.githubusercontent.com/Schmensch/Endlager-zum-mitnehmen/master/story.json'
data = urllib.request.urlopen(url)
game = json.loads(data.read())

decision = "start"

decision_data = game[decision]

print(decision_data["text"])
print(decision_data["question"])
answer = input()

decision = decision_data[answer]

print("Nächste Entscheidung: " + decision)
