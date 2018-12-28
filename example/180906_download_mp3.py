import pymytube
from functools import partial
import subprocess
from multiprocessing import Pool

# playlist_id = 'PLkHNi_DrLua7Ftxss45CYYSRCrGMPILM1'
# content_list = pymytube.get_contents_by_playlist(playlist_id)

# for content in content_list:
#     pymytube.download_audio(content, 'result/')

# download_files = partial(pymytube.download_audio, output_path='result/',
#                          include_subtitle=False)
#
# pool = Pool(processes=4)
# pool.map(download_files, content_list)
# pool.close()
# pool.join()

# audio_url = 'https://www.youtube.com/watch?v=EW_JjNpJx2g'
# pymytube.download_audio(audio_url, 'result/')
pymytube.cvt_video_to_mp3('result/'+'Sereno - Bad Prolog (악성 프롤로그).mp4', 'result/')
