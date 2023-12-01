## Currency Conversion Solution

----

### Overview:

This solution automates the process of converting budget amounts in a CSV file from EUR to various local currencies. It fetches current exchange rates from an API and applies these rates to the specified amounts. The output is a CSV file with the converted currency values.

----

### Setup:

----

_Without Docker:_

#### Prerequisites

* Python >= 3.8 on your system
* Required Python packages: Install them using `pip install -r requirements.txt`


To run the script directly, use the following command in the project's root directory:

```shell
python main.py path/to/input.csv path/to/output.csv
```

Replace `path/to/input.csv` with the path to your input CSV file and `path/to/output.csv` with the desired path for the output file.

---

_With Docker:_

Building the Docker Image
Navigate to the directory containing the Dockerfile and run the following command to build the Docker image:

```shell
docker build -t currency-converter-app .
```

This command creates a Docker image named `currency-converter-app`

Running the Container
Run the container using the command:

```shell
docker run -v /path/to/data:/data currency-converter-app /data/input.csv /data/output.csv
```

Replace `/path/to/data` with the directory containing your input CSV file and where you want the output CSV file to be saved.

----

### Examples:

_Running Without Docker:_

Assuming you have an input file named `input.csv` in your current directory and want to save the output as `output.csv` in the same directory:

```python
python main.py ./input.csv ./output.csv
```

```shell
python main.py data/raw/sales_report_input.csv data/preprocessed/test_file.csv
```

_Running With Docker:_

**Example 1: Default File Paths**

For an `input.csv` in your current directory and saving the output as `output.csv` in the same directory:

```shell
docker run -v $(pwd):/data currency-converter-app /data/input.csv /data/output.csv
```

**Example 2: Custom File Paths**

Using custom file names or directories:

```shell
docker run -v /path/to/myfiles:/data currency-converter-app /data/my_custom_input.csv /data/my_custom_output.csv
```

Replace `/path/to/myfiles` with your desired directory, `my_custom_input.csv` with your input file name, and `my_custom_output.csv` with your output file name.

---

### Output:

The output is a CSV file containing the original data along with an additional column for the converted budget values in the specified local currency.

----

### Additional Information

Ensure your input CSV file follows the expected format with the necessary columns.


