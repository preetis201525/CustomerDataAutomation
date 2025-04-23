
import pandas as pd
import re

# Load raw file
df = pd.read_csv(r"D:\preeti\automation\CustomerDataAutomation\Raw\CustomerData_Raw.csv")

# Clean Phone Numbers (retain digits only)
df["CleanedPhone"] = df["PhoneNumber"].astype(str).apply(lambda x: re.sub(r"\D", "", x))

# Validate Emails – basic '@' and '.' check
df["EmailValid"] = df["EmailAddress"].astype(str).apply(
    lambda x: "Valid" if "@" in x and "." in x and x.count("@") == 1 else "Invalid"
)

# Save Cleaned Output
df.to_csv(r"D:\preeti\automation\CustomerDataAutomation\Cleaned\CustomerData_Cleaned.csv", index=False)

print("✅ Data cleaned and saved to CustomerData_Cleaned.csv")

# Optional: Preview cleaned output
cleaned_df = pd.read_csv(r"D:\preeti\automation\CustomerDataAutomation\Cleaned\CustomerData_Cleaned.csv")
print(cleaned_df.head())
