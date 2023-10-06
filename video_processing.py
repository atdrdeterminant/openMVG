import os
import fire
from Katna.video import Video
from Katna.writer import KeyFrameDiskWriter


def key_frame_extraction(num_frames, video_file_path, frame_folder):
    """
    Extract key frames from a video
    :param num_frames: number of frames to extract
    :param video_path: path to video
    :param frame_folder: path to save frames
    :return:
    """
    vd = Video()
    # create frame folder if not exists
    os.makedirs(frame_folder, exist_ok=True)
    diskwriter = KeyFrameDiskWriter(location=os.path.join(frame_folder,"images"))

    # extract key frames
    vd.extract_video_keyframes(
       no_of_frames=num_frames, file_path=video_file_path,
       writer=diskwriter)
    
    print("Key frames extracted successfully")


if __name__ == "__main__":
    fire.Fire(key_frame_extraction)