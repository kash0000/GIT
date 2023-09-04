import gensim
from gensim.summarization import summarize

# Function to summarize text from a file
def summarize_from_file(file_path, summary_ratio=0.1):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            input_text = file.read()
        
        # Perform extractive summarization
        summary = summarize(input_text, ratio=summary_ratio)
        
        return summary
    except Exception as e:
        return str(e)

# Input file path (replace 'input.txt' with the path to your input file)
input_file_path = 'input.txt'

# Set the desired summary ratio (0.1 means 10% of the original text will be in the summary)
summary_ratio = 0.1

# Generate the summary
summary_result = summarize_from_file(input_file_path, summary_ratio)

# Print the summary
if summary_result:
    print("Summary:")
    print(summary_result)
else:
    print("Error occurred while summarizing the file.")
