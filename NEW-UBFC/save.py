import os
import shutil
from moviepy.editor import VideoFileClip

# Define your root path where subject directories are stored
root_path = r'D:\ubfc-2'  # Change this to your dataset path

# Define the new folder (outside the root path) where videos and ground_truth will be stored
# Specify an absolute path to the destination folder
new_folder = r'D:\NEW-UBFC'  # Change this to the desired outside folder path
os.makedirs(new_folder, exist_ok=True)

# Create videos and ground_truth directories inside the new folder
videos_dir = os.path.join(new_folder, 'videos')
ground_truth_dir = os.path.join(new_folder, 'ground_truth')

os.makedirs(videos_dir, exist_ok=True)
os.makedirs(ground_truth_dir, exist_ok=True)

# List all subject directories (assuming they're named subject<number>)
subject_dirs = [d for d in os.listdir(root_path) if os.path.isdir(os.path.join(root_path, d)) and d.startswith('subject')]

# Loop through each subject directory and move files, using the subject number in file names
for subject_dir in subject_dirs:
    # Extract the subject number from the directory name (e.g., 'subject3' -> '3')
    subject_number = subject_dir.replace('subject', '')
    
    subject_path = os.path.join(root_path, subject_dir)

    # Construct the source paths
    video_src = os.path.join(subject_path, 'vid.avi')
    ground_truth_src = os.path.join(subject_path, 'ground_truth.txt')

    # Construct the destination paths using the subject number
    video_dst_mp4 = os.path.join(videos_dir, f'video_{subject_number}.mp4')
    ground_truth_dst = os.path.join(ground_truth_dir, f'ground_truth_{subject_number}.txt')

    # Convert the video to mp4 and save it to the new location
    if os.path.exists(video_src):
        # Convert .avi to .mp4 using moviepy
        clip = VideoFileClip(video_src)
        clip.write_videofile(video_dst_mp4, codec='libx264')  # Save video as mp4
        clip.close()

    # Move the ground truth file
    if os.path.exists(ground_truth_src):
        shutil.move(ground_truth_src, ground_truth_dst)

print("Files moved and converted successfully!")
