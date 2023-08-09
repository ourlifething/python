
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

"""
国語>>90
算数>>80
理科>>90
社会>>80
英語>>90
合計430
平均86.0
"""
