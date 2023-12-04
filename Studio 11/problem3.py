import csv


def calculate_percentage(score, total_questions):
    return (score / total_questions) * 100


with open('stats.csv', 'r') as file:
    lines = file.readlines()
    answer_key = lines[0].strip().split(',')

total_questions = len(answer_key)
scores = []

for line in lines[1:]:
    student_answers = line.strip().split(',')
    score = sum(1 for a, b in zip(answer_key, student_answers) if a == b)
    scores.append(score)

sorted_scores = sorted(scores)
high_score = max(scores)
low_score = min(scores)
median_score = (sorted_scores[len(sorted_scores) // 2] + sorted_scores[(len(sorted_scores) - 1) // 2]) / 2
mean_score = sum(scores) / len(scores)

print(f"OUTPUT High: {calculate_percentage(high_score, total_questions):.2f}%, Low: {calculate_percentage(low_score, total_questions):.2f}%, Median: {calculate_percentage(median_score, total_questions):.2f}%, Mean: {calculate_percentage(mean_score, total_questions):.2f}%")

# passed