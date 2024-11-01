# Author: Sahil Patel id:100991127, Kshitiz Pal id:100970696
# Date: 2024-11-01
# Description: This Python program filters and displays AWS EC2 instance types based on user-defined CPU and memory requirements.
<<<<<<< Tabnine <<<<<<<
def retrieve_cpu_requirements():#+
    """#+
    Get valid minimum and maximum CPU requirements from the user.#+
#+
    This function prompts the user to enter the minimum and maximum CPU cores required.#+
    It validates the input to ensure that the minimum CPU cores is a non-negative integer and#+
    the maximum CPU cores is either a non-negative integer or infinity (indicating no limit).#+
    If the input is invalid, the function displays an error message and prompts the user again.#+
#+
    Parameters:#+
    None#+
#+
    Returns:#+
    tuple: A tuple containing the minimum and maximum CPU cores requirements.#+
    """#+
    while True:#+
        try:#+
            minimum_cpu = int(input("Enter minimum CPU cores required: "))#+
            maximum_cpu = int(input("Enter maximum CPU cores required (press enter for no limit): ") or float('inf'))#+
            if minimum_cpu < 0 or maximum_cpu < minimum_cpu:#+
                print("Please enter valid CPU values.")#+
                continue#+
            return minimum_cpu, maximum_cpu#+
        except ValueError:#+
            print("Invalid input. Please enter integer values for CPU cores.")#+
>>>>>>> Tabnine >>>>>>># {"conversationId":"db569ea8-e6fd-43ef-96f9-50566c5742f2","source":"instruct"}
import json

def retrieve_cpu_requirements():
    """Get valid minimum and maximum CPU requirements from the user."""
    while True:
        try:
            minimum_cpu = int(input("Enter minimum CPU cores required: "))
            maximum_cpu = int(input("Enter maximum CPU cores required (press enter for no limit): ") or float('inf'))
            if minimum_cpu < 0 or maximum_cpu < minimum_cpu:
                print("Please enter valid CPU values.")
                continue
            return minimum_cpu, maximum_cpu
        except ValueError:
            print("Invalid input. Please enter integer values for CPU cores.")

def retrieve_memory_requirements():
    """Get valid minimum and maximum memory requirements from the user."""
    while True:
        try:
            minimum_memory = float(input("Enter minimum memory required in GiB: "))
            maximum_memory = float(input("Enter maximum memory required (press enter for no limit): ") or float('inf'))
            if minimum_memory < 0 or maximum_memory < minimum_memory:
                print("Please enter valid memory values.")
                continue
            return minimum_memory, maximum_memory
        except ValueError:
            print("Invalid input. Please enter numeric values for memory.")

def convert_memory_size(memory_input):
    """Convert memory size from string format (e.g., '3.75 GiB') to float."""
    try:
        if 'GiB' in memory_input:
            memory_amount = memory_input.split()[0]  # Extract the numeric part
            return float(memory_amount)  # Convert to float
        return 0.0  # Default value if 'GiB' is not found
    except (IndexError, ValueError):
        return 0.0  # Default value if conversion fails

def load_ec2_instances_from_file(file_path):
    """Load EC2 instances from a JSON file."""
    with open(file_path, 'r') as file:
        return json.load(file)

def filter_ec2_instances_by_requirements(instance_list, minimum_cpu, maximum_cpu, minimum_memory, maximum_memory):
    """Filter EC2 instances based on CPU and memory requirements."""
    filtered_instance_list = []

    for instance in instance_list:
        cpu_cores_count = int(instance.get('vcpu', '0 vCPU').split()[0])  # Extract CPU cores
        memory_capacity = convert_memory_size(instance.get('memory', '0 GiB'))  # Extract memory size

        # Check if the instance meets the requirements
        if (minimum_cpu <= cpu_cores_count <= maximum_cpu) and (minimum_memory <= memory_capacity <= maximum_memory):
            filtered_instance_list.append(instance)

    return filtered_instance_list

def execute_main():
    """Main function to run the EC2 instance filter application."""
    minimum_cpu, maximum_cpu = retrieve_cpu_requirements()
    minimum_memory, maximum_memory = retrieve_memory_requirements()

    # Load EC2 instances from JSON file
    instances_data = load_ec2_instances_from_file('ec2_instance_types.json')

    # Filter instances based on user requirements
    matched_instance_list = filter_ec2_instances_by_requirements(instances_data, minimum_cpu, maximum_cpu, minimum_memory, maximum_memory)

    # Output results
    
    if matched_instance_list:
        print("\nMatched EC2 Instances:")
        for instance in matched_instance_list:
            print(f"- Name: {instance['name']}, vCPUs: {instance['vcpu']}, Memory: {instance['memory']}, "
                  f"Storage: {instance['storage']}, Bandwidth: {instance['bandwidth']}, "
                  f"Availability: {instance['availability']}")
    else:
        print("No instances matched your requirements.")

if __name__ == "__main__":
    execute_main()
