# Book Recommendation System

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Data Description](#data-description)
- [Recommendation Methods](#recommendation-methods)
- [Web Application](#web-application)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)



## Overview

The Book Recommendation System is a research-driven project aimed at exploring various recommendation algorithms to evaluate their performance, strengths, and weaknesses. The objective is to identify the most effective methods for providing personalized book recommendations. Our findings are presented through a comprehensive web application that not only details the methodologies and results of our research but also offers an interactive demo where users can experience the recommendation system in action. This project serves as a valuable resource for understanding the intricacies of recommendation systems and their practical applications in enhancing user experience in book discovery.


## Features

- **Home Page**: Provides an overview of the system and its functionalities.
- **About Page**: Offers information about the project, its goals, and the team behind it.
- **Methods Page**: Explains the different recommendation algorithms explored in the project.
- **Demo Page**: Interactive demonstration of the recommendation system:
  - **Trends**: Displays trending books based on overall popularity.
  - **Personalized**: Offers personalized book recommendations based on user input.
  - **User-specific**: Personalized recommendations for registered users based on their reading history.
- **Contact Page**: Contains information on how to reach the project team for inquiries or feedback.

## Installation

To set up the Book Recommendation System on your local machine, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/BookRecommendationSystem.git

2. Navigate to the project directory:
   ```sh
   cd BookRecommendationSystem

## Usage

1. Run the Flask Application
   ```sh
   python app.py

2. Open your web browser and navigate to http://127.0.0.1:5000.


## Project Structure

  * app.py: The main file for running the Flask application.
  * model.py: Contains the model class and essential functions for generating recommendations.
  * templates/: Directory containing all HTML templates.
    * index.html: Home page template.
    * about.html: About page template.
    * methods.html: Methods page template.
    * trends.html: Trends page template.
    * personalized.html: Personalized recommendations page template.
    * user.html: User-specific recommendations page template.
    * contact.html: Contact page template.
  * static/: Directory containing CSS, JavaScript, and image files.
    * css/: Contains CSS files for styling.
    * js/: Contains JavaScript files.
    * images/: Contains image files used in the application.
  * requirements.txt: List of dependencies required to run the project.
  * README.md: This file.

## Data Description
The dataset used in this project includes book ratings from various users. The key fields are:

* User-ID: Unique identifier for each user.
* Age: Age of the user.
* Country: Country of the user.
* ISBN: Unique identifier for each book.
* Book-Rating: Rating given by the user to the book.
* Avg_Rating: Average rating of the book.
* Total_No_Of_Users_Rated: Total number of users who have rated the book.
* Book-Title: Title of the book.
* Book-Author: Author of the book.
* Year-Of-Publication: Year the book was published.
* Publisher: Publisher of the book.

## Recommendation Methods
The system explores and implements various recommendation algorithms, including:

* **Collaborative Filtering**: Utilizes user-item interactions to generate recommendations.
  * **User-based Collaborative Filtering**: Finds similarities between users and recommends books liked by similar users.
  * **Item-based Collaborative Filtering**: Finds similarities between items and recommends books similar to those a user has liked.
* **Matrix Factorization**: Decomposes the user-item interaction matrix to discover latent factors.
  * **SVD (Singular Value Decomposition)**: Reduces the dimensionality of the user-item matrix to predict ratings.
  * **NMF (Non-negative Matrix Factorization)**: Factorizes the matrix into non-negative factors to make recommendations.


## Web Application
The web application is built using Flask and provides the following routes:

* / (index): The home page of the application.
* /about: The about page providing information about the project.
* /methods: The methods page detailing the recommendation algorithms used.
* /demo/trends: The demo page showcasing trending books.
* /demo/personalized: The demo page for personalized book recommendations.
* /demo/personalized/<user_id>: The demo page for user-specific recommendations.
* /contact: The contact page for user inquiries and feedback.

## Backend Integration
* app.py: Defines the routes and handles the HTTP requests and responses.
* model.py: Implements the recommendation algorithms and provides functions to fetch and process data.

## **Frontend Integration**
* **HTML Templates**: Located in the templates/ directory, these files define the structure of the web pages.
* **CSS and JavaScript**: Located in the static/ directory, these files handle the styling and interactivity of the web pages.

## Images
Here are some screeshots of the web application.

<img src="/images/home.jpeg">
<img src="/images/methods.jpeg">
<img src="/images/trends.jpeg">
<img src="/images/1.png">
<img src="/images/2.png">

## Contributing
We welcome contributions to the project. If you would like to contribute, please follow these steps:

* Fork the repository.
* Create a new branch for your feature or bugfix.
* Commit your changes and push them to your branch.
* Create a pull request with a detailed description of your changes.


## Contact
For any questions or inquiries, please reach out to rohitkrtiwari2002@gmail.com.

