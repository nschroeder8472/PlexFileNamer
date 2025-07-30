import os

show_name = "Show Name"
directory_path = "Path to video Files"
episode_names_path = "Path to Show Episode Name text file"

def replace_illegal_char(s:str):
    illegal_chars = ['<', '>',':', '\'', '/', '\\', '|', '?', '*', '\n']
    for illegal_char in illegal_chars:
        s = s.replace(illegal_char, "")
    return s

contents = os.listdir(directory_path)
try:
    with open(episode_names_path, 'r') as file:
        for episode in file:
            episode_num_name = episode.split("~")
            episode_num = episode_num_name[0]
            episode_name = replace_illegal_char(episode_num_name[1])
            for video_file in contents:
                if os.path.isdir(os.path.join(directory_path, video_file)):
                    continue
                if video_file.lstrip().startswith(episode_num):
                    ext = os.path.splitext(video_file)[1]
                    full_vid_path = os.path.join(directory_path, video_file)
                    new_vid_name = os.path.join(directory_path, f"{show_name} - {episode_num} - {episode_name}{ext}")
                    os.rename(full_vid_path, new_vid_name)
                    break

except Exception as e:
    print(f"oops: {e}", e)

