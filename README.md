# Media_Server_Lite_For_N3DS

This is a python script run on your PC or Mac, then you can play your PC's videos on New 3DS Internet Browser.

## FEATURES

- Support Windows, OSX, Linux(Need Python2.7 and Flask)
- Only Support New 3DS or New3DS XL(Only New3DS browser support HTML5 Videos)
- Only Support MP4 format ( H.264 - MPEG-4 AVC Video, AAC - ISO / IEC 14496-3 MPEG-4AAC, MP3) and resolution resolution lower than 480P.

## USAGE

- Install Python 2.7 and Flask.
- Extract 7z file.
- Put your movie files in static/movie.
- Open command line in the directory, run "python RUN_Server.py".
- open your Internet Browser on New 3DS, go to `http://<your computer's IP>:5000`, you will see your movies list.
- Click it, then click the play icon.
- Internet Browser on New 3DS support Side by Side 3D Movie! Try "3D" on the touch screen!

## FAQ

Q:Where can I find MP4 format videos?

A:The MP4 files downloaded from Youtube are supported. Other files you need a transcoder like this.


Q:Why my MP4 files can't be played.

A:Browser only support  H.264 - MPEG-4 AVC Video, AAC - ISO / IEC 14496-3 MPEG-4AAC, MP3, and resolution resolution lower than 480P.
