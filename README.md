# Recipe Heaven

For this project, I am to build a Full-stack site that allows users to manage a common dataset about a particular domain.

I have created a site that allows users to create store edit and delete cooking recipes that can be used to inspire.

## UX

The site is aimed at cooking enthusiast of all levels that want to backup hand written recipes that could be miss placed or destroyed. The site will enable users to create store edit delete and share cooking recipes.

- As a user, I want to add recipes.

- As a user, I want to find recipes.

- As a user, I want to share recipes.

- As a user, I want to find new recipes.

### Wireframes

- Please find initial wireframe design for Home page, click <a href="wireframes/home-page-initial-wireframe-design.pdf">here</a>.
- Please find initial wireframe design for All recipes page, click <a href="wireframes/all-recipes-page-initial-wireframe-design.pdf">here</a>.
- Please find initial wireframe design for Add recipe page, click <a href="wireframes/add-recipe-page-initial-wireframe-design.pdf">here</a>.
- Please find initial wireframe design for Recipe page, click <a href="wireframes/recipe-page-initial-wireframe-design.pdf">here</a>.
- Please find initial wireframe design for Edit recipe page, click <a href="wireframes/edit-recipe-page-initial-wireframe-design.pdf">here</a>.

## Features

### Existing Features

Recipe Heaven is a clutter free site. The site is a five page site, broken up into home page, all recipes page, add recipe page recipe page page and an edit recipe page.

#### Home page

On this page users will be given a brief overview of the site along with recently added recipe section.

At the top of the page will be the navbar with a navbar brand link to index.html, also there will be links to all recipes page and add recipe page.
Below the navbar will be the main content section within that section, will be a jumbotron with site name and brief outline of what the site offers.
below that will be the recently added recipes section, displaying the most recent recipes added to the database.
At the very bottom will be the footer section with copyright info.

#### All Recipes page

On this page the user can view all recipes in the database.

At the top of the page will be the navbar with a navbar brand link to index.html, also there will be links to all recipes page and add recipe page.
Below the navbar will be the main content section within that section, will be the recipes displayed in a grid system.
At the very bottom will be the footer section with copyright info.

#### Add Recipes page

On this page the user will fill in the categories and submit recipe to database.

At the top of the page will be the navbar with a navbar brand link to index.html, also there will be links to all recipes page and add recipe page.
Below the navbar will be the main content section within that section, will be a form with input fields and below that is a submit button.
At the very bottom will be the footer section with copyright info.

#### Recipes page page

On this page the user can view the entire recipe from name, description, cuisine, serves, meal, prep, cooking, ingredients, directions username and last modified.

At the top of the page will be the navbar with a navbar brand link to index.html, also there will be links to all recipes page and add recipe page.
Below the navbar will be the main content section within that section, will be a form with input fields and below that is a edit recipe button and a delete button.
At the very bottom will be the footer section with copyright info.

#### Edit Recipe page

On this page the user can edit all input fields of the entire recipe from name, description, cuisine, serves, meal, prep, cooking, ingredients, directions username and last modified.

At the top of the page will be the navbar with a navbar brand link to index.html, also there will be links to all recipes page and add recipe page.
Below the navbar will be the main content section within that section, will be a form with input fields and below that is an update recipe button.
At the very bottom will be the footer section with copyright info.

### Features Left to Implement

#### Search function

A text input search function, that allows the user to search for recipes by name or ingredient.

#### Recipe image

I would also like to allow users to upload a picture to the recipe.

## Technologies Used

This project uses HTML, CSS and JavaScript programming languages.

- <a href="https://en.wikipedia.org/wiki/HTML5#References">**HTML**</a> and
  <a href="https://en.wikipedia.org/wiki/Cascading_Style_Sheets">**CSS**</a>

  - This project uses base languages used to create website

- <a href="https://en.wikipedia.org/wiki/JavaScript">**Javascript**</a>

  - This project uses Javascript for the dynamic responsive website

- <a href="https://code.visualstudio.com">**VS Code**</a>

  - This project was developed using VS Code for building the website

- <a href="https://www.python.org">**Python**</a>

  - This project uses Python to write the logic for the site

- <a href="https://flask.palletsprojects.com/en/1.1.x">**Flask**</a>

  - This project uses Flask's micro framework

- <a href="https://www.mongodb.com">**MongoDB**</a>

  - This project uses MongoDB to store data

- <a href="https://getbootstrap.com">**Bootstrap**</a>

  - This project uses Bootstrap to simplify the structure of the website and make the website responsive easily

- <a href="https://fonts.google.com">**Google Fonts**</a>

  - This project uses Google fonts to style the website fonts

- <a href="https://github.com">**GitHub**</a>

  - This project uses GitHub to store and share all project code remotely

- <a href="https://autoprefixer.github.io">**AutoPrefixer**</a>

  - The project used AutoPrefixer to make sure all css prefixes were the most up to date versions

## Testing

All code used on the site has been tested to ensure everything is working as expected

All code used on the site has been tested across multiple devices via DevTool option in Chrome.

- Pixel 2 XL, click <a href="testing/devices/rh-pixel2-xl-screen-shot.jpg">here</a> to view screen shot.
- iPhone 6/7/8, click <a href="testing/devices/rh-iphone-6-7-8-screen-shot.jpg">here</a> to view screen shot.
- iPad, click <a href="testing/devices/rh-ipad-screen-shot.jpg">here</a> to view screen shot.

Site has been viewed and tested in the following browsers:

- Google Chrome, click <a href="testing/browsers/rh-google-chrome-screen-shot.jpg">here</a> to view screen shot.
- Opera, click <a href="testing/browsers/rh-opera-screen-shot.jpg">here</a> to view screen shot.
- Microsoft Edge, click <a href="testing/browsers/rh-microsoft-edge-screen-shot.jpg">here</a> to view screen shot.
- Mozilla Firefox, click <a href="testing/browsers/rh-firefox-screen-shot.jpg">here</a> to view screen shot.
- Safari, click <a href="testing/browsers/rh-safari-screen-shot.jpg">here</a> to view screen shot.

## Deployment

Live demo can be viewed <a href="https://recipe-heaven-cookbook.herokuapp.com/">here</a>

The following steps explain how you can get the website running on heroku locally.

### Branches

For this project, there are a total of 2 branches, the master branch is the latest up to date, and the one to focus on.

- Master
- dev

### How to Clone and setup website locally

- **Clone website**

  - Go to GitHub
  - Click Repositories.
  - Locate recipe-heaven.
  - Open recipe-heaven.
  - Click the green button clone to download.
  - Or clone from URL using the following command in terminal: got clone https://github.com/juliancameron79/recipe-heaven.git

- **Installing Requirements**
  Once you have the project cloned on your computer.

  - Open the Terminal and navigate to recipe-heaven folder on your computer.
  - Install the libraries from requirements.txt by typing pip3 install -r requirements.txt

- Setting up the database keys
  Once the project is cloned, and you have the libraries installed from requirements.txt, we now must setup the database.

  - Create a python file and place it outside of the folder structure, next to app.py.
  - Inside the newly created file, you need to add information to 2 variables and 1 import.
  - At the top of the file add the following line import os.
  - Then add the following 2 lines below.
  - os.environ["Mongo_URI"] = "mongodb+srv://myRoot:MONGODB-PASSWORD@CLUSTER-NAME-96wib.mongodb.net/DATABASE-NAME?retryWrites=true&w=majority".
  - Add os.environ["MONGO_DBNAME"] = 'Your database name'.

- **Running the Project locally**
  - Run app.py
  - Paste http://0.0.0.0:5000/ into your browser.

### Deploy Recipe Heaven on Heroku

Complete the above, Clone Website before starting.

- **Setting up Heroku**

  - Create an account on Heroku.
  - Click New button, then Click Create new app.
  - Give it a name and choose your region.
  - Click Create App.
  - Find your App name on the dash board, and enter.
  - Click Settings, and locate Config Vars, and fill in like shown below (Just edit out the placeholder text).

- Key | Value
- IP | 0.0.0.0
- PORT | 5000
- MONGO_URI | mongodb+srv://myRoot:MONGODB-PASSWORD@CLUSTER-NAME-96wib.mongodb.net/DATABASE-NAME?retryWrites=true&w=majority
- MONGO_DBNAME Name of the database

- If the Procfile is missing, preform the following command in your terminal echo web: python3 run.py > Procfile
- If the requirements.txt is missing, preform the following command in your terminal pip3 freeze > requirements.txt

- **Deploy to Heroku**
  - In your Terminal type heroku login.
  - Then git push heroku master.
  - Open Heroku website.
  - Navigate to the app (Recipe Heaven), and click on Open App.

## Credits

### Content

- Recipes taken from allrecipes website.

### Media

- The background image used was sourced from Pexels.

### Code

### Acknowledgements

I had trouble with the deployment section write up but lucky I found <a href="https://github.com/Pyleks/Milestone-Project-3">pyleks</a>that helped me.

I got lots of inspiration from watching is video <a href="https://www.youtube.com/watch?v=CxohCB9Q_GA">Recipe Database Project - Python / Flask</a>

#### Disclaimer

The content of this website, including the images used, are for educational purposes only.
