# importing Numpy
import numpy as np

# importing moviepy module
from moviepy.editor import * 
from moviepy.video.tools.segmenting import findObjects

def videointromaker(filename):

	# screen size
	screensize = (720, 460)

	# creating a text clip of color green, font is Arial and size is 80
	txtClip = TextClip('SHIBALLLLL', color = 'gold', font = "Monteseratt",
					kerning = 5, fontsize = 80)

	# creating a composite video of given size
	cvc = CompositeVideoClip( [txtClip.set_pos('center')],
							size = screensize)

	# helper function
	rotMatrix = lambda a: np.array( [[np.cos(a), np.sin(a)],
									[-np.sin(a), np.cos(a)]] )


	# creating a effect 1 method
	def effect1(screenpos, i, nletters):
		
		# damping
		d = lambda t : 1.0/(0.3 + t**8)
		# angle of the movement
		a = i * np.pi / nletters
		
		# using helper function
		v = rotMatrix(a).dot([-1, 0])
		
		if i % 2 : v[1] = -v[1]
			
		# returning the function
		return lambda t: screenpos + 400 * d(t)*rotMatrix(0.5 * d(t)*a).dot(v)

	# method for effect 2
	def effect2(screenpos, i, nletters):
		
		# numpy array
		v = np.array([0, -1])
		
		d = lambda t : 1 if t<0 else abs(np.sinc(t)/(1 + t**4))
		
		# returning the function
		return lambda t: screenpos + v * 400 * d(t-0.15 * i)



	# a list of ImageClips
	letters = findObjects(cvc)


	# method to move letters
	def moveLetters(letters, funcpos):
		
		return [ letter.set_pos(funcpos(letter.screenpos, i, len(letters)))
				for i, letter in enumerate(letters)]

	# adding clips with specific effect
	clips = [ CompositeVideoClip( moveLetters(letters, funcpos),
								size = screensize).subclip(0, 5)
			for funcpos in [effect1] ]

	# comping all the clips
	title_clip = concatenate_videoclips(clips)

	template_clip = VideoFileClip("templates/template.mp4").subclip(0,5)


	intro_video = CompositeVideoClip([template_clip, title_clip.subclip(0,5).set_pos('center').set_start(1.4).set_duration(2.5)])
	mid_clip = VideoFileClip(f"vids_to_edit_/{filename}")
	end_clip = VideoFileClip("templates/template_end.mp4")
	final_video = concatenate_videoclips([intro_video,mid_clip,end_clip])


	final_video.write_videofile(f"vids_final/{filename}",fps=60)


for
videointromaker("1stvideo.mp4")
