import requests

# API key and the search URL
API_KEY = ''
SEARCH_URL = f"https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=20&order=date&q=surfing&type=video&key=AIzaSyCRrEfg2sme2u_eYhsrLFyrzpgexJ1ugcw"

# Make the API request
response = requests.get(SEARCH_URL)

# Parse the JSON response
data = response.json()

# Extract video IDs
video_ids = [item['id']['videoId'] for item in data['items']]

# Print the video IDs
for vid in video_ids:
    print(vid)
