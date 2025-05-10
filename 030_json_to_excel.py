import pandas as pd
import json
with open("029_data.json", "r") as file:
    data = json.load(file)

    df = pd.DataFrame(data)

    df.to_excel("031_data.xlsx", index=False)

    print("conversion successful.Excel file '031_data.xlsx' created")
