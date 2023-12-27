#Student_ID = 21041604
#Task 1b = Filter for and remove any dud records where there is no value for SiteID or there is a mismatch between SiteID and Location.

#Importing Pandas Library to perform this task.
import pandas as pd

#Code written in try-except construct as good practice of coding.
try:

#To read the new crop file created from task 1a and set the Date Time format
    clean_data = pd.read_csv("crop.csv", delimiter =',', low_memory=False)
    clean_data['Date Time']  = pd.to_datetime(clean_data['Date Time'])
    clean_data['Data Time'] = pd.to_datetime(clean_data['Date Time'], format="%d %b %Y %H")

#To find the mismatch between the SiteID and Location and the dud records
    mismatch = clean_data.index[((clean_data.SiteID == 452) & (clean_data.Location != 'AURN St Pauls'))|
                              ((clean_data.SiteID == 215) & (clean_data.Location != 'Parson Street School'))|
                              ((clean_data.SiteID == 270) & (clean_data.Location != 'Wells Road'))|
                              ((clean_data.SiteID == 203) & (clean_data.Location != 'Brislington Depot'))|
                              ((clean_data.SiteID == 463) & (clean_data.Location != 'Fishponds Road'))|
                              ((clean_data.SiteID == 206) & (clean_data.Location != 'Rupert Street'))|
                              ((clean_data.SiteID == 375) & (clean_data.Location != 'Newfoundland Road Police Station'))|
                              ((clean_data.SiteID == 500) & (clean_data.Location != 'Temple Way'))|
                              ((clean_data.SiteID == 447) & (clean_data.Location != 'Bath Road'))|
                              ((clean_data.SiteID == 395) & (clean_data.Location != "Shiner's Garage"))|
                              ((clean_data.SiteID == 501) & (clean_data.Location != 'Colston Avenue'))|
                              ((clean_data.SiteID == 213) & (clean_data.Location != 'Old Market'))|
                              ((clean_data.SiteID == 481) & (clean_data.Location != 'CREATE Centre Roof'))|
                              ((clean_data.SiteID == 459) & (clean_data.Location != 'Cheltenham Road \ Station Road'))|
                              ((clean_data.SiteID == 573))|
                              ((clean_data.SiteID.isna()))].tolist()        
    print("Number of mismatches found = ", len(mismatch))

#To delete the dud records from the dataset
    clean_data.drop((mismatch), axis=0, inplace=True)  

#To delete the dud records from the crop data file and create a new clean.csv file
    clean_data.to_csv("clean.csv", index=False)                   
    print("After deleting the mismatches, ", clean_data.shape[0], "lines has been transfered to clean.csv")

except BaseException as err:
        print(f"An error in the Code: {err}")