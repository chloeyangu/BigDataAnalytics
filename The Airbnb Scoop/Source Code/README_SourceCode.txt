######################
### DATA AND CODES ###
######################

The raw data downloaded from Inside Airbnb consists of the following files: 
1. reviews.csv
2. listings_new.csv

The raw data crawled from Tripadvisor consists of the following files:
1. barcelona_attractions.csv [1. Tripadvisor Web Crawling.ipynb]


The preprocessing steps consists of 3 files:
1. listings_31Mar.csv [2. Data Preparation Part 1 (Listings).ipynb]
	- Conversion to numeric variables
	- Dummy variables for amenities
	- Join data of attractions with listings
2. preprocessed_data_1_Apr.csv [3. Data Preparation Part 2 (Listings).ipynb]
	- Convert categorical string variables to dummy variables
	- Drop unnecessary columns for linear regression and classification
3. reviews_27Mar.csv [4. Data Preparation Part 3 (Reviews).ipynb]
	- Translate Non-English reviews to English 
	- Only first 10 reviews translation is shown in the output as it took many hours for the code to run


Data Analysis consists of 2 iPython Notebook files:
1. [5. Data Analysis - Linear Regression and Classification.ipynb]
2. [6. Data Analysis - Sentiment Analysis]

################
### DATABASE ###
################

To create the database, go to terminal and type the following:
sudo chown -R `id -u` /data/airbnb
mongod

Open a new terminal and type the following to see the database:
mongo
show dbs
use airbnb

To insert the data into the database, open a new terminal and type the following:
mongoimport --db airbnb --type csv --file listings_new.csv -c listings_new
mongoimport --db airbnb --type csv --file barcelona_attractions.csv -c attractions
mongoimport --db airbnb --type csv --file listings_31Mar.csv --headerline -c Rawdata
mongoimport --db airbnb --type csv --file reviews.csv --headerline -c reviews
mongoimport --db airbnb --type csv --file preprocessed_data_1_Apr.csv --headerline -c Listing
mongoimport --db airbnb --type csv --file reviews_27Mar.csv -c reviews


#################################
### INSTALL PACKAGES (PYTHON) ###
#################################

For web crawling using Selenium:
	- Install web driver from: https://sites.google.com/a/chromium.org/chromedriver/downloads

pip install pymongo
pip install -U scikit-learn
git clone git://github.com/statsmodels/statsmodels.git
pip install numpy
pip install pandas
pip install matplotlib
pip install seaborn
pip install ipython
pip install pydotplus
pip install -U textblob
pip install https://pypi.python.org/packages/source/a/afinn/afinn-0.0.1rc1.tar.gz
pip install beautifulsoup4
pip install requests
pip install -U selenium

