import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV
df = pd.read_csv("student_data.csv")

# Show data
print("First 5 rows:")
print(df.head())

# Basic stats
print("\nStatistics:")
print(df.describe())

# Add average column
df["average"] = df[["math", "science", "english"]].mean(axis=1)

# Top performer
top_student = df.loc[df["average"].idxmax()]
print("\nTop Performer:")
print(top_student)

# Plot
plt.figure(figsize=(8,5))
sns.barplot(x="name", y="average", data=df)
plt.title("Student Average Scores")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
