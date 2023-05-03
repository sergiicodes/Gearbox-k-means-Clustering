import pandas as pd

location = r"kNeighborGBX.xlsx"
excel = pd.read_excel(location)

df = pd.DataFrame(excel)

mod_col = df.iloc[:,0].dropna()
eff_col = df.iloc[:,2].dropna()
premium_col = df.iloc[:,4].dropna()

# Calculate mode and occurrence count for each column
columns = ['GBX for Price-Moderate:','GBX for Price-Efficient:','GBX for Price-Premium:']
for column in columns:
    col = df[column].dropna()
    first_three_letters_mode = col.astype(str).str[:3].mode()
    mode_count = col.astype(str).str[:3].value_counts().max()

    print("Most common gearbox brand in",column, first_three_letters_mode[0])
    print("Occurrence count:", mode_count)
    print()
