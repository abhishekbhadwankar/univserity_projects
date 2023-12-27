#Student_ID = 21041604
#Task 1a = Crop the file to delete any records before 00:00 1 Jan 2010 (1262304000)

#Importing Pandas Library to perform this task.

import pandas as pd
#Code written in try-except construct as good practice of coding. 

try:
#To read the data and storing it into data variable for further processing.
    data = pd.read_csv("bristol-air-quality-data.csv", delimiter =';', low_memory=False)

#To Filter data with any date before "00:00 1 Jan 2010".
    crop_data = data.loc[(data['Date Time'] > '2010')]

#To copy the filtered data into a new file "crop.csv"
    crop_data.to_csv("crop.csv", index=False)
    print("The number of lines after filter are =", crop_data.shape[0], "  These lines are transfered to crop.csv")
    
        
except BaseException as err:
        print(f"An error in the Code: {err}")

