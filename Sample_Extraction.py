import json

# Define the size limit in bytes (15 GB)
size_limit = 15 * 1024 * 1024 * 1024

# Open the large JSON file for reading
with open('All_Amazon_Meta.json', 'r') as infile:
    # Open a new file for writing filtered content
    with open('filtered_content.json', 'w') as outfile:
        # Initialize a variable to track the total size of extracted data
        extracted_size = 0
        
        # Iterate over each line in the input file
        for line in infile:
            try:
                # Parse the JSON object from the line
                item = json.loads(line)
                
                # Convert the JSON object to a string
                json_str = json.dumps(item)
                
                # Calculate the size of the JSON string
                json_size = len(json_str.encode('utf-8'))
                
                # Check if adding this JSON object exceeds the size limit
                if extracted_size + json_size <= size_limit:
                    # Write the JSON object to the output file
                    outfile.write(json_str + '\n')
                    
                    # Update the total extracted size
                    extracted_size += json_size
                else:
                    # Stop processing if the size limit is reached
                    break
            except json.JSONDecodeError:
                # Skip lines that cannot be parsed as JSON
                continue
