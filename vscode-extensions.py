import os
import shutil


with open("extensions_list.txt", "r") as extensions:
    extension_ids = extensions.read().splitlines()

for extension in extension_ids:
    os.system(f"code --install-extension {extension}")

# Define the source path
src_file = "settings.json"

# Get the value of the USERPROFILE environment variable
user_profile = os.environ["USERPROFILE"]

# Extract the computer name from the user profile path
computer_name = os.path.basename(user_profile)

# Construct the path to the destination file
dst_file = os.path.join(user_profile, "AppData/Roaming/Code/User/settings.json")

if os.path.exists(dst_file):
    os.remove(dst_file)

# Copy/Replace the new file to the destination
shutil.copy(src_file, dst_file)
