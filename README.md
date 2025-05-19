Recommendation System Project
Overview
This project implements the data preprocessing and exploratory data analysis (EDA) for a recommendation system using the MovieLens dataset. The goal is to clean the data, select relevant features, transform the data, and provide initial insights through visualizations and summary statistics.
Repository Structure

src/main.py: Main Python script for data preprocessing and EDA.
plots/: Directory containing EDA visualizations (e.g., rating distribution, ratings per user/item).
movielens_ratings.csv: Sample dataset (replace with actual MovieLens dataset).
README.md: Project documentation.
presentation.tex: LaTeX file for presentation slides.
requirements.txt: List of Python dependencies.
.gitignore: Git ignore file for excluding unnecessary files.

Requirements

Python 3.8+
Libraries: pandas, numpy, matplotlib, seaborn, scikit-learn
Install dependencies:pip install -r requirements.txt



How to Run

Clone the repository:git clone https://github.com/harshjaiswal848/Recommendation_System.git
cd Recommendation_System


Install dependencies:pip install -r requirements.txt


Place the dataset (movielens_ratings.csv) in the root directory.
Run the main script:python src/main.py


Check the plots/ directory for EDA visualizations.

Dataset
The project uses the MovieLens dataset (example columns: user_id, item_id, rating, timestamp). Ensure the dataset is in CSV format and placed in the root directory.
Outputs

Cleaned and transformed dataset (in-memory, can be saved as CSV).
EDA visualizations in plots/:
rating_distribution.png: Histogram of ratings.
ratings_per_user.png: Histogram of ratings per user.
ratings_per_item.png: Histogram of ratings per item.


Console output with summary statistics and preprocessing steps.
Presentation slides compiled from presentation.tex (requires LaTeX).

Presentation
Compile presentation.tex using PDFLaTeX to generate the presentation PDF:
pdflatex presentation.tex

Ensure the plots/ directory contains the visualizations before compiling.

This project is made by our TEAM : "DATA SURFERS"
 Vani Gupta (23SCSE1010474)
 Harsh Jaiswal (23SCSE1011377)
 Shubh Kulshrestha (23SCSE1010443)