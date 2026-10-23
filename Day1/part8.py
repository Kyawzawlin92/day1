scores = [55,80,35,90,65]

scores.append(75)
scores[1] = 85
print(scores)
print("Maximum:",max(scores))
print("Minimum:",min(scores))

print("Average:",sum(scores)/len(scores))

for score in scores:
    if(score >= 80):
        print("Scores grater than 80:",score)