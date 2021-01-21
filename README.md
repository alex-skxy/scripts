# scripts
A collection of random and not-so-random scripts.
I cannot guarantee that any of these scripts works 100% and will not f up your system. Execute at your own risk.

- [scripts](#scripts)
- [fixes](#fixes)
  * [conf-pen](#-conf-pen--https---githubcom-alex-skxy-scripts-blob-main-fixes-conf-pen-)
  * [conf-rotate-input](#-conf-rotate-input--https---githubcom-alex-skxy-scripts-blob-main-fixes-conf-rotate-input-)
  * [conf-screen-input](#-conf-screen-input--https---githubcom-alex-skxy-scripts-blob-main-fixes-conf-screen-input-)
- [ffmpeg](#ffmpeg)
  * [crop](#-crop--https---githubcom-alex-skxy-scripts-blob-main-ffmpeg-crop-)
  * [cut](#-cut--https---githubcom-alex-skxy-scripts-blob-main-ffmpeg-cut-)
  * [draw_box](#-draw-box--https---githubcom-alex-skxy-scripts-blob-main-ffmpeg-draw-box-)
  * [draw_text](#-draw-text--https---githubcom-alex-skxy-scripts-blob-main-ffmpeg-draw-text-)
  * [tomp4](#-tomp4--https---githubcom-alex-skxy-scripts-blob-main-ffmpeg-tomp4-)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

# fixes
Sometimes your system doesn't work the way you'd like it to. These fixes are here to fix that.

## [conf-pen](https://github.com/alex-skxy/scripts/blob/main/fixes/conf-pen)
Remaps the side-button of a Surface Pen to right click (instead of middle click) on Xorg.
Usage: `./conf-pen`

## [conf-rotate-input](https://github.com/alex-skxy/scripts/blob/main/fixes/conf-rotate-input)
Rotates the screen AND input under Xorg.
Change the top variables to suit your needs.
Based on [https://gist.github.com/rubo77/daa262e0229f6e398766](https://gist.github.com/rubo77/daa262e0229f6e398766)
Usage: `./conf-rotate-input`

## [conf-screen-input](https://github.com/alex-skxy/scripts/blob/main/fixes/conf-screen-input)
Remaps pen and eraser input to only one screen when two screens are connected.
Change the top variables to suit your needs.
Usage: `./conf-screen-input`

# ffmpeg
ffmpeg related scripts for future reference.

## [crop](https://github.com/alex-skxy/scripts/blob/main/ffmpeg/crop)

## [cut](https://github.com/alex-skxy/scripts/blob/main/ffmpeg/cut)
Usage: `./cut input-file timestamp-from timpestamp-to output-file`

## [draw_box](https://github.com/alex-skxy/scripts/blob/main/ffmpeg/draw_box)
Draws a white box somewhere over the video. More of a cheatsheet than usable script.
Usage: `./draw_box input-file output-file`

## [draw_text](https://github.com/alex-skxy/scripts/blob/main/ffmpeg/draw_text)
Draws black text somewhere over the video. Combine with draw_box and go make some memes.
Usage: `./draw_text input-file output-file text`

## [tomp4](https://github.com/alex-skxy/scripts/blob/main/ffmpeg/tomp4)
Extra simple script to convert a file to mp4.
Usage: `./tomp4 input-file output-file`
