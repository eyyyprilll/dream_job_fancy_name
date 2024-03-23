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

# Define the main function to interact with the user
def main():
    # Ask the user to input their name
    name = input("\033[94mEnter your name: \033[0m")
    # Ask the user to input their birthday
    birthday = input("\033[94mEnter your birthday (YYYY-MM-DD): \033[0m")
    # Ask the user to input their dream job
    dream_job = input("\033[94mEnter your dream job: \033[0m")
    # Call the print_fancy function with the provided name, birthday, and dream job
    print_fancy(name, birthday, dream_job)

# Check if the script is run directly
if __name__ == "__main__":
    # Call the main function to start the program
    main()
