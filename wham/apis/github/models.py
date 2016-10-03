from django.db import models
from wham.fields import (
    WhamCharField,
    WhamManyToManyField,
    WhamTextField,
    WhamURLField,
    WhamForeignKey,
    WhamIntegerField,
    WhamDateTimeField, WhamBooleanField)
from wham.models import WhamModel
from wham.utils import merge_dicts


class GithubMeta:
    base_url = 'https://api.github.com/'
    # auth_for_public_get = 'API_KEY'
    # api_key_settings_name = 'LASTFM_API_KEY'
    # params = {
    #     'format': 'json',
        #'limit': 500, #disabled as it breaks the mock test
    # }

# class LastFmTrack(WhamModel):
#
#     objects = WhamManager()
#
#     id = WhamCharField(max_length=255, primary_key=True)
#     name = WhamTextField()
#     listeners = WhamIntegerField()
#     playcount = WhamIntegerField()
#     duration = WhamIntegerField()
#
#     class Meta:
#         db_table = 'lastfm_track'
#
#     class WhamMeta(LastFmMeta):
#         endpoint = ''
#         params = {'method': 'track.getInfo'}
#
#     def __unicode__(self):
#         return self.name


class Repository(WhamModel):
    id = WhamCharField(max_length=255, primary_key=True)
    name = WhamCharField(max_length=255)
    full_name = WhamTextField()
    html_url = WhamURLField()
    description = WhamTextField(null=True)
    url = WhamURLField()
    stargazers_count = WhamIntegerField()
    watchers_count = WhamIntegerField()
    forks_count = WhamIntegerField()
    open_issues_count = WhamIntegerField()
    has_issues = WhamBooleanField()
    language = WhamCharField(max_length=255, null=True)

    created_at = WhamDateTimeField(wham_format='iso8601')
    updated_at = WhamDateTimeField(wham_format='iso8601')
    pushed_at = WhamDateTimeField(wham_format='iso8601')

    size = WhamIntegerField()


    # "created_at": "2011-01-26T19:01:12Z",
    # "updated_at": "2011-01-26T19:14:43Z",


    class WhamMeta(GithubMeta):
        endpoint = 'repositories'

        class Filter:
            endpoint = 'search/repositories'
            filters = [
                {
                    'field': 'language',
                    'querystring_param': 'q',
                    'querystring_value_prefix': 'language:',
                }
            ]
            results_path = ('items',)


# class LastFmUser(WhamModel):
#
#     name = WhamCharField(max_length=255, primary_key=True)
#
#     top_artists = WhamManyToManyField(
#         #http://ws.audioscrobbler.com/2.0/?method=user.gettopartists&user=rj&api_key=a04961fe4330211ff149a949dfabef51&format=json
#         'LastFmArtist',
#         through='LastFmUserTopArtists',
#         wham_endpoint='',
#         wham_pk_param='user',
#         wham_params={'method': 'user.gettopartists'},
#         wham_results_path=('topartists', 'artist')
#     )
#
#     class Meta:
#         db_table = 'lastfm_user'
#
#     class WhamMeta(LastFmMeta):
#         endpoint = ''
#         detail_base_result_path = ('user',)
#         params = merge_dicts(LastFmMeta.params, {'method': 'user.getInfo'})
#         url_pk_type = 'querystring'
#         url_pk_param = 'user'
#
#     def __unicode__(self):
#         return self.name
#
#
# class LastFmArtist(WhamModel):
#
#     name = WhamTextField(primary_key=True)
#     mega_image_url = WhamURLField(wham_result_path=('image', 4, '#text'))
#
#     mbid = WhamCharField(max_length=255, null=True, wham_can_lookup=True) #this *would* be unique & not nullable, but lasfm doesn't always know it
#
#     class Meta:
#         db_table = 'lastfm_artist'
#
#     class WhamMeta(LastFmMeta):
#         endpoint = ''
#         params = merge_dicts(LastFmMeta.params, {'method': 'artist.getInfo'})
#         detail_base_result_path = ('artist',)
#         url_pk_type = 'querystring'
#         url_pk_param = 'artist'
#
#     def __unicode__(self):
#         return self.name
#
#
#
# class LastFmUserTopArtists(models.Model):
#     user = WhamForeignKey(LastFmUser, related_name='')
#     artist = WhamForeignKey(LastFmArtist)
#     playcount = WhamCharField(max_length=255)
#
#     class Meta:
#         ordering = ('-playcount',)