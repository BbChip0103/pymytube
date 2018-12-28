import pymytube
from functools import partial
import subprocess
from multiprocessing import Pool

# playlist_id = 'PLkHNi_DrLua7Ftxss45CYYSRCrGMPILM1'
# content_list = pymytube.get_contents_by_playlist(playlist_id)
content_list = ['o_peo6U7IRM', 'rNh2CrTFpm4', 'LeVkjCuUdRs']

for content in content_list:
    pymytube.download_video(content, 'result/')

# download_files = partial(pymytube.download_video, output_path='result/',
#                          include_subtitle=False)
#
# pool = Pool(processes=4)
# pool.map(download_files, content_list)
# pool.close()
# pool.join()
