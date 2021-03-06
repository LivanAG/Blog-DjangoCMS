import os  # isort:skip
gettext = lambda s: s

"""
Django settings for Asiel project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import django_heroku
import dropbox

from dropbox import common,users,users_common
# Build paths inside the project like this: BASE_DIR / 'subdir'.


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$b=azy(g2retcx!1%po^b!n=&$*4tgc$l-%=v259zaf55%h)_i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
'https://shuman-blog.herokuapp.com/',
'https://shuman-blog.herokuapp.com',
'shuman-blog.herokuapp.com',
'localhost',
'127.0.0.1']


# Application definition

ROOT_URLCONF = 'Asiel.urls'



WSGI_APPLICATION = 'Asiel.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Havana'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.dirname(os.path.dirname(__file__))






SITE_ID = 3


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'Asiel', 'templates'),],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
                'cms.context_processors.cms_settings'
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader'
            ],
        },
    },
]


MIDDLEWARE = [
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    # whitenoise
    #'whitenoise.middleware.WhiteNoiseMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
]

INSTALLED_APPS = [
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'registration',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'filer',
    'easy_thumbnails',
    'djangocms_bootstrap4',
    'djangocms_bootstrap4.contrib.bootstrap4_alerts',
    'djangocms_bootstrap4.contrib.bootstrap4_badge',
    'djangocms_bootstrap4.contrib.bootstrap4_card',
    'djangocms_bootstrap4.contrib.bootstrap4_carousel',
    'djangocms_bootstrap4.contrib.bootstrap4_collapse',
    'djangocms_bootstrap4.contrib.bootstrap4_content',
    'djangocms_bootstrap4.contrib.bootstrap4_grid',
    'djangocms_bootstrap4.contrib.bootstrap4_jumbotron',
    'djangocms_bootstrap4.contrib.bootstrap4_link',
    'djangocms_bootstrap4.contrib.bootstrap4_listgroup',
    'djangocms_bootstrap4.contrib.bootstrap4_media',
    'djangocms_bootstrap4.contrib.bootstrap4_picture',
    'djangocms_bootstrap4.contrib.bootstrap4_tabs',
    'djangocms_bootstrap4.contrib.bootstrap4_utilities',
    'djangocms_file',
    'djangocms_icon',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_style',
    'djangocms_googlemap',
    'djangocms_video',
    'widget_tweaks',
    'Asiel',
    
    # Cookies
    'cookielaw',

    # django-newsletter y dependencias
    'sorl.thumbnail',
    'newsletter',

    
    # djangocms-blog y dependencias
    'aldryn_apphooks_config',
    'parler',
    'taggit',
    'taggit_autosuggest',
    'meta',
    'sortedm2m',
    'djangocms_blog',

    # django_comments_xtd y dependencias
    'django_comments_xtd',
    'django_comments',

    # django-check-seo
    "django_check_seo",
    
 
]








DROPBOX_OAUTH2_TOKEN = '1EsWTmpuLSUAAAAAAAAAAcXv1CjDNcDOrrVe2PIXu6-DU8WMXZfWDL3wug3JsqKX'
DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'


dbx = dropbox.Dropbox (DROPBOX_OAUTH2_TOKEN)
DROPBOX_ROOT_PATH = '/media/'




STATIC_URL = '/static/'
#MEDIA_URL = '/media/'
#MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')


LANGUAGES = (
    ## Customize this
    ('es', gettext('es')),
)

CMS_LANGUAGES = {
    ## Customize this
    1: [
        {
            'code': 'es',
            'name': gettext('es'),
            'redirect_on_fallback': True,
            'public': True,
            'hide_untranslated': False,
        },
    ],
    'default': {
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': False,
    },
}

CMS_TEMPLATES = (
    ## Customize this
    ('fullwidth.html', 'Fullwidth'),
    ('sidebar_left.html', 'Sidebar Left'),
    ('sidebar_right.html', 'Sidebar Right'),
    ('home.html', 'Home'),
    ('contacto.html', 'Contacto'),
    ('blog_principal.html', 'Blog')
)

X_FRAME_OPTIONS = 'SAMEORIGIN'

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': 'localhost',
        'NAME': 'project.db',
        'PASSWORD': '',
        'PORT': '',
        'USER': ''
    }
}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

META_SITE_PROTOCOL = 'https'  # set 'http' for non ssl enabled websites
META_USE_SITES = True


META_USE_OG_PROPERTIES=True
META_USE_TWITTER_PROPERTIES=True
META_USE_GOOGLEPLUS_PROPERTIES=True # django-meta 1.x+
META_USE_SCHEMAORG_PROPERTIES=True  # django-meta 2.x+


LOGIN_REDIRECT_URL = '/'


LOGOUT_REDIRECT_URL = '/'




#------------------ Configuracion Email--------------------------------------------------------------------------------------

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST="smtp.gmail.com"
EMAIL_USE_TLS=True
EMAIL_PORT = 587
EMAIL_HOST_USER="marcelosking00@gmail.com"
EMAIL_HOST_PASSWORD="zgbzmpcpinhoqsvn"


#------------------ END Configuracion Email--------------------------------------------------------------------------------------







#------------------ Configuracion NEWSLETTER--------------------------------------------------------------------------------------
NEWSLETTER_CONFIRM_EMAIL = True

# Amount of seconds to wait between each email. Here 100ms is used.
NEWSLETTER_EMAIL_DELAY = 0.1

# Amount of seconds to wait between each batch. Here one minute is used.
NEWSLETTER_BATCH_DELAY = 60

# Number of emails in one batch
NEWSLETTER_BATCH_SIZE = 100

#------------------ END Configuracion NEWSLETTER--------------------------------------------------------------------------------------






#------------------ Configuracion Comments--------------------------------------------------------------------------------------

COMMENTS_APP='django_comments_xtd'

COMMENTS_XTD_CONFIRM_EMAIL = True

COMMENTS_XTD_MAX_THREAD_LEVEL =10
COMMENTS_XTD_LIST_ORDER = ('-thread_id', 'order')  # default is ('thread_id', 'order')


COMMENTS_XTD_APP_MODEL_OPTIONS = {
    'default': {
        'allow_flagging': True,
        'allow_feedback': True,
        'show_feedback': False,
        'who_can_post': 'all'  # Valid values: 'all', users'
    }
}
#------------------END Configuracion Comments--------------------------------------------------------------------------------------


#------------------ Configuracion Django Registrations--------------------------------------------------------------------------------------

ACCOUNT_ACTIVATION_DAYS = 7

#------------------ END Configuracion Django Registrations--------------------------------------------------------------------------------------





#------------------ Configuracion Blog--------------------------------------------------------------------------------------


BLOG_PLUGIN_TEMPLATE_FOLDERS = (
    ('plugins', 'Default_template'),    
    ('Plugins_barra_nav_blog', 'Barra Navegacion Vertical'),    
    ('Plugins_home', 'Home'),

)


#------------------ END Configuracion Blog--------------------------------------------------------------------------------------




#------------------ Configuracion Filer--------------------------------------------------------------------------------------




FILER_ENABLE_PERMISSIONS=False

FILER_ALLOW_REGULAR_USERS_TO_ADD_ROOT_FOLDERS=True

FILER_STORAGES = {
    'public': {
        'main': {
            'ENGINE': DEFAULT_FILE_STORAGE,
            'OPTIONS': {
                #'location': MEDIA_ROOT,
                #'base_url': MEDIA_URL,
            },
            'UPLOAD_TO': 'filer.utils.generate_filename.randomized',
            'UPLOAD_TO_PREFIX': 'filer_public',
        },
        'thumbnails': {
            'ENGINE': DEFAULT_FILE_STORAGE,
            'OPTIONS': {
                #'location':MEDIA_ROOT,
                #'base_url': MEDIA_URL,
            },
            'UPLOAD_TO_PREFIX': 'filer_public_thumbnails',
            
        },
    },
  
}


#------------------ END Configuracion Filer--------------------------------------------------------------------------------------




#------------------ END Configuracion Django Registration--------------------------------------------------------------------------------------


REGISTRATION_FORM = 'Asiel.forms.CustomForm'
#------------------ Configuracion Django Registration--------------------------------------------------------------------------------------



#------------------ Configuracion OTRAS--------------------------------------------------------------------------------------


NOMBRE_DEL_BLOG = 'Shuman'

#------------------ END Configuracion OTRAS--------------------------------------------------------------------------------------



#------------------ END Configuracion SEO--------------------------------------------------------------------------------------
DJANGO_CHECK_SEO_FORCE_HTTP = True


DJANGO_CHECK_SEO_SETTINGS  =  { 
    "content_words_number" :  [ 300 ,  600 ], 
    "internal_links" :  1 , 
    "external_links" :  1 , 
    "meta_title_length" :  [ 1 ,  40 ], 
    "meta_description_length" :  [ 50 ,  160 ], 
    "keywords_in_first_words" :  50 , 
    "max_link_depth" :  3 , 
    "max_url_length" :  70 , 
}
#------------------ END Configuracion SEO--------------------------------------------------------------------------------------




# Activa Django-Heroku.
django_heroku.settings(locals())
