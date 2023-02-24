import os
import shutil

# NEW_NAME = "xyz"

#    # Read directories from txt file and clean them
lines = open("download_and_end_folders.txt", "r").readlines()
modified = []
for line in lines:
    if line[-1] == "\n":
        modified.append(line[:-1])
    else:
        modified.append(line)

# assign source and destination folder
download_folder = modified[1]
destination_folder = modified[4]
origin_folder = modified[7]


def move_csv(name: str):
    try:
        os.chdir(download_folder)
        os.rename("QUEST 3 Product Search.csv", f"{name}.csv")
        shutil.move(f"{name}.csv", destination_folder)
    except FileNotFoundError:
        pass

    os.chdir(origin_folder)


# if __name__ == "__main__":
#     move_csv(NEW_NAME)
#     print(os.chdir)
