import csv
import re

class Task:

    def __init__(self, id, required_inputs, optional_inputs, outputs, prompt):
        self.id = id
        self.required_inputs = self.parse_list(required_inputs)
        self.optional_inputs = self.parse_list(optional_inputs)
        self.outputs = self.parse_list(outputs)
        self.prompt = prompt

    def parse_list(self, string):
        # Assuming the input string is enclosed in square brackets []
        # and elements are separated by commas
        elements = re.findall(r'\[([^\]]+)\]', string)
        cleaned_elements = [element.replace('...', '').strip() for element in elements]
        return [element for element in cleaned_elements if element]  # Remove empty elements

    def generate_prompt(self, inputs):
        for input in self.required_inputs:
            if input not in inputs.keys():
                return -1
        # Replace [INPUTNAME] in self.prompt with corresponding input strings
        prompt = self.prompt
        for input_name, input_string in inputs.items():
            placeholder = f"[{input_name}]"
            prompt = prompt.replace(placeholder, input_string)

        # Skip optional inputs in the parenthesis if the inputs are the same length as required inputs
        if len(inputs) == len(self.required_inputs):
            opening_parenthesis = prompt.find('(')
            closing_parenthesis = prompt.find(')') + 1
            prompt = prompt[:opening_parenthesis] + prompt[closing_parenthesis:]

        return prompt

        


def load_tasks():
    tasks = {}

    with open('Tasks/Tasks.csv', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        header = next(reader)  # Read the header
        for row in reader:
            task = Task(
                int(row[0]),
                row[2],
                row[3],
                row[4],
                row[5],
            )
            tasks[task.id] = task

    return tasks

# Example usage:
tasks_dict = load_tasks()

# Accessing task information by id
task_id = 0
if task_id in tasks_dict:
    task_info = tasks_dict[task_id]
    print(f"Required Inputs: {task_info.required_inputs}")
    print(f"Optional Inputs: {task_info.optional_inputs}")
    print(f"Outputs: {task_info.outputs}")
    print(f"Prompt: {task_info.prompt}")
    print(task_info.generate_prompt({"CONVERSATION": "Hello", "NAME": "Henri"}))
else:
    print(f"Task with id {task_id} not found.")
