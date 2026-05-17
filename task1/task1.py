def total_salary(path):
    total_salary_sum = 0
    developers_count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                name, salary = line.strip().split(",")
                total_salary_sum += float(salary)
                developers_count += 1

        average_salary =(total_salary_sum / developers_count)

        return round(total_salary_sum, 2), round(average_salary, 2) 
    except ZeroDivisionError:
        print("Chance of division by zero. No developers found.")
        return 0, 0

    except FileNotFoundError:
        print("No such file")
        return 0, 0

    except ValueError:
        print("Please check the file format. Each line should contain a name and a salary separated by a comma.")
        return 0, 0


total, average = total_salary("task1/salary_file.txt")

print(f"Total salary: {total}")
print(f"Average salary: {average}")