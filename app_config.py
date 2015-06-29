#!/usr/bin/env python

"""
Project-wide application configuration.

DO NOT STORE SECRETS, PASSWORDS, ETC. IN THIS FILE.
They will be exposed to users. Use environment variables instead.
See get_secrets() below for a fast way to access them.
"""

import os

from authomatic.providers import oauth2
from authomatic import Authomatic


"""
NAMES
"""
# Project name to be used in urls
# Use dashes, not underscores!
PROJECT_SLUG = 'best-songs-2015-so-far'
# PROJECT_SLUG = 'miller'


# Project name to be used in file paths
PROJECT_FILENAME = 'bestsongs15_midyear'

# The name of the repository containing the source
REPOSITORY_NAME = 'bestsongs15-midyear'
GITHUB_USERNAME = 'nprapps'
REPOSITORY_URL = 'git@github.com:%s/%s.git' % (GITHUB_USERNAME, REPOSITORY_NAME)
REPOSITORY_ALT_URL = None # 'git@bitbucket.org:nprapps/%s.git' % REPOSITORY_NAME'

# Project name used for assets rig
# Should stay the same, even if PROJECT_SLUG changes
ASSETS_SLUG = 'bestsongs15-midyear'

"""
DEPLOYMENT
"""
PRODUCTION_S3_BUCKET = {
    'bucket_name': 'apps.npr.org',
    'region': 'us-east-1'
}

STAGING_S3_BUCKET = {
    'bucket_name': 'stage-apps.npr.org',
    'region': 'us-east-1'
}

ASSETS_S3_BUCKET = {
    'bucket_name': 'assets.apps.npr.org',
    'region': 'us-east-1'
}

DEFAULT_MAX_AGE = 20

PRODUCTION_SERVERS = ['cron.nprapps.org']
STAGING_SERVERS = ['cron-staging.nprapps.org']

# Should code be deployed to the web/cron servers?
DEPLOY_TO_SERVERS = False

SERVER_USER = 'ubuntu'
SERVER_PYTHON = 'python2.7'
SERVER_PROJECT_PATH = '/home/%s/apps/%s' % (SERVER_USER, PROJECT_FILENAME)
SERVER_REPOSITORY_PATH = '%s/repository' % SERVER_PROJECT_PATH
SERVER_VIRTUALENV_PATH = '%s/virtualenv' % SERVER_PROJECT_PATH

# Should the crontab file be installed on the servers?
# If True, DEPLOY_TO_SERVERS must also be True
DEPLOY_CRONTAB = False

# Should the service configurations be installed on the servers?
# If True, DEPLOY_TO_SERVERS must also be True
DEPLOY_SERVICES = False

UWSGI_SOCKET_PATH = '/tmp/%s.uwsgi.sock' % PROJECT_FILENAME

# Services are the server-side services we want to enable and configure.
# A three-tuple following this format:
# (service name, service deployment path, service config file extension)
SERVER_SERVICES = [
    ('app', SERVER_REPOSITORY_PATH, 'ini'),
    ('uwsgi', '/etc/init', 'conf'),
    ('nginx', '/etc/nginx/locations-enabled', 'conf'),
]

# These variables will be set at runtime. See configure_targets() below
S3_BUCKET = None
S3_BASE_URL = None
S3_DEPLOY_URL = None
SERVERS = []
SERVER_BASE_URL = None
SERVER_LOG_PATH = None
DEBUG = True

"""
COPY EDITING
"""
COPY_GOOGLE_DOC_KEY = '1bR-KYOP7M5Y4DgEr4lvHwwEPIa3171FR5CIAr3PFagU'
COPY_PATH = 'data/copy.xlsx'

"""
SONG DATA
"""
SONGS_GOOGLE_DOC_KEY = '1Egm-N9uQBAAq6aEAZEJKB-iwd2TPlZFzHK9H2MHONbg'
SONGS_CSV_DATA_PATH = 'data/songs.csv'

"""
SHARING
"""
SHARE_URL = 'http://%s/%s/' % (PRODUCTION_S3_BUCKET['bucket_name'], PROJECT_SLUG)

"""
ADS
"""

NPR_DFP = {
    'STORY_ID': '1002',
    'TARGET': 'homepage',
    'ENVIRONMENT': 'NPRTEST',
    'TESTSERVER': 'false'
}

"""
SERVICES
"""
NPR_GOOGLE_ANALYTICS = {
    'ACCOUNT_ID': 'UA-5828686-4',
    'DOMAIN': PRODUCTION_S3_BUCKET['bucket_name'],
    'TOPICS': '' # e.g. '[1014,3,1003,1002,1001]'
}

VIZ_GOOGLE_ANALYTICS = {
    'ACCOUNT_ID': 'UA-5828686-75'
}

DISQUS_API_KEY = 'tIbSzEhGBE9NIptbnQWn4wy1gZ546CsQ2IHHtxJiYAceyyPoAkDkVnQfCifmCaQW'
DISQUS_UUID = '9aa466a3-03aa-11e5-a407-80e6500ab74c'

"""
OAUTH
"""

GOOGLE_OAUTH_CREDENTIALS_PATH = '~/.google_oauth_credentials'

authomatic_config = {
    'google': {
        'id': 1,
        'class_': oauth2.Google,
        'consumer_key': os.environ.get('GOOGLE_OAUTH_CLIENT_ID'),
        'consumer_secret': os.environ.get('GOOGLE_OAUTH_CONSUMER_SECRET'),
        'scope': ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/userinfo.email'],
        'offline': True,
    },
}

authomatic = Authomatic(authomatic_config, os.environ.get('AUTHOMATIC_SALT'))

"""
SONGZ
"""
GENRE_TAGS = [
    'Classical',
    'Country/Americana',
    'Electronic',
    'Hip-Hop',
    'Jazz',
    'Latin',
    'Pop',
    'R&B',
    'Rock',
    '\m/ >_< \m/',
    'World'
]

REVIEWER_TAGS = [
    'Bob Boilen',
    'Ann Powers',
    'Ali Shaheed Muhammad',

    'Jason King',
    'David Dye',
    'Rita Houston',

    'Anastasia Tsioulcas',
    'Felix Contreras',
    'Kevin Cole'
]

REVIEWER_IMAGES = {
    # With playlists
    'Bob Boilen': 'bob.jpg',
    'Ann Powers': 'ann.jpg',
    'Ali Shaheed Muhammad': 'ali.jpg',
    'Jason King': 'jason-king.jpg',
    'David Dye': 'david-dye.jpg',
    'Rita Houston': 'rita-houst.jpg',
    'Anastasia Tsioulcas': 'tsioulcas.jpg',
    'Felix Contreras': 'contreras.jpg',
    'Kevin Cole': 'kevin-cole.jpg'
}

REVIEWER_BIOS = {
    'Bob Boilen': 'Co-host of All Songs Considered ',
    'Ann Powers': 'Pop Critic for NPR Music',
    'Ali Shaheed Muhammad': 'Host of NPR Music&rsquo;s Microphone Check',
    'Jason King': 'Host of NPR R&B',
    'David Dye': 'Host of NPR&rsquo;s World Cafe',
    'Rita Houston': 'Program Director at WFUV in New York City',
    'Anastasia Tsioulcas': 'Co-host of NPR Classical',
    'Felix Contreras': 'Co-host of NPR Music&rsquo;s Alt.Latino',
    'Kevin Cole': 'Program Director at KEXP in Seattle'
}

WELCOME_AUDIO = '/npr/specialmusic/2014/12/20141208_specialmusic_welcome.mp3'

TAG_AUDIO_INTROS = {
    'Bob Boilen': '/npr/specialmusic/2015/06/20150626_specialmusic_bobboilen.mp3',
    'Ann Powers': '/npr/specialmusic/2015/06/20150626_specialmusic_annpowers.mp3',
    'Ali Shaheed Muhammad': '/npr/specialmusic/2015/06/20150626_specialmusic_alishaheedmuhammad.mp3',
    'Jason King': '/npr/specialmusic/2015/06/20150626_specialmusic_jasonking.mp3',
    'David Dye': '/npr/specialmusic/2015/06/20150626_specialmusic_daviddye.mp3',
    'Rita Houston': '/npr/specialmusic/npr/specialmusic/2015/06/20150626_specialmusic_ritahouston.mp3',
    'Anastasia Tsioulcas': '/npr/specialmusic/2015/06/20150626_specialmusic_anastasiatsioulcas.mp3',
    'Felix Contreras': '/npr/specialmusic/2015/06/20150626_specialmusic_felixc.mp3',
    'Kevin Cole': '/npr/specialmusic/npr/specialmusic/2015/06/20150626_specialmusic_kevincole.mp3'
}

SKIP_LIMIT = 6


"""
Utilities
"""
def get_secrets():
    """
    A method for accessing our secrets.
    """
    secrets_dict = {}

    for k,v in os.environ.items():
        if k.startswith(PROJECT_SLUG):
            k = k[len(PROJECT_SLUG) + 1:]
            secrets_dict[k] = v

    return secrets_dict

def configure_targets(deployment_target):
    """
    Configure deployment targets. Abstracted so this can be
    overriden for rendering before deployment.
    """
    global S3_BUCKET
    global S3_BASE_URL
    global S3_DEPLOY_URL
    global SERVERS
    global SERVER_BASE_URL
    global SERVER_LOG_PATH
    global DEBUG
    global DEPLOYMENT_TARGET
    global DISQUS_SHORTNAME
    global ASSETS_MAX_AGE

    if deployment_target == 'production':
        S3_BUCKET = PRODUCTION_S3_BUCKET
        S3_BASE_URL = 'http://%s/%s' % (S3_BUCKET['bucket_name'], PROJECT_SLUG)
        S3_DEPLOY_URL = 's3://%s/%s' % (S3_BUCKET['bucket_name'], PROJECT_SLUG)
        SERVERS = PRODUCTION_SERVERS
        SERVER_BASE_URL = 'http://%s/%s' % (SERVERS[0], PROJECT_SLUG)
        SERVER_LOG_PATH = '/var/log/%s' % PROJECT_FILENAME
        DISQUS_SHORTNAME = 'npr-news'
        DEBUG = False
        ASSETS_MAX_AGE = 86400
    elif deployment_target == 'staging':
        S3_BUCKET = STAGING_S3_BUCKET
        S3_BASE_URL = 'http://%s/%s' % (S3_BUCKET['bucket_name'], PROJECT_SLUG)
        S3_DEPLOY_URL = 's3://%s/%s' % (S3_BUCKET['bucket_name'], PROJECT_SLUG)
        SERVERS = STAGING_SERVERS
        SERVER_BASE_URL = 'http://%s/%s' % (SERVERS[0], PROJECT_SLUG)
        SERVER_LOG_PATH = '/var/log/%s' % PROJECT_FILENAME
        DISQUS_SHORTNAME = 'nprviz-test'
        DEBUG = True
        ASSETS_MAX_AGE = 20
    else:
        S3_BUCKET = None
        S3_BASE_URL = 'http://127.0.0.1:8000'
        S3_DEPLOY_URL = None
        SERVERS = []
        SERVER_BASE_URL = 'http://127.0.0.1:8001/%s' % PROJECT_SLUG
        SERVER_LOG_PATH = '/tmp'
        DISQUS_SHORTNAME = 'nprviz-test'
        DEBUG = True
        ASSETS_MAX_AGE = 20

    DEPLOYMENT_TARGET = deployment_target

"""
Run automated configuration
"""
DEPLOYMENT_TARGET = os.environ.get('DEPLOYMENT_TARGET', None)

configure_targets(DEPLOYMENT_TARGET)
