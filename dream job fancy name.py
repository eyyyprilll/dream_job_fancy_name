# Define a function to print the formatted dream job information
def print_fancy(name, birthday, dream_job):
    # Define the header for the fancy output
    header = "*****************************"
    # Define the content with formatted strings for name, birthday, and dream_job
    content = [
        f"* Name: {name.ljust(26)} *",
        f"* Birthday: {birthday.ljust(22)} *",
        f"* Dream Job: {dream_job.ljust(19)} *"
    ]
    # Print the header in bold and magenta color
    print("\033[1m\033[95m" + header)
    # Iterate over each line in the content and print it
    for line in content:
        print(line)
    # Print the footer of the fancy output
    print(header + "\033[0m")


