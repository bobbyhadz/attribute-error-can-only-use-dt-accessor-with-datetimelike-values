# AttributeError: Can only use .dt accessor with datetimelike values

import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bobby', 'Carl', 'Dan'],
    'salary': [175.1, 180.2, 190.3, 205.4],
    'date': ['2023-01-05', '2023-03-25', '2021-01-24', '2022-01-29']
})

df['date'] = pd.to_datetime(df['date'], errors='coerce')

print(df['date'].dtype)  # 👉️ datetime64[ns]

print(df['date'].dt.year)