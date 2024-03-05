import csv
import pandas as pd
import re

class Task:

    def __init__(self, id, required_inputs, optional_inputs, outputs, prompt):
        self.id = id
        self.required_inputs = self.parse_list(required_inputs)
        self.optional_inputs = self.parse_list(optional_inputs)
        self.outputs = self.parse_list(outputs)
        self.prompt = prompt

    def parse_list(self, string):
        # Remove trailing "..." and split the string into elements using commas as separators
        elements = string.rstrip('...').split(',')
        
        # Clean up each element by removing leading and trailing whitespaces
        cleaned_elements = [element.strip() for element in elements]
        
        # Remove empty elements from the list
        return [element for element in cleaned_elements if element]

    def create_input(self, inputs):
        for input in self.required_inputs:
            if input not in inputs.keys():
                return -1
        for input in inputs.keys():
            if (input not in self.required_inputs) and (input not in self.optional_inputs):
                return -1
        # Replace [INPUTNAME] in self.prompt with corresponding input strings
        prompt = self.prompt
        for input_name, input_string in inputs.items():
            placeholder = f"[{input_name}]"
            prompt = prompt.replace(placeholder, input_string)
        for input_name in self.optional_inputs:
            if input_name not in inputs.items():
                placeholder = f"[{input_name}]"
                prompt = prompt.replace(placeholder, "unknown") 
        # Skip optional inputs in the parenthesis if the inputs are the same length as required inputs
        if len(inputs) == len(self.required_inputs):
            opening_parenthesis = prompt.find('(')
            closing_parenthesis = prompt.find(')') + 1
            prompt = prompt[:opening_parenthesis] + prompt[closing_parenthesis:]
        prompt = prompt.replace('(','').replace(')','')
        return prompt

    def create_output(self, outputs):
        for output in self.outputs:
            if output not in outputs.keys():
                return -1
        for output in outputs.keys():
            if output not in self.outputs:
                return -1
        prompt = ""
        for output in outputs.keys():
            prompt = prompt + "[" + output.upper() + "][" + outputs[output] + "]"
        return prompt
        


def load_tasks():
    tasks = {}

    with open('Tasks/Tasks.csv', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, quotechar='"')

        # Skip the header row
        header = next(reader)

        for row in reader:

            task = Task(
                int(row[0]),
                row[2],
                row[3], 
                row[4],
                row[5],  
            )

            # Remove double quotes from the parsed values
            task.required_inputs = [element.strip('\"') for element in task.required_inputs]
            task.optional_inputs = [element.strip('\"') for element in task.optional_inputs]
            task.outputs = [element.strip('\"') for element in task.outputs]
            task.prompt = task.prompt.strip('\"')

            tasks[task.id] = task

    return tasks


# Example usage:
tasks_dict = load_tasks()

# Accessing task information by id
task_id = 18
if task_id in tasks_dict:
    task_info = tasks_dict[task_id]
    print(f"Required Inputs: {task_info.required_inputs}")
    print(f"Optional Inputs: {task_info.optional_inputs}")
    print(f"Outputs: {task_info.outputs}")
    print(f"Prompt: {task_info.prompt}")
    print(task_info.create_input({"fen": "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"}))
    print(task_info.create_output({"reasoning": "hmmmm","move":"e4"}))
else:
    print(f"Task with id {task_id} not found.")
