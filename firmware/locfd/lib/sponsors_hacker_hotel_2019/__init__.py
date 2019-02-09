# SPONSORS APPLICATION
# SHOWN ONCE AFTER SETUP

import ugfx, badge, appglue, utime, audio, wifi

def show_sponsors():
    for x in range(1, 17):
      	ugfx.set_lut(ugfx.LUT_NORMAL)
        ugfx.clear(ugfx.WHITE)
        ugfx.flush()
        try:
            ugfx.set_lut(ugfx.GREYSCALE)
            badge.eink_png(0,0,'/lib/sponsors_hacker_hotel_2019/sponsor%s.png' % x)
        except:
            ugfx.string(0, 0, "SPONSOR LOAD ERROR #"+str(x), "Roboto_Regular12", ugfx.BLACK)
        ugfx.flush()
        utime.sleep(3)

def play_music():
    wifi.init()
    wifi.connect()
    if wifi.wait(5, True):
        audio.play_mp3_stream('https://badge.team/RoccoW_-_06_-_Pumped.mp3')

def program_main():
    print("--- SPONSORS APP ---")
    ugfx.init()
    ugfx.set_lut(ugfx.LUT_NORMAL)
    ugfx.clear(ugfx.BLACK)
    ugfx.flush()
    play_music()
    show_sponsors()
    appglue.start_app("") # Return home

# Start main application
program_main()
