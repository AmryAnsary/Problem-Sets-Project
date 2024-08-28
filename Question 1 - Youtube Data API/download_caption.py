import os
import requests

API_KEY = ''  # Replace with API key
VIDEO_IDS = ['W7RXTVihRok', 'GH6Vt8SUy-U', 'U62HaQb41T8', 'Y9O_K0oHDnM', 'AjrgHf2Yp_Q', 'FjcHiNkal24', 'Uk7W0YK1dSE', 'Nw3szqrt_C0', '25oKzXME0_4', '_7UZoLQzGoU', 'cNd0Bo7ByvE', 'eSkdbDpc6tA', 'ddrM3Ik4WSc', 'UZhvAlcSTWM', 'WSR5sqQOpYg', 'VsT9JzpO_kg', 'Qp4KyGXVG2M', 'qUaCnAVR5Ns', 'K8xPrgZlVfw', 'jr6HufxNsIc']  # Add more video IDs here
OUTPUT_FOLDER = 'captions_folder'  # Specify your desired folder

# Ensure the output folder exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Dictionary to map video IDs to their corresponding caption IDs (manually filled or obtained earlier)
VIDEO_CAPTION_MAP = {
    'W7RXTVihRok': 'AUieDaZyvlTcqsDWuVic4AVK5iLowdhNRlF9jbtt9Q4-gLCJmpw',
    'GH6Vt8SUy-U': 'AUieDaZ8X8mZT8WCu6iVQ4sN1CRguzfVHDBSGZgUXzo6dX_1BTA',
    'Y9O_K0oHDnM': 'AUieDaYSo1PzPtvMyMk0gQTdoEUzxlHg2XnggbvtPn_9lpRhmeA',
    'FjcHiNkal24': 'AUieDabN56dwWtqawSBn_YLKnhpXsgM1LhSJBn3DRXal2r4pjsw',
    'Uk7W0YK1dSE': 'AUieDaYX20R-0mT-yCy1OpzN_oDr_gKU3Cww-pZex6TJvYdpWWk',
    'Nw3szqrt_C0': 'AUieDaZy9L67OL6-mrgmV4cDPr5-1ldt1Pei1oj6FJ5iGQVfNI0',
    '25oKzXME0_4': 'AUieDaYg3jn4EV3prxZ5dGvJbF-V-U1xEGn3g5CpUlZCOjCz2zo',
    '_7UZoLQzGoU': 'AUieDaZDmMuCRh7soBeOhJ_dy7ry8g70QRgShT0YLuibtOPXww4',
    'cNd0Bo7ByvE': 'AUieDaazFAbG1bUhE4D5V1ItpGKYtxVWaT8G5xwGx08o9mfe8AQ',
    'eSkdbDpc6tA': 'AUieDaaGRMNFqlK8iU7LmqSJc5MYFJUdJ3UimW2s0LOa0Ng7PGY',
    'ddrM3Ik4WSc': 'AUieDaY2TJnVeCtiiY2Eg-3vDlVndkCcS0qzaVtpsGLDPfrmgFo',
    'WSR5sqQOpYg': 'AUieDaabwQ5Edu_MEyecCRUSO604-kdTmHMuhop68q0qI9Jl9TQ',
    'VsT9JzpO_kg': 'AUieDabr5JQytZZEIWwzUsJgp2jb1oJ6aXgtgq3BDIYHAoygZw',
    'Qp4KyGXVG2M': 'AUieDaaHjRTEATnDR-INJeDtypgGjOVUljK9bE9ihubtSiA20cU',
    'qUaCnAVR5Ns': 'AUieDaYjF-4AKxop99WNpGE_hvcsFJbCieaK0oSNx7qM0mEJRfs',
    'K8xPrgZlVfw': 'AUieDab1X2oVMRmZovkk1tDd0gCDWu-bfqJvQhJgfyt8-aI8xXY',
    'jr6HufxNsIc': 'AUieDaZA4O_ASD9peFhjlA5mQYaYUbruvXbrQu5-yiF8IAu0mOI'
    # Add all your video IDs with their corresponding caption IDs here
}

def download_captions(video_id, caption_id):
    # Step 3: Download the captions using the provided caption_id
    download_url = f"https://www.googleapis.com/youtube/v3/captions/{caption_id}?key={API_KEY}&tfmt=srt"
    caption_response = requests.get(download_url)
    
    if caption_response.status_code == 200:
        # Save or process the caption file
        file_path = os.path.join(OUTPUT_FOLDER, f"{video_id}_captions.srt")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(caption_response.text)
        print(f"Captions for video {video_id} saved to {file_path}")
    else:
        print(f"Failed to download captions for video {video_id} (caption ID: {caption_id}).")

# Process each video ID and corresponding caption ID
for video_id in VIDEO_IDS:
    caption_id = VIDEO_CAPTION_MAP.get(video_id)
    if caption_id:
        download_captions(video_id, caption_id)
    else:
        print(f"No caption ID found for video {video_id}.")