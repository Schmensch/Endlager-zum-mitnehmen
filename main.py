import json
import sys

try:
    data = open("story.json", "r", encoding="utf-8")
except:
    print("story.json was not found. Exiting.")
    sys.exit()

story = json.loads(data.read())

decision = "start"

while True:
    decision_data = story[decision]

    print(decision_data["text"])
    print(decision_data["question"])

    answer = input()

    decision = decision_data[answer]

#test