import pyscreenshot as ImageGrab

# fullscreen
im = ImageGrab.grab()
im.show()

# part of the screen
im = ImageGrab.grab(bbox=(10,10,510,510))
im.show()

# 스크린샷 헤더 다운로드 필요!
