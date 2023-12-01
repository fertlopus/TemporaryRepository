from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, count, max as max_, lit


def init_spark_session():
    """ Initialize and return a Spark session """
    return SparkSession.builder.appName("Inventory Analysis").getOrCreate()


def load_data(spark, inventory_path, users_path):
    """ Load data into Spark DataFrames """
    inventory_df = spark.read.parquet(inventory_path)
    selected_users_df = spark.read.parquet(users_path)
    return inventory_df, selected_users_df


def calculate_logged_in_percentage(df):
    """ Task 1: Calculate the percentage of logged-in users per day """
    return df.groupBy("date").agg(
        (count(when(col("is_logged_in"), 1)) / count("*") * 100).alias("logged_in_percentage")
    )


def site_with_most_logged_in_users(df):
    """ Task 2: Find which site has the most logged in users """
    return df.filter(col("is_logged_in")).groupBy("site").count().orderBy(col("count").desc()).limit(1)


def share_of_logged_in_users_using_mobile_app(df):
    """ Task 3: Calculate the share of logged-in users who are using Mobile App """
    total_logged_in = df.filter(col("is_logged_in")).count()
    mobile_app_logged_in = df.filter(col("is_logged_in") & col("is_mobile_app")).count()
    return mobile_app_logged_in / total_logged_in * 100


def add_identity_type_column(df):
    """ Task 4: Add identity_type column based on conditions """
    return df.withColumn(
        "identity_type",
        when((col("device_type") == "Mobile Phone") & (col("is_mobile_app")), "Mobile Phone App")
        .when((col("device_type") == "Mobile Phone") & (~col("is_mobile_app")), "Mobile Phone Web")
        .when(col("device_type") == "Desktop", "Desktop")
        .otherwise("Unknown")
    )


def add_max_order_id_column(df):
    """ Task 5: Add max_order_id column for each identity_type """
    max_order_id = df.groupBy("identity_type").agg(max_("order_id").alias("max_order_id"))
    return df.join(max_order_id, "identity_type")


def clicks_per_day_for_selected_users(df, selected_users_df):
    """ Task 6: Calculate total number of clicks per day for selected users """
    return df.join(selected_users_df, "user_id").filter(col("event") == "click").groupBy("date").count()


def clicks_per_day_for_non_selected_users(df, selected_users_df):
    """ Task 7: Calculate total number of clicks per day for non-selected users """
    return df.join(selected_users_df, "user_id", "left_anti").filter(col("event") == "click").groupBy("date").count()
