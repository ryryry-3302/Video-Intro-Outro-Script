# importing Numpy
import numpy as np
import os

# importing moviepy module
from moviepy.editor import * 
from moviepy.video.tools.segmenting import findObjects

def videointromaker(filename):
	title = filename.strip(".mp4")
	# screen size
	screensize = (720, 460)
	
	# creating a text clip of color green, font is Arial and size is 80
	txtClip = TextClip(title, color = 'gold', font = "Monteseratt",
					kerning = 5, fontsize = 80)

	title_clip = txtClip

	template_clip = VideoFileClip("templates/template.mp4").subclip(0,5)


	intro_video = CompositeVideoClip([template_clip, title_clip.subclip(0,5).set_pos('center').crossfadein(1.5).set_start(1.7).set_duration(3).crossfadeout(.5)])
	mid_clip = VideoFileClip(f"vids_to_edit/{filename}")
	end_clip = VideoFileClip("templates/template_end.mp4")
	final_video = concatenate_videoclips([intro_video,mid_clip,end_clip])


	final_video.write_videofile(f"vids_final/{filename}",fps=60)

# Get the list of all files and directories

dir_list = os.listdir("./vids_to_edit")

for videoname in dir_list:
	videointromaker(videoname)
