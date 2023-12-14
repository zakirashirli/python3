import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('/Users/zakirashirli/Documents/GitHub/python3/files/spotify_songs.csv')

print(df.head())

print("\nSummary Statistics:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

sns.set(style="whitegrid")

plt.figure(figsize=(12, 8))

sns.histplot(df['track_popularity'], bins=20, kde=True, color='skyblue', edgecolor='black')

plt.title('Distribution of Song Popularity', fontsize=16)
plt.xlabel('Popularity (0-100)', fontsize=14)
plt.ylabel('Frequency', fontsize=14)

# Add grid lines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

mean_popularity = df['track_popularity'].mean()
plt.axvline(mean_popularity, color='red', linestyle='--', linewidth=2, label='Mean Popularity')

plt.legend()
plt.show()
