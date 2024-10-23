has_high_icome = True
has_good_credit = True

if has_high_icome and has_good_credit:
    print("Eligible for loan.")
else:
    print("Not eligible for loan.")

has_high_icome = True
has_good_credit = False

if has_high_icome or has_good_credit:
    print("Eligible for loan.")
else:
    print("Not eligible for loan.")

has_high_icome = True
has_criminal_record = True

if has_high_icome and not has_criminal_record:
    print("Eligible for loan.")
else:
    print("Not eligible for loan.")