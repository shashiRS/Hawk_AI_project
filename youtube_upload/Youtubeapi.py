import argparse
import scrapy
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = 'AIzaSyCpHvN2US2sGJnIHDS9GmOO0s7rzVOm3Y4'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
class QuotesSpider(scrapy.Spider):
  name = "youtubespider"
  parser = argparse.ArgumentParser()
  parser.add_argument('--q', help='search term', default='prestige misty water')
  parser.add_argument('20', help='Max results', default=20)
  args = parser.parse_args()

  try:
    youtube_search(args)
  except HttpError, e:
    print 'An HTTP error %d occurred:\n%s' % (e.resp.status, e.content)
  def youtube_search(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
      developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
      q=options.q,
      part='id,snippet',
      maxResults=options.max_results
    ).execute()

    videos = []
    channels = []
    playlists = []
    # print(search_response)
    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    for search_result in search_response.get('items', []):
      if search_result['id']['kind'] == 'youtube#video':
        videos.append('%s (%s)' % (search_result['snippet']['title'],
                                   search_result['snippet']['description'],
                                  ))
        print('URL of thumbnails: '+search_result['snippet']['thumbnails']['default']['url'])
        print('TITLE: '+search_result['snippet']['title'])

        print('DESCRIPTION: '+search_result['snippet']['description'])
        print('DOMAIN: '+search_result['snippet']['channelTitle'])
        print('PUBLISHED: '+search_result['snippet']['publishedAt'])
      elif search_result['id']['kind'] == 'youtube#channel':
        channels.append('%s (%s)' % (search_result['snippet']['title'],
                                     search_result['id']['channelId']))
      elif search_result['id']['kind'] == 'youtube#playlist':
        playlists.append('%s (%s)' % (search_result['snippet']['title'],
                                      search_result['id']['playlistId']))
 
  # print 'Videos:\n', '\n'.join(videos), '\n'
  # print 'Channels:\n', '\n'.join(channels), '\n'
  # print 'Playlists:\n', '\n'.join(playlists), '\n'


