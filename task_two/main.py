from utils.analytics_scripts import *
import pandas as pd
import warnings


def main():
    warnings.filterwarnings("ignore")
    # FYI: Only for the local session not the cluster calculations
    spark = init_spark_session()

    inventory_df, selected_users_df = load_data(spark, "data/inventory.parquet",
                                                "data/selected_users.parquet")

    # Tasks:
    task1_result = calculate_logged_in_percentage(inventory_df).toPandas()
    task2_result = site_with_most_logged_in_users(inventory_df).toPandas()
    task3_result = share_of_logged_in_users_using_mobile_app(inventory_df)

    inventory_df = add_identity_type_column(inventory_df)
    inventory_df = add_max_order_id_column(inventory_df)

    task6_result = clicks_per_day_for_selected_users(inventory_df, selected_users_df).toPandas()
    task7_result = clicks_per_day_for_non_selected_users(inventory_df, selected_users_df).toPandas()

    with pd.ExcelWriter('data/task_results.xlsx', engine='openpyxl') as writer:
        task1_result.to_excel(writer, sheet_name='Task 1')
        task2_result.to_excel(writer, sheet_name='Task 2')
        pd.DataFrame({'Task 3 Share': [task3_result]}).to_excel(writer, sheet_name='Task 3')
        inventory_df.toPandas().to_excel(writer, sheet_name='Tasks 4 and 5')
        task6_result.to_excel(writer, sheet_name='Task 6')
        task7_result.to_excel(writer, sheet_name='Task 7')

    spark.stop()


if __name__ == "__main__":
    main()
