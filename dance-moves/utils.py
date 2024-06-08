import os
import time
from dotenv import load_dotenv

load_dotenv()

YOUTUBE_VIDEO = os.getenv('YOUTUBE_VIDEO')
VIDEO_PATH = os.getenv('VIDEO_PATH')
IMAGES_PATH = os.getenv('IMAGES_PATH')
VIDEO_NAME = os.getenv('VIDEO_NAME')


def get_video_dir_path():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    video_dir_path = os.path.join(dir_path, VIDEO_PATH)

    return video_dir_path


def get_images_dir_path():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    images_dir_path = os.path.join(dir_path, IMAGES_PATH)

    return images_dir_path


def get_video_path():
    video_dir_path = get_video_dir_path()
    video_path = os.path.join(video_dir_path, VIDEO_NAME)

    return video_path


def get_every_video_frame():
    return int(os.getenv('EVERY_VIDEO_FRAME'))


def get_youtube_video():
    return os.getenv('YOUTUBE_VIDEO')


def get_video_name():
    return os.getenv('VIDEO_NAME')


def get_image_prefix():
    return os.getenv('IMAGE_PREFIX')


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Время выполнения {func.__name__}: {elapsed_time:.2f} секунд")
        return result
    return wrapper
