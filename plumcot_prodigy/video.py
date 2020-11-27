from moviepy.editor import VideoFileClip
from tempfile import NamedTemporaryFile
import base64
from typing import Dict, Text
from pathlib import Path


def mkv_to_base64(mkv: Path, start_time: float, end_time: float) -> Text:
    """Extract video excerpt for use with prodigy

    Parameters
    ----------
    mkv : Path
        Path to mkv video file
    start_time : float
        Excerpt start time in seconds.
    end_time : float
        Excerpt end time in seconds.
    """

    video = VideoFileClip(mkv).subclip(start_time, end_time)
    with NamedTemporaryFile(mode="wb", suffix=".mp4", delete=True) as fw:
        video.write_videofile(fw.name, preset="ultrafast", logger=None)
        with open(fw.name, mode="rb") as fr:
            b64 = base64.b64encode(fr.read()).decode()
    return f"data:video/mp4;base64,{b64}"
