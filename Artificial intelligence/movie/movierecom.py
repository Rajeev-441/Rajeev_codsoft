import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

# Sample movie ratings data
data = {
    'User': ['A', 'B', 'C', 'D', 'E'],
    'Movie1': [5, 4, 1, 4, 2],
    'Movie2': [3, 5, 2, 3, 3],
    'Movie3': [4, 1, 5, 3, 4],
    'Movie4': [2, 2, 4, 1, 5],
    'Movie5': [1, 3, 2, 5, 4]
}
df = pd.DataFrame(data)

# Function to recommend movies based on user preferences
def recommend(user):
    # Normalize the data
    scaler = StandardScaler()
    ratings = df.drop('User', axis=1)
    normalized_ratings = scaler.fit_transform(ratings.T).T

    # Compute cosine similarity
    user_similarity = cosine_similarity(normalized_ratings)

    # Find the index of the given user
    user_index = df[df['User'] == user].index[0]

    # Calculate the weighted sum of ratings for each movie
    similar_users = user_similarity[user_index]
    weighted_sum = sum(similar_users[i] * normalized_ratings[i] for i in range(len(similar_users)))

    # Sort movies by weighted sum and return the top 3 recommendations
    recommendations = pd.Series(weighted_sum, index=ratings.columns).sort_values(ascending=False)
    return recommendations.index[:3]

# Function to handle recommendation button click
def recommend_movies():
    user = user_entry.get().strip()
    if user in df['User'].values:
        recommendations = recommend(user)
        messagebox.showinfo("Recommendations", f"Top 3 recommended movies for {user}: {', '.join(recommendations)}")
    else:
        messagebox.showwarning("Invalid User", "User not found in the database.")

# Set up the main application window
root = tk.Tk()
root.title("Movie Recommendation System")

# User input
user_label = tk.Label(root, text="Enter User:")
user_label.pack(pady=5)
user_entry = tk.Entry(root)
user_entry.pack(pady=5)

# Recommendation button
recommend_button = tk.Button(root, text="Recommend Movies", command=recommend_movies)
recommend_button.pack(pady=20)

# Start the application
root.mainloop()

