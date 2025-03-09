import decisions
2
options = float(input("Enter the number of options: "))
total = float(input("Enter the total count: "))

# Compute the options ratio
result = decisions.get_options_ratio(options, total)

# Get the faculty rating based on the ratio
rating = decisions.get_faculty_rating(result)

print(f"The faculty rating is: {rating}")
