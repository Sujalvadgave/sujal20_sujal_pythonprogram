import pandas as pd
import random

# List of Indian names
indian_names = ["Aarav", "Aaradhya", "Siddharth", "Ishita", "Rohan"]

# Create sample data
data = {
    'Name': [random.choice(indian_names) for _ in range(10)],  # Randomly select from Indian names
    'Class': [random.randint(1, 12) for _ in range(10)],  # Random class from 1 to 12
    'Roll No': [random.randint(1001, 1100) for _ in range(10)]  # Random roll numbers
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
