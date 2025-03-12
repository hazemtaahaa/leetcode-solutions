import requests
import re

# Replace with your LeetCode username
LEETCODE_USERNAME = "HazemTaha"

def get_leetcode_stats(username):
    """
    Fetch LeetCode stats for the given username.
    """
    url = f"https://leetcode.com/{username}/"
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        raise Exception(f"Failed to fetch LeetCode stats. Status code: {response.status_code}")
    
    # Extract stats from the response (this may require inspecting the page source)
    # Example: Look for the progress stats in the HTML
    # (You may need to use BeautifulSoup or regex for this)
    # For now, we'll use placeholder values
    stats = {
        "easy": 50,
        "medium": 60,
        "hard": 10,
        "total": 120
    }
    return stats

def update_readme(stats):
    """
    Update the README.md file with the latest LeetCode stats.
    """
    with open("../README.md", "r") as f:
        content = f.read()
    
    # Define the new progress section
    new_progress_section = f"""
## LeetCode Progress

![Easy](https://img.shields.io/badge/Easy-{stats['easy']}%20solved-brightgreen)
![Medium](https://img.shields.io/badge/Medium-{stats['medium']}%20solved-yellow)
![Hard](https://img.shields.io/badge/Hard-{stats['hard']}%20solved-red)
![Total](https://img.shields.io/badge/Total-{stats['total']}%20solved-blue)
"""
    
    # Replace the existing progress section (if any)
    # Use regex to find and replace the progress section
    progress_pattern = r"## LeetCode Progress[^#]*"
    updated_content = re.sub(progress_pattern, new_progress_section, content, flags=re.DOTALL)
    
    # Write the updated content back to README.md
    with open("../README.md", "w") as f:
        f.write(updated_content)

def main():
    # Fetch LeetCode stats
    stats = get_leetcode_stats(LEETCODE_USERNAME)
    
    # Update README.md with the latest stats
    update_readme(stats)
    print("README.md updated successfully!")

if __name__ == "__main__":
    main()
