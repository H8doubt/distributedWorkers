# distributedWorkers

 python -m pip -r requirements.txt

 # Task Management System

## Overview

This Python program implements a simple task management system using multithreading. It allows users to create worker threads that process tasks concurrently. Each worker has a performance metric that affects how quickly it can complete tasks, and users can add tasks dynamically while checking the status of each worker.

## Features

- Multithreading support for concurrent task processing.
- Dynamic task addition with user-defined complexity.
- Performance-based task completion time.
- Status checking for each worker, including remaining time and queue length.
- Graceful shutdown of workers.

## Requirements

- Python 3.x
- No external libraries are required; the program uses standard Python libraries.

## Usage

1. Clone the repository or download the script.
2. Run the script using Python:
3. 
   python main.py
   
4. Follow the prompts to:
   - Enter the number of workers.
   - Define the performance for each worker.
   - Add tasks with specified complexities.
   - Check the status of the workers.
   - Exit the program when finished.

## Commands

- add_task: Prompts for task complexity and adds a new task to the least busy worker.
- check_status: Displays the remaining time and queue length for each worker.
- exit: Exits the program, signaling workers to finish their current tasks before shutting down.


### Example

When prompted, you might enter:


Enter the number of workers: 2
Enter performance for Process 1: 2.0
Enter performance for Process 2: 1.0
Enter a command (add_task/check_status/exit): add_task
Enter task complexity: 5.0
..   
