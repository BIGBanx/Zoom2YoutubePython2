import os.path

from zoom import ZoomRecording
from youtube import YoutubeRecording
from settings import (
    ZOOM_KEY, ZOOM_SECRET, ZOOM_HOST_ID, ZOOM_EMAIL, ZOOM_PASSWORD, VIDEO_DIR,
    GOOGLE_REFRESH_TOKEN, GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, DOWNLOADED_FILES
)


class lock(object):
    def __init__(self, lock_file):
        self._lock_file = lock_file

    def __enter__(self):
        if os.path.exists(self._lock_file):
            exit('The program is still running')
        open(self._lock_file, 'w').close()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if os.path.exists(self._lock_file):
            os.remove(self._lock_file)


if __name__ == '__main__':
    with lock('lock'):
        zoom = ZoomRecording(ZOOM_KEY, ZOOM_SECRET, ZOOM_HOST_ID)
        zoom.download_meetings(
            ZOOM_EMAIL, ZOOM_PASSWORD, VIDEO_DIR, DOWNLOADED_FILES
        )

        youtube = YoutubeRecording(
            GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, GOOGLE_REFRESH_TOKEN
        )
        youtube.uploads_videos(VIDEO_DIR)
