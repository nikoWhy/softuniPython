days = int(input())

doctors = 7
treated_patients = 0
untreated_patients = 0

for i in range(1, days+1):
    current_patients = int(input())
    if i%3==0:
        if untreated_patients > treated_patients and current_patients >= doctors:
            doctors += 1
            treated_patients += doctors
            untreated_patients += (current_patients-doctors)
        else:
            treated_patients += current_patients
    else:
        if current_patients >= doctors:
            treated_patients += doctors
            untreated_patients += (current_patients-doctors)
        else:
            treated_patients += current_patients

print(treated_patients)
print(untreated_patients)