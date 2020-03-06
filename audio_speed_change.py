from pydub import AudioSegment

def speed_change(sound, speed=1.0):
    # Manually override the frame_rate. This tells the computer how many
    # samples to play per second
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
         "frame_rate": int(sound.frame_rate * speed)
      })
     # convert the sound with altered frame rate to a standard frame rate
     # so that regular playback programs will work right. They often only
     # know how to play audio at standard frame rate (like 44.1k)
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)


if __name__ == '__main__':
	song_name = input("Enter your song name: ")
	song = AudioSegment.from_mp3(song_name)
	rate = input("Enter the speed rate: ")
	new_song = speed_change(song, float(rate))

	new_song.export("Speedrate"+rate+"_"+song_name, format="mp3")

