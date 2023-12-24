import pandas as pd
import os

folder_path = r"/Users/ahmed/Documents/Self/FST/s/tst_csv"
def create_one_empty_table(file_name, num_days, times_taken, start_time=0, end_time=24, step=0.5):
    time = start_time
    cols_names = []

    # Create column names
    while time <= end_time:
        cols_names.append(str(time))  # Convert to string without decimal part
        time += step

    # Create an empty DataFrame with columns
    df = pd.DataFrame(columns=cols_names)

    # Create rows and set values based on times_taken
    for day in range(num_days):
        row_data = [0] * len(cols_names)  # Initialize the row with zeros

        # Set values in columns specified by times_taken for the current day
        for times in times_taken[day]:
            col_index = int( times/ 0.5 )# Convert to string without decimal part
            row_data[col_index] = 1

        # Add the row to the DataFrame
        df.loc[len(df)] = row_data

    # Save the DataFrame to a CSV file
    df.to_csv(os.path.join(folder_path, f'{file_name}.csv'), index=False)

# Example usage:


    
def create_mul_tables():
    create_one_empty_table("first", 3, [[8, 8.5, 9, 9.5, 10, 10.5, 12, 12.5], [], [8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15]])
    create_one_empty_table("second", 3, [[], [], [8, 8.5, 9, 9.5, 10]])
    create_one_empty_table("third", 3, [[], [], [8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 15, 15.5]])

create_mul_tables()