from moviepy.editor import *


video1 = VideoFileClip('vvp.mp4') #file video

logo = (ImageClip('logo.png') #file logo
        .set_duration(video1.duration)
        .resize(height=100)
        .margin(left=2, bottom=2, opacity=0.45)
        .set_pos(('right', 'top')))

final = CompositeVideoClip([video1, logo])
final.write_videofile('vpp1.mp4', audio=True)
