age = input("what is yoour current age? ")

result = 90-int(age)
result_days= result*365
result_weeks = result*52
result_months=result*12
message=f"You have {result_days} days, {result_weeks} weeks, and {result_months} months left."
print(message)