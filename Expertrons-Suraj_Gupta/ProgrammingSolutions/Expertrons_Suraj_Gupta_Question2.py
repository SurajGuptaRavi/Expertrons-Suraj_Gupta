A = ['Raj', 'Pankaj', 'Shreyas']
B = ['Sandeep', 'Vikas', 'Raj']

new_list = [person_name for person_name in A if person_name not in B] + [person_name for person_name in B if person_name not in A]

print(new_list)
