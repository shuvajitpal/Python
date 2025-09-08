import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('Book1.csv')
print("First 5 rows of dataset:")
print(df.head())
print("\nDataset Info:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe())

column = "Salary"
if column in df.columns:
    col_data = df[column].dropna() 
    mean_val = np.mean(col_data)
    median_val = np.median(col_data)
    min_val = np.min(col_data)
    max_val = np.max(col_data)
    std_val = np.std(col_data)
    print(f"\nAnalysis of column: {column}")
    print(f"Mean: {mean_val}")
    print(f"Median: {median_val}")
    print(f"Min: {min_val}")
    print(f"Max: {max_val}")
    print(f"Standard Deviation: {std_val}")
else:
    print(f"Column '{column}' not found in dataset.")

# Bar Chart for categorical column counts
cat_column = "Age" 
if cat_column in df.columns: 
    df[cat_column].value_counts().plot(kind="bar", color="skyblue", edgecolor="black")
    plt.title(f"Bar Chart of {cat_column}")
    plt.xlabel(cat_column)
    plt.ylabel("Count")
    plt.show()

# Scatter Plot between two numeric columns
x_col = "Salary"
y_col = "Age"
if x_col in df.columns and y_col in df.columns:
    plt.scatter(df[x_col], df[y_col], alpha=0.7, color="green")
    plt.title(f"Scatter Plot of {x_col} vs {y_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.show()

# Heatmap of correlation matrix
numeric_df = df.select_dtypes(include=[np.number])
corr_matrix = numeric_df.corr()
fig, ax = plt.subplots(figsize=(6, 5))
cax = ax.imshow(corr_matrix, cmap="coolwarm", interpolation="nearest")
fig.colorbar(cax)
ax.set_xticks(range(len(corr_matrix.columns)))
ax.set_yticks(range(len(corr_matrix.columns)))
ax.set_xticklabels(corr_matrix.columns, rotation=45, ha="right")
ax.set_yticklabels(corr_matrix.columns)
for i in range(len(corr_matrix.columns)):
    for j in range(len(corr_matrix.columns)):
        ax.text(j, i, f"{corr_matrix.iloc[i, j]:.2f}",
                ha="center", va="center", color="black")
ax.set_title("Heatmap of Correlation Matrix")
plt.tight_layout()
plt.show()

print("\n--- Insights & Observations ---\n" \
"1. The bar chart shows the distribution of categories in the selected column.\n" \
"2. The scatter plot reveals possible relationships between the chosen numeric columns.\n" \
"3. The heatmap highlights correlations between numeric features, useful for feature selection.")