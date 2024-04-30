import time
import requests
import winsound

def check_autosys_job(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print("Error fetching URL:", e)
        return None

def check_jobs_for_failure(html_content):
    # You would need to customize this function based on the structure of your Autosys webpage
    # This is just a placeholder implementation
    if "Failed" in html_content:
        return True
    else:
        return False

def play_alarm():
    winsound.Beep(1000, 1000)  # Beep at 1000 Hz for 1 second

if __name__ == "__main__":
    autosys_url = input("Enter Autosys batch URL: ")
    
    while True:
        html_content = check_autosys_job(autosys_url)
        if html_content is not None:
            if check_jobs_for_failure(html_content):
                print("A job has failed! Playing alarm...")
                play_alarm()
            else:
                print("No failed jobs detected.")
        else:
            print("Failed to fetch URL. Retrying in 1 minute...")
        
        time.sleep(60)  # Wait for 1 minute before checking again
