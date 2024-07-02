# if applicant has high income and good credit is eligible for loan

has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("is eligible for loan")

# if an applicant had good credit and doesn't have criminal record is eligible for loan
has_good_credit = True
has_criminal_record = True

if has_good_credit and not has_criminal_record:
    print("is eligible for loan")