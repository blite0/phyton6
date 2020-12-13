stud = {'ivanov_ivan': [4, 4, 5], 'petrov_petr': [3, 3, 5], 'stepanov_stepan': [4, 4, 4]}
stud_val = {
'ivanov_ivan': sum([4, 4, 5])/len(stud.values()),
'petrov_petr': sum([3, 3, 5])/len(stud.values()),
'stepanov_stepan': sum([4, 4, 4])/len(stud.values())
}
for key in stud_val.keys():
    print(key, stud_val[key])