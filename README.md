### Project Title: MochiOlive Happy Hour (MOHH)

#### Demo
[Demo](http://ec2-54-213-123-63.us-west-2.compute.amazonaws.com:8000/)

Our web application allows Vancouverites to locate establishments in the city that offer "Happy Hours", which are specific times in the week or day when restaurants or bars offer discounted food and beverages.

To achieve this functionality, we intend to provide the web app's users with a map that plots the locations of these happy hour establishments as well as a table that displays their name, ratings, and other attributes. The data for the restaurants or bars will come from the Yelp API. In addition, we will implement a sign-in system that allows the user to log into our app through their Twitter account or an account they can create in the app. By signing into their account, the user will be able to save their favourite happy hour places in a list and tweet about their happy hour experience through our app.

We will also store user information as well as data regarding happy hour establishments (which we retrieved from the Yelp API) into a database. Furthermore, the admin of the app can ensure that the data is up to date by clicking a “retrieve latest data” button on an admin dashboard.

mochiolive happy hour

NOTE: run requirements.txt to install all required python packages by running the following command:
        pip install -r requirements.txt
Please re-run to enable twitter sign in

TODO: For testing locally, the web-url and call back for twitter is pointed to 127.0.0.1:8000
Need to change this in times of deployment

#### API Endpoints: 
- Refer to: https://github.com/CPSC310-2015W1/MochiOlive/wiki/RESTful-Design-Principle-Incorporation

