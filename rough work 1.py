# Initialize the chatbot
print("Electricity Usage Notification Bot")
print("Enter 'quit' to exit")

# Loop to interact with the user
while True:
    # Get the electricity usage from the user
    usage = input("Enter your current electricity usage: ")

    # Check if the user wants to quit
    if usage == 'quit':
        break

    # Convert the usage to a number
    usage = float(usage)

    # Check if the usage is excessive
    if usage > 1000:
        print("Warning: Excessive electricity usage detected.")
    else:
        print("Usage is within normal range.")

# End the chatbot
print("Goodbye!")
        