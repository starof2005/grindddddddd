import json
import pandas as pd

# 1. Load JSON data
with open('chewdata.json', 'r') as f:
    data = json.load(f)

# 2. Convert to DataFrame
df = pd.DataFrame(data)

# 3. Save as CSV
df.to_csv('chewdata.csv', index=False)

print("✅ Converted JSON to CSV!")
