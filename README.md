mochiolive happy hour

NOTE: run requirements.txt to install all required python packages by running the following command:
        pip install -r requirements.txt

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

