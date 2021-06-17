# a & b)

def write_punishment(text, nr_reps = 10):
    punishment_text = (text[:6] + text[10:].replace('paste', 'delete')) * nr_reps
    return punishment_text

p_text = "I will not copy-paste all that crap from Stackoverflow\n"
reps = 20

print(write_punishment(p_text))