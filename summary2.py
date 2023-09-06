from summarizer import Summarizer

# Function to summarize text from a file
def summarize_from_file(file_path, num_sentences=3):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            input_text = file.read()
        
        # Initialize the BERT summarizer
        model = Summarizer()
        
        # Generate the summary
        summary = model(input_text, num_sentences=num_sentences)
        
        return summary
    except Exception as e:
        return str(e)

# Input file path (replace 'input.txt' with the path to your input file)
input_file_path = 'input.txt'

# Set the number of sentences in the summary
num_sentences = 3

# Generate the summary
summary_result = summarize_from_file(input_file_path, num_sentences)

# Print the summary
if summary_result:
    print("Summary:")
    print(summary_result)
else:
    print("Error occurred while summarizing the file.")
