from moviepy.editor import * 
import numpy as np
import moviepy.video.fx.all as vfx
from moviepy.video.tools.segmenting import findObjects

# WE CREATE THE TEXT THAT IS GOING TO MOVE, WE CENTER IT.

screensize = (720,460)


txtClip = TextClip('Shibal hello',color='white', font="Montserrat", fontsize=50).set_duration(5)



final_clip = txtClip
final_clip = final_clip.set_start(1.7).crossfadein(1.5).set_duration(5).set_pos('center')

clip = VideoFileClip("template.mp4").subclip(0,5)

video = CompositeVideoClip([clip, final_clip])
video.write_videofile("myHolidays_edited.mp4",fps=60)