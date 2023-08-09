
scores = []
scores.append(int(input('国語>>')))
scores.append(int(input('算数>>')))
scores.append(int(input('理科>>')))
scores.append(int(input('社会>>')))
scores.append(int(input('英語>>')))

total_score = sum(scores)
avg_score = total_score / len(scores)

print(f'合計{total_score}')
print(f'平均{avg_score}')
