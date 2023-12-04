from tabulate import tabulate
import solutions.year2023.day1.solution
import solutions.year2023.day2.solution
import solutions.year2023.day3.solution
import solutions.year2023.day4.solution

headers = ["Day", "Part", "Answer", "Time (ms)"]
data = solutions.year2023.day1.solution.timings + \
       solutions.year2023.day2.solution.timings + \
       solutions.year2023.day3.solution.timings + \
       solutions.year2023.day4.solution.timings


total = 0
for time in data:
    if time[1] == "Part 1" or time[1] == "Part 2":
        total += time[3]
    time[3] = round(time[3] * 1000, 3)

table = tabulate(data, headers, tablefmt="github")

with open("README.md", "r+", encoding="utf8") as f:
    old = f.read()  # read everything in the file
    f.seek(0)
    readme_text = old.split("## Timing")[0]
    readme_text += "## Timing\n" + table + "\n\n" + "Total time (For only submitted stars): " + str(
        round(total, 3)) + " second(s)                "
    f.write(readme_text)
