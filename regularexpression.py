import re

# Input text containing dates
text = "Here are some dates: 20/10/2022, 15-12-2023, and 05/31/2024."

# Define a regular expression pattern to match dates in "dd/mm/yyyy" or "dd-mm-yyyy" format
pattern = r'\b(\d{2}[/-]\d{2}[/-]\d{4})\b'

# Search for dates in the input text using the re module
matches = re.findall(pattern, text)

# Print the matched dates
print("Dates found in the text:")
for match in matches:
    print(match)

# Function to validate dates
def is_valid_date(date):
    try:
        # Try to parse the date and see if it's valid
        from datetime import datetime
        datetime.strptime(date, '%d/%m/%Y')
        return True
    except ValueError:
        return False

# Function to convert dates to a different format
def convert_date_format(date):
    from datetime import datetime
    parsed_date = datetime.strptime(date, '%d/%m/%Y')
    return parsed_date.strftime('%Y-%m-%d')

# Print validation and conversion results
print("\nValidation and Conversion:")
for date in matches:
    if is_valid_date(date):
        print(f"{date} is a valid date.")
        converted_date = convert_date_format(date)
        print(f"Converted date: {converted_date}")
    else:
        print(f"{date} is not a valid date.")

