# This module is made for getting json of yt video details

import re


def get_streams(YouTube):
    """
    YouTube : Youtube object
        from pytube.ytstreams import get_streams
        yt = YouTube(yt_url)
        get_streams(yt)
    """
    streams = YouTube.streams
    qualities = YouTube.vid_info['streamingData']
    dash = qualities['adaptiveFormats']
    progressive = qualities['formats']
    streamList = []
    for i in dash:
        mimeTypeDetails = i['mimeType'].split(";")
        mimeType = mimeTypeDetails[0]
        itag = i['itag']
        url = i['url']
        stream = {
            'itag': itag,
            'mime_type': mimeType,
            'url':url
        }

        if 'video' in mimeType:
            stream['fps'] = i['fps']
            stream['resolution'] = i['qualityLabel']
            stream['width'] =i['width']
            stream['height'] = i['height']
            stream['video_codec'] = re.findall('"[^"]*"', mimeTypeDetails[-1])[0].replace('"', '')
        if 'audio' in mimeType:
            stream['audio_codec'] = re.findall('"[^"]*"', mimeTypeDetails[-1])[0].replace('"', '')
        try:
            stream['file_size'] = int(i['contentLength'])
        except KeyError:
            stream['file_size'] = int(streams.get_by_itag(itag).filesize)

        streamList.append(stream)

    for i in progressive:
        mimeTypeDetails = i['mimeType'].split(";")
        mimeType = mimeTypeDetails[0]
        itag = i['itag']
        fps = i['fps']
        res = i['qualityLabel']
        width =i['width']
        height = i['height']
        codecs = re.findall('"[^"]*"', mimeTypeDetails[-1])[0].replace('"', '').split(', ')
        video_codec = codecs[0]
        audio_codec = codecs[1]
        url = i['url']
        stream = {
            'itag': itag,
            'mime_type': mimeType,
            'fps': fps,
            'url':url,
            'resolution': res,
            'width': width,
            'height': height,
            'video_codec': video_codec,
            'audio_codec': audio_codec
        }

        try:
            stream['file_size'] = int(i['contentLength'])
        except KeyError:
            stream['file_size'] = int(streams.get_by_itag(itag).filesize)

        streamList.append(stream)

    return streamList
