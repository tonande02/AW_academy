f_name = "FREDDIE"
l_name = "fredson"
course = "AW Academy Data Engineer Intensive Training Program"
nr_of_candidates = "11"

# a)
print(f"""My name is {f_name} {l_name}. I'm currently taking the training
course '{course}.' There are {nr_of_candidates} candidates taking
the course.
""")

# b)
print(f"""My name is {f_name.capitalize()} {l_name.capitalize()}. I'm currently taking the training
course '{course}.' There are {nr_of_candidates} candidates taking
the course.
""")

# c)
print(f"""My name is {f_name.capitalize()} {l_name.capitalize()}. I'm currently taking the training
course '{course.lower()}.' There are {nr_of_candidates} candidates taking
the course.
""")
