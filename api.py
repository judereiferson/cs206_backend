import requests
import heapq

url = "https://api.thebipartisanpress.com/api/endpoints/beta/robert"
API_KEY = "gAAAAABeVpQJKRM5BqPX91XW2AKfz8pJosk182maAweJcm5ORAkkBFj__d2feG4H5KIeOKFyhUVSY_uGImiaSBCwy2L6nWxx4g=="
input = "Joe Biden is a terrible President."


sentences = input.split('.')
total_sum = 0


heap = []

for elem in sentences:
    body = {
        "Text": elem,
        "API": API_KEY
    }
    score = requests.post(url, data=body).content
    f = (float(score.decode("utf-8", "strict")) + 20) / 40
    total_sum += f
    f = abs(0.5 - f)
    if len(heap) < 5:
        heapq.heappush(heap, (f, elem))
    else:
        heapq.heappushpop(heap, (f, elem))
biasedSections = {}
while (len(heap) != 0):
    s = heapq.heappop(heap)
    biasedSections[s[1]] = s[0] + 0.5

print(total_sum / len(sentences), biasedSections)