# coding=utf-8

from __future__ import unicode_literals
import requests
import json


def game_video_list(game):
    """ Get channel's upload videos| 50 limit"""

    youtube_link = {ссылка на канал вводится пользователем}

    # отрезаем id канала
    CHANNEL_ID = game.channel.rsplit('/', 1)[-1]

    try:
        YOUTUBE_URI = 'https://www.googleapis.com/youtube/v3/search?key={}&channelId={}&part=snippet,id&order=date&maxResults=50'
        FORMAT_YOUTUBE_URI = YOUTUBE_URI.format( YOUTUBE_API_KEY, CHANNEL_ID)

        content = requests.get(FORMAT_YOUTUBE_URI).text
        data = json.loads(content)

        video_list =[]
        keys = 'id', 'title', 'description', 'preview'

        for item in data.get('items'):
            id = item.get('id').get('videoId')
            title = item.get('snippet').get('title')
            description = item.get('snippet').get('description')
            preview = item.get('snippet').get('thumbnails').get('high').get('url')

            values = id, title, description, preview

            if id:
                video_item =dict(zip(keys, values))
                video_list.append(video_item)

        return video_list
    except:
        return {}