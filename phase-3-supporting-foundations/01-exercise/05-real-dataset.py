import pandas as pd

url = "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins.csv"

penguins = pd.read_csv(url)
head_penguins = penguins.head()
print(head_penguins)
print("\n")
penguins.info()

# remove missing values
clean_penguins = penguins.dropna()
head_clean_penguins = clean_penguins.head()
print("\n")
print(head_clean_penguins)
print("\n")
clean_penguins.info()

# describe
print("\n")
describe_clean_penguins = clean_penguins.describe()
print(describe_clean_penguins)


# find mean of body_mass_g
mean_body_mass_g = clean_penguins.groupby("species")["body_mass_g"].mean()
print("\n")
print("Mean of body_mass_g:", mean_body_mass_g)


