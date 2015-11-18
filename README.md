mochiolive happy hour

NOTE: run requirements.txt to install all required python packages by running the following command:
        pip install -r requirements.txt
Please re-run to enable twitter sign in

TODO: For testing locally, the web-url and call back for twitter is pointed to 127.0.0.1:8000
Need to change this in times of deployment

#### API Endpoints: 
- Adding a restaurant and getting all restaurants: 
GET, POST: <host url>/v1/restaurants/

- Relating to individual restaurants specified by primary key: 
GET, PUT, DELETE: <host url>/v1/restaurants/<primary key>/


#### Yelp Client Usage

- Step 1: Instantiate 
        Example: client = YelpClient()

- Step 2: get data
        Example: data = client.get_all_sets(keys, 200) 
        Note: 200 in the example in the number of data points you want to get


#### admin info:
you can access the login page via the url: http://127.0.0.1:8000/login/admin

the username is: mochiolive_admin; 
pass: m0chi0live. 

after successful login, it will redirect you to the page: http://127.0.0.1:8000/admin/dashboard/

