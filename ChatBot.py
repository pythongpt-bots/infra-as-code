import openai  # Assuming you have the OpenAI Python library installed

# Define your OpenAI API key
openai.api_key = 'sk-qpdvzMLJ8lK6QiXj9yUUJ2A0yuZ6NKHuqaEJL1OqFGG5EvyW'

def chat_with_user():
    print("Welcome to the Infrastructure as Code (IAC) template generator!")
    user_name = input("What's your name? ")
    print(f"Hello, {user_name}!")

    # Ask the user which cloud provider they want to use
    cloud_provider = input("Which cloud provider would you like to use (AWS, Azure, GCP, etc.)? ")

    # List of cloud services for each provider (You can expand this)
    cloud_services = {
        'aws': ['EC2', 'S3', 'RDS', 'Lambda'],
        'azure': ['VM', 'Blob Storage', 'SQL Database', 'Azure Functions'],
        'gcp': ['Compute Engine', 'Cloud Storage', 'BigQuery', 'Cloud Functions']
    }

    if cloud_provider.lower() not in cloud_services:
        print("Sorry, we don't support that cloud provider at the moment.")
        return

    print(f"Here are some services available for {cloud_provider}:")
    for service in cloud_services[cloud_provider.lower()]:
        print(service)

    # Ask the user to select services
    selected_services = input("Please select the services you want (comma-separated): ")
    selected_services = [s.strip() for s in selected_services.split(',')]

    # Generate Terraform IAC template based on user input
    terraform_template = generate_terraform_template(cloud_provider, selected_services)

    print("Here's your Terraform IAC template:")
    print(terraform_template)

def generate_terraform_template(cloud_provider, selected_services):
    # Use Goose AI ChatGPT to generate Terraform code
    prompt = f"Generate Terraform IAC template for {cloud_provider} using {', '.join(selected_services)}."
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150  # Adjust as needed
    )
    terraform_template = response.choices[0].text
    return terraform_template

if __name__ == "__main__":
    chat_with_user()
