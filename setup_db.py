import urllib.request
import zipfile
import os

# URL for the Chinook SQLite database
url = "https://www.sqlitetutorial.net/wp-content/uploads/2018/03/chinook.zip"
zip_path = "chinook.zip"
db_name = "chinook.db"

print("Downloading Chinook database... Please wait.")
urllib.request.urlretrieve(url, zip_path)

print("Extracting database...")
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(".")

# The zip usually contains a file named 'chinook.db'
# We make sure it is in our root folder
if os.path.exists(db_name):
    print(f"✅ Success! '{db_name}' is ready in your folder.")
else:
    print("❌ Something went wrong. Check if the file was extracted.")

# Clean up the zip file
os.remove(zip_path)