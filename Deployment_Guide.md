IPL Cricket Quiz & Stats App

This is a Streamlit application for an IPL Cricket Quiz and Stats Explorer. This guide explains how to push the project to GitHub and run it using Docker.

Project Structure

Your project folder should look like this:
dataset from https://www.kaggle.com/datasets/patrickb1912/ipl-complete-dataset-20082020

.
├── IPL_Streamlit_App.py       # Your main application file
├── IPL Matches 2008-2020.csv/ # The folder containing your data
│   └── matches.csv
├── requirements.txt         # Python dependencies
├── Dockerfile               # Instructions to build the Docker image
├── docker-compose.yml       # Configuration to run the Docker container
├── .gitignore               # Files for Git to ignore
└── README.md                # This guide


Part 1: How to Upload to GitHub

Tools needed:

Git (must be installed on your computer)

A GitHub account

Step-by-Step Instructions

Create a New Repository on GitHub:

Log in to GitHub.

Click the "+" icon in the top-right corner and select "New repository".

Give it a name (e.g., ipl-streamlit-app).

Choose "Public" or "Private".

Do not initialize with a README, .gitignore, or license (since we are adding our own).

Click "Create repository".

Initialize Git in Your Project Folder:

Open a terminal or command prompt.

Navigate to your project's root folder (the one containing IPL_Streamlit_App.py).

Run the following command to turn your folder into a Git repository:

git init -b main


Add and Commit Your Files:

Add all your new and existing files to Git's tracking:

git add .


Commit the files with a message describing the change:

git commit -m "Initial commit of IPL Streamlit app"


Link Your Local Repo to GitHub:

On your new GitHub repository page, copy the URL from the "…or push an existing repository from the command line" section. It will look like this: https://github.com/YourUsername/ipl-streamlit-app.git

In your terminal, run this command (paste your copied URL):

git remote add origin [https://github.com/YourUsername/ipl-streamlit-app.git](https://github.com/YourUsername/ipl-streamlit-app.git)


Push Your Code to GitHub:

Finally, "push" your local files to the GitHub server:

git push -u origin main


Refresh your GitHub page. Your files should now be visible!

Part 2: How to Run with Docker

Tools needed:

Docker Desktop (must be installed and running on your computer)

Step-by-Step Instructions

Ensure Docker is Running:

Open the Docker Desktop application. You should see a green icon indicating it's running.

Build and Run the Container:

Open your terminal in the same project root folder.

Run the following command:

docker-compose up --build


What this command does:

--build: Tells Docker Compose to first build a new image based on your Dockerfile.

up: Starts the container defined in your docker-compose.yml file.

You will see a lot of output in your terminal as Docker downloads the Python image, installs your requirements, and finally starts the Streamlit server.

Access Your App:

Once it's running, open your web browser and go to:
http://localhost:8501

You should see your colorful IPL app running, served from inside the Docker container!

To Stop the Container:

Go back to your terminal and press Ctrl + C.

To remove the container, you can run:

docker-compose down
