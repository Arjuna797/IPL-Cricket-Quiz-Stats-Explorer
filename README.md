🏏 IPL Cricket Quiz & Stats Explorer

This is a web application built with Streamlit that provides an interactive IPL (Indian Premier League) quiz and a data explorer for match statistics from 2008-2020. The app features a custom, colorful, animated UI with a frosted-glass effect.

✨ Features

Interactive Cricket Quiz: Test your IPL knowledge with randomly generated questions about match winners, stadiums, and "Player of the Match" awards.

Stats Explorer: Visualize historical IPL data, including:

Top 10 most used stadiums

Top 10 "Player of the Match" winners

Total wins per team

Custom Interface: A dynamic, animated gradient background with an IPL logo watermark and modern frosted-glass containers for content.

📂 Project Structure

To run this project, your folder should be organized as follows:

.
├──  cricket_app.py           # Your main Streamlit application file
├── IPL Matches 2008-2020.csv/ # Folder containing the dataset
│   └── matches.csv
├── requirements.txt         # Python dependencies
├── Dockerfile               # Instructions to build the Docker image
├── docker-compose.yml       # Configuration to run the Docker container
├── .gitignore               # Files and folders for Git to ignore
└── README.md                # This file
Use the appropriate command based on your operating system:

```bash
# On Ubuntu / Linux
docker-compose up -d

# On Windows
docker compose up -d



🚀 How to Run

There are two primary ways to run this application: locally on your machine or inside a Docker container.

1. Run Locally

Prerequisites:

Python 3.8+

pip (Python package installer)

Steps:

Clone the repository (or download the files):

git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git)
cd YOUR_REPOSITORY


Install the required Python packages:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run cricket_app.py


Open your web browser and navigate to the "Local URL" shown in your terminal (usually http://localhost:8501).

2. Run with Docker (Recommended)

This is the easiest way to run the app with all its dependencies managed in a self-contained environment.

Prerequisites:

Docker Desktop (must be installed and running)

Steps:

Build and start the container:

Make sure you are in the project's root directory (where docker-compose.yml is located).

Run the following command in your terminal:

docker-compose up --build


This command will build the Docker image based on the Dockerfile and then start the container.

Access the application:

Once the build is complete and the container is running, open your web browser and go to:
http://localhost:8501

To stop the application:

Press Ctrl + C in your terminal.

To remove the container, you can run docker-compose down.

💾 Data

This application requires the matches.csv file from the IPL Matches 2008-2020 dataset.

You must place the matches.csv file inside a folder named IPL Matches 2008-2020.csv in the root of the project directory for the app to find it.

⬆️ How to Upload to GitHub

Initialize Git:

git init -b main


Add all files:

git add .


Make your first commit:

git commit -m "Initial commit: Add IPL Streamlit app and Docker files"


Link to your GitHub repository:

git remote add origin [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git)


Push your code:

git push -u origin main
