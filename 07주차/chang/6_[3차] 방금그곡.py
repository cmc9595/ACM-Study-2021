def solution(m, musicinfos):
    answer = ''
    m = change_music(m)
    answer = "(None)"
    max_time = 0
    for musicinfo in musicinfos:
        song_time, name, music = get_music(musicinfo)
        # print(song_time, name, music)
        r = int(song_time / len(music))
        s = song_time % len(music)
        full_music = music*r + music[:s]

        if m in full_music:
            if song_time > max_time:
                max_time = song_time
                answer = name

    return answer

def get_music(string):
    start, end, name, music = string.split(",")
    song_time = get_minutes(end) - get_minutes(start)
    new_music = change_music(music)

    return (song_time, name, new_music)

def get_minutes(origin):
    hh, mm = origin.split(":")
    return int(hh)*60 + int(mm)

def change_music(music):
    new_music = ""
    for note in music:
        if note == "#":
            new_note = new_music[-1]
            new_music = new_music[:-1] + new_note.lower()
            continue
        new_music += note

    return new_music