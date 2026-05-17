def get_cats_info(path):
    cats_info = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                cat_id, name, age = line.strip().split(",")

                cat = {
                    "id": cat_id,
                    "name": name,
                    "age": round(float(age), 2)
                }

                cats_info.append(cat)

        return cats_info

    except FileNotFoundError:
        print("Please check the file.")
        return []

    except ValueError:
        print("Please check the format of the data in the file.")
        return []

cats_info = get_cats_info("task2/cats_file.txt")
print(cats_info)