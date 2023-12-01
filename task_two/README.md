# PySpark Data Analysis 

----

This project involves performing a series of data analysis using PySpark on inventory data. The analyses include calculating logged-in user percentages, site usage statistics, user interactions with mobile apps, and more.

---

### Tasks:

1. Calculate the daily percentage of logged-in users.
2. Identify the site with the most logged-in users.
3. Determine the share of logged-in users using a mobile app.
4. Add a new column identity_type based on specific conditions.
5. Add a new column max_order_id showing the maximum order ID for each identity_type.
6. Caculate the total number of clicks per day for selected users in a given campaign.
7. Calculate the total number of clicks per day for users not in the campaign.


### Data:

The datasets are placed under the directory `data/inventory.parquet` and `data/selected_users.parquet`


* inventory.parquet: Contains user activity and interaction data.
* selected_users.parquet: Contains a list of selected users for specific campaign analyses.


---

### Dependencies and setup:

* Python >= 3.11
* PySpark
* Pandas
* Openpyxl (for writing the results into Excel)


Install dependencies via:

```shell
$ pip install -r requirements.txt
```

---

### The output:

You can obtain the examples in `jupyter notebook` in `/notebooks/analysis.ipynb` inside the directory of the project.

Or you can run the `main.py` script that will save all of the results in separate tabs in Excel spreadsheet under the directory `data/test_results.xlsx`

```shell
$ python main.py
```

---

### Notes: 

* Adjust the paths in main.py to the location of your Parquet files.
* The script is designed for small to medium-sized datasets. Large datasets may require optimization.

