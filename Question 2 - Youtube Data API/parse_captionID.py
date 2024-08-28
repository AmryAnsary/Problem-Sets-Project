import requests

API_KEY = 'AIzaSyCRrEfg2sme2u_eYhsrLFyrzpgexJ1ugcw'  # Replace with API key

# List of video IDs to check
video_ids = ['W7RXTVihRok', 'GH6Vt8SUy-U', 'U62HaQb41T8', 'Y9O_K0oHDnM', 'AjrgHf2Yp_Q', 
             'FjcHiNkal24', 'Uk7W0YK1dSE', 'Nw3szqrt_C0', '25oKzXME0_4', '_7UZoLQzGoU', 
             'cNd0Bo7ByvE', 'eSkdbDpc6tA', 'ddrM3Ik4WSc', 'UZhvAlcSTWM', 'WSR5sqQOpYg', 
             'VsT9JzpO_kg', 'Qp4KyGXVG2M', 'qUaCnAVR5Ns', 'K8xPrgZlVfw', 'jr6HufxNsIc']

# Lists to store the video IDs and caption IDs
caption_ids = []
video_ids_with_captions = []

# Loop through each video ID and check for captions
for video_id in video_ids:
    # API request URL
    captions_url = f"https://www.googleapis.com/youtube/v3/captions?part=snippet&videoId={video_id}&key={API_KEY}"
    
    # Make the API request
    response = requests.get(captions_url)
    
    # Parse the JSON response
    data = response.json()
    
    # Check if captions are available
    if 'items' in data and len(data['items']) > 0:
        for item in data['items']:
            # Append the caption ID and video ID to the respective lists
            caption_ids.append(item['id'])
            video_ids_with_captions.append(video_id)
    else:
        print(f"No captions available for video ID {video_id}.")

# Print the lists of video IDs and caption IDs
print("Video IDs with captions:", video_ids_with_captions)
print("Caption IDs:", caption_ids)