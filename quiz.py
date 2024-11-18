import random
questions =[
  {"question": "What is the capital city of Uganda?", "options":["Kampala", "Entebbe", "JinJa"], "answer": "Kampala"},
   {"question": "What is the capital city of USA?", "options":["NewYork", "Chicago", "Washington, D.C"], "answer": "Washington, D.C"},
    {"question": "What is the capital city of Rwanda?", "options":["Kigali", "Rutoma", "Kishasha"], "answer": "Kigali"},
    {"question": "What is the longest river in Africa?", "options":["R.Nile", "R.Aswa", "R.Rwizi"], "answer": "Kigali"},
    {"question": "Which of the following is the smallest unit of data in a computer?", "options":[" Byte", "Bit", " Kilobyte"], "answer": "Bit"},
    {"question": "Which of the following programming languages is primarily used for web development?", "options":["HTML", "Python", "CSS"], "answer": "HTML"}
]
random.shuffle
score=0

print("Welcome to The Quiz Game")
for i, q in enumerate(questions):
  print(f"Question {i+1}:{q['question']}")
  for index, option in enumerate(q['options'], start=1):
    print(f"{index}.{option}")
  answer=input("Enter the number of your answer:")
  if q['options'][int(answer)-1] ==q['answer']:
    print("Correct")
    score+=1
  else:
    print(f"Wrong! The correct answer was: {q['answer']}")
print(f"Yoour final score is: {score}/{len(questions)}")
if score==len(questions):
  print("Excellent! You're a genius!")
elif score >len(questions)//2:
  print("Good job! you did well.")
else:
  print("Better luck next time")