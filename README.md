Recommendation System Project

Overview
This project implements a movie recommendation system using collaborative filtering, enhanced with interactive data visualizations to provide insights into user ratings, movie popularity, and recommendation trends. The system leverages a dataset of movie ratings (movies.csv) to recommend movies based on user preferences, while visualizations in index.html analyze user behavior and recommendation outcomes.
Project Objectives

Recommendation System: Suggest movies to users based on collaborative filtering, using user ratings from movies.csv.
Data Visualizations: Provide insights into:
Average ratings by user group (Young Adults, Adults, Seniors) from 2010 to 2020.
Rating trends over time to identify shifts in preferences.
Movie popularity to assess recommendation distribution.


Visualization Goals: Meet requirements for appropriate chart types, clarity, aesthetics, interactivity, and storytelling, as outlined in the project guidelines.

Project Structure

recommendation.py: Python script implementing collaborative filtering for movie recommendations.
movies.csv: Dataset containing user ratings for movies.
index.html: Interactive visualizations using Chart.js to display rating trends and movie popularity.
data.json: Sample dataset for visualizations, derived from movies.csv concepts.
README.md: Comprehensive project documentation (this file).

Methodologies
Recommendation System
The recommendation system uses collaborative filtering, specifically item-based collaborative filtering, to suggest movies. The methodology includes:

Data Preprocessing: Load movies.csv using Pandas, handling user ratings (1–5 scale) for movies.
Similarity Computation: Calculate cosine similarity between movies based on user ratings to identify similar items.
Recommendation Generation: For a given user, predict ratings for unrated movies based on similarities to rated movies, recommending the highest-scored ones.
Tools: Python, Pandas, NumPy, Scikit-learn (for similarity metrics).

Data Visualizations
The visualizations analyze user ratings and recommendation outcomes, using Chart.js for interactive charts:

Bar Chart: Compares average ratings across user groups (Young Adults, Adults, Seniors) for each year, highlighting preference differences.
Line Chart: Shows rating trends over time, revealing shifts in user behavior.
Pie Chart: Displays movie popularity based on recommendation frequency, identifying dominant genres.
Interactivity: Includes a dropdown to filter by user group and tooltips for detailed data points.
Aesthetics: Uses high-contrast colors, clear labels, and modern styling (white containers, shadows, rounded corners).
Storytelling: Narrates user engagement trends and potential algorithm biases (e.g., over-recommending action movies).

Setup Instructions
Prerequisites

Python Environment:
Python 3.8 or higher.
Install required libraries: pip install pandas numpy scikit-learn.


Web Browser: For viewing visualizations (no additional setup needed, as Chart.js is loaded via CDN).
Internet Connection: Required to load Chart.js and its plugins in index.html.

Installation

Clone the Repository:git clone https://github.com/harshjaiswal848/Recommendation_System
cd Recommendation_System


Set Up Python Environment:
Create a virtual environment (optional but recommended):python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:pip install pandas numpy scikit-learn




Verify Dataset:
Ensure movies.csv is in the repository root.
The visualization dataset (data.json) is included for index.html. To use real data from movies.csv, preprocess it to match the data.json structure (see "Customizing Visualizations" below).


Run Visualizations:
Open index.html in a web browser (e.g., Chrome, Firefox) to view visualizations.
No server is required, as Chart.js is loaded via CDN.



Usage Examples
Running the Recommendation System

Generate Recommendations:
Run recommendation.py to get movie recommendations for a user:python recommendation.py


Example output (assuming recommendation.py prints recommendations):Recommendations for User 123:
1. The Matrix (Predicted Rating: 4.5)
2. Inception (Predicted Rating: 4.3)




Customize Input:
Modify recommendation.py to input a specific user ID or movie title for personalized recommendations.
Example: Update the script to prompt for a user ID:user_id  = input("Enter User ID: ")
recommendations = get_recommendations(user_id)
print(f"Recommendations for User {user_id}:", recommendations)





Interacting with Visualizations

View Visualizations:
Open index.html in a web browser.
The page displays three charts:
Bar Chart: Average ratings by user group (2010–2020).
Line Chart: Rating trends over time.
Pie Chart: Movie popularity distribution.




Filter by User Group:
Use the dropdown to select a user group (e.g., "Young Adults") or "All Groups".
Click "Update" to refresh the charts.


Explore Data:
Hover over line chart points to see exact ratings (e.g., "Young Adults: 4.2 Stars").
Review the pie chart to see percentage-based movie popularity.


Insights:
The "Insights" section below the charts summarizes findings, such as Young Adults’ high ratings and action movie dominance.



Visualizations
Chart Types

Bar Chart: Compares average ratings across user groups for each year, ideal for highlighting group-specific preferences.
Line Chart: Shows rating trends over time, revealing how preferences evolve.
Pie Chart: Displays movie popularity proportions, identifying frequently recommended genres.

Aesthetics and Clarity

Color Scheme: Distinct colors (e.g., red for Young Adults, blue for Adults) ensure readability.
Labels and Legends: Clear titles, axis labels, and data labels (e.g., percentages on pie chart) enhance understanding.
Design: White chart containers with shadows and rounded corners provide a modern, clean look.

Interactivity

Group Filter: Dropdown to filter charts by user group or view all groups.
Tooltips: Hover on line chart points to display ratings (e.g., "Seniors: 4.2 Stars").
Responsive Design: Charts adapt to different screen sizes.

Data Storytelling
The visualizations narrate the recommendation system’s performance:

Bar Chart: Young Adults consistently rate movies highest (peaking at 4.2 in 2018), indicating strong engagement with recommended content.
Line Chart: Seniors’ ratings increase steadily, suggesting growing trust in the system over time.
Pie Chart: Action movies dominate recommendations (40%), highlighting a potential bias toward popular genres, which could inform algorithm tweaks for diversity.

Dataset

Recommendation Data: movies.csv contains user ratings for movies (1–5 scale), used by recommendation.py.
Visualization Data: data.json includes:
Average ratings for three user groups (Young Adults, Adults, Seniors) from 2010 to 2020.
Movie popularity counts for five movies (e.g., Action Movie: 400 recommendations).


Validation: Ratings are capped at 5, and popularity counts reflect recommendation frequencies. Data is verified for consistency.

Customizing Visualizations
To use real data from movies.csv:

Preprocess movies.csv to generate a JSON file with the same structure as data.json:import pandas as pd
df = pd.read_csv('movies.csv')
# Example: Group ratings by user demographics and years
grouped_data = df.groupby(['year', 'user_group'])['rating'].mean().unstack().to_dict()
# Save as JSON
import json
with open('data.json', 'w') as f:
    json.dump({'years': list(range(2010, 2021)), 'groups': grouped_data}, f)


Update index.html to load data.json dynamically:fetch('data.json').then(response => response.json()).then(data => {
    // Use data for charts
});


Adjust movie popularity data based on recommendation outputs from recommendation.py.

Tools Used

Python: For the recommendation system (recommendation.py).
Pandas/NumPy/Scikit-learn: For data processing and similarity computations.
Chart.js: For interactive visualizations (index.html).
HTML/CSS/JavaScript: For webpage structure and styling.


This project is made by our TEAM : "DATA SURFERS",
 Vani Gupta (23SCSE1010474),
 Harsh Jaiswal (23SCSE1011377),
 Shubh Kulshrestha (23SCSE1010443).