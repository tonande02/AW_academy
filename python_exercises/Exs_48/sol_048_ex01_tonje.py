# a & b)
 
punishment_text = "I will not copy-paste the solutions from the Stackoverflow"
numb_of_repititions = 20
reps_completed = 0

while reps_completed < numb_of_repititions:
    print((punishment_text[:6] + punishment_text[10:].replace('paste', 'delete')))
    reps_completed += 1

print()

for i in range(numb_of_repititions):
    print((punishment_text[:6] + punishment_text[10:].replace('paste', 'delete')))
