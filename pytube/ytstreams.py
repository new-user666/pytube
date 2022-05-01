# This module is made for getting json of yt video details
def get_streams(YouTube):
    """
    YouTube : Youtube object
        from pytube.ytstreams import get_streams
        yt = YouTube(yt_url)
        get_streams(yt)
    """

    qualities = YouTube.vid_info['streamingData']
    dash = qualities['adaptiveFormats']
    progressive = qualities['formats']
    streamList = []
    for i in dash:
        mimeType = i['mimeType']
        itag = i['itag']
        stream = {
            'itag': itag,
            'mime_type': mimeType
        }

        if 'video' in mimeType:
            stream['fps'] = i['fps']
            stream['resolution'] = i['qualityLabel']
            stream['pixel_size'] = f"{i['width']}x{i['height']}"
        try:
            stream['file_size'] = int(i['contentLength'])
        except KeyError:
            pass

        streamList.append(stream)

    for i in progressive:
        mimeType = i['mimeType']
        itag = i['itag']
        fps = i['fps']
        res = i['qualityLabel']
        pixelsize = f"{i['width']}x{i['height']}"
        stream = {
            'itag': itag,
            'mime_type': mimeType,
            'fps': fps,
            'resolution': res,
            'pixel_size': pixelsize
        }

        try:
            stream['file_size'] = int(i['contentLength'])
        except KeyError:
            pass

        streamList.append(stream)

    return streamList
