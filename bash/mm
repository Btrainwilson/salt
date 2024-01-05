#!/bin/bash

# Check if the required number of arguments are provided
if [[ $# -lt 1 ]]; then
    echo "Usage: $0 <directory> [command]"
    exit 1
fi

# Set the directory and command variables
DIR="$1"
COMMAND="${2:-make}"  # Default to 'make' if no command is given

# Install inotify-tools if not available
if ! command -v inotifywait &> /dev/null; then
    echo "inotifywait could not be found!"
    echo "Please install inotify-tools package."
    exit 1
fi

# Monitor the directory for modifications and execute the command in the directory
while true; do
    inotifywait -r -e modify "$DIR"
    pushd "$DIR" > /dev/null  # Change to the specified directory
    $COMMAND
    popd > /dev/null  # Return to the previous directory
done

