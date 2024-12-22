# Tasks CLI

A simple command-line todo list application written in Python that helps you manage tasks across different states: todo, in progress, and done.

## Features

- Manage tasks in three different lists:
  - Todo
  - In Progress
  - Done
- Add new tasks
- Update existing tasks
- Delete tasks
- Move tasks between lists
- Persistent storage using JSON

## Installation

### Linux/MacOS
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd tasks-cli
   ```
2. Make the Python script executable

    ```bash
    chmod +x tc.py
    ```

3. Create symbolic link in /usr/local/

    ```bash
    sudo ln -sf "$(pwd)/tc.py" /usr/local/bin/tc
    ```

After installation, you can run the program from anywhere using the `tc` command.

## Usage

The command syntax is: `tc <command> [options]`

### Available Commands

#### View Tasks
```bash
tc list todo         # List all todo tasks
tc list in_progress  # List all in-progress tasks
tc list done        # List all completed tasks
```

#### Add Tasks
```bash
tc add 'task description'  # Add a new task to todo list
```

#### Update Tasks
```bash
tc update todo 1 'updated task'      # Update task #1 in todo list
tc update in_progress 1 'new text'   # Update task #1 in in-progress list
tc update done 1 'completed task'    # Update task #1 in done list
```

#### Delete Tasks
```bash
tc delete 1              # Delete task #1 from todo list
tc delete todo 1         # Delete task #1 from todo list
tc delete in_progress 1  # Delete task #1 from in-progress list
tc delete done 1         # Delete task #1 from done list
```

#### Move Tasks Between Lists
```bash
tc mark-inp 1    # Move task #1 from todo to in-progress
tc mark-done 1   # Move task #1 from todo to done
tc finish 1      # Move task #1 from in-progress to done
```

#### Help
```bash
tc help  # Display help information
```

## Data Storage

The application stores all tasks in a file called `liststorage.json` in the same directory as the script. You can backup this file to preserve your tasks.

## Error Handling

The application includes error handling for:
- Invalid commands
- Invalid task indices
- File read/write errors
- JSON parsing errors
- Missing command arguments

## Author

Written by aswinpradeepc

## Note

This application was written to beat boredom, but provides practical task management functionality through a simple command-line interface.