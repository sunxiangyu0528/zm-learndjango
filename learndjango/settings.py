"""
Django settings for learndjango project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
import datetime
import sys
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@=qn*7qyve98$=)6csvv3(ex8%@=2hz2r4ik6nww))l$v#ny*l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['146.56.194.79', 'localhost', '0.0.0.0:8000', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'apps.projects.apps.ProjectsConfig',
    # 'apps.interfaces.apps.InterfacesConfig',
    # 'apps.user.apps.UserConfig',
    'rest_framework',
    'django_filters',
    'drf_yasg',
    'interfaces.apps.InterfacesConfig',
    'projects.apps.ProjectsConfig',
    'user.apps.UserConfig',
    'configures.apps.ConfiguresConfig',
    'debugtalks.apps.DebugtalksConfig',
    'envs.apps.EnvsConfig',
    'reports.apps.ReportsConfig',
    'testcases.apps.TestcasesConfig',
    'testsuits.apps.TestsuitsConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # 跨域设置
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'learndjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'learndjango.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        # 指定引擎
        'ENGINE': 'django.db.backends.mysql',
        # 指定数据库名称
        'NAME': 'study_happy',
        # 数据库用户
        'USER': 'root',
        # 数据库密码
        'PASSWORD': '123456',
        'HOST':'localhost',
        # 'HOST': '146.56.194.79',

        'PORT': '3306',
        # 'OPTIONS': {
        #     "init_command": "SET foreign_key_checks = 0;",
        # }
    }
}

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

LANGUAGE_CODE = 'zh-hans'

# TIME_ZONE = 'Asia/ShangHai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        # 设置排序过滤引擎
        'rest_framework.filters.OrderingFilter',
        # 设置查询过滤引擎
        'django_filters.rest_framework.backends.DjangoFilterBackend'
    ],
    # 在全局指定分页的引擎
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_PAGINATION_CLASS': 'utils.pagination.PageNumberPaginationManual',

    'PAGE_SIZE': 3,  # 每页数目,
    "DEFAULT_SCHEMA_CLASS": 'rest_framework.schemas.coreapi.AutoSchema',
    # "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated",],
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"],
    # "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAdminUser",],

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',  # 第一种jwt方式
        'rest_framework.authentication.BasicAuthentication',  # 基本认证
        'rest_framework.authentication.SessionAuthentication',  # session认证
    ),
}
ALLOWED_HOSTS = ["146.45.194.79", "localhost", "0.0.0.0:8000", "127.0.0.1"]

BASE_LOG_DIR = os.path.join(BASE_DIR, "logs")
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'standard': {
#             'format': '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]'
#                       '[%(levelname)s][%(message)s]'
#         },
#         'simple': {
#             'format': '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
#         },
#         'collect': {
#             'format': '%(message)s'
#         }
#     },
#     'filters': {
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue',
#         },
#     },
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'filters': ['require_debug_true'],  # 只有在Django debug为True时才在屏幕打印日志
#             'class': 'logging.StreamHandler',
#             'formatter': 'simple'
#         },
#         'SF': {
#             'level': 'INFO',
#             'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，根据文件大小自动切
#             'filename': os.path.join(BASE_LOG_DIR, "xxx_info.log"),  # 日志文件
#             'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
#             'backupCount': 3,  # 备份数为3  xx.log --> xx.log.1 --> xx.log.2 --> xx.log.3
#             'formatter': 'standard',
#             'encoding': 'utf-8',
#         },
#         'TF': {
#             'level': 'INFO',
#             'class': 'logging.handlers.TimedRotatingFileHandler',  # 保存到文件，根据时间自动切
#             'filename': os.path.join(BASE_LOG_DIR, "xxx_info.log"),  # 日志文件
#             'backupCount': 3,  # 备份数为3  xx.log --> xx.log.2018-08-23_00-00-00 --> xx.log.2018-08-24_00-00-00 --> ...
#             'when': 'D',  # 每天一切， 可选值有S/秒 M/分 H/小时 D/天 W0-W6/周(0=周一) midnight/如果没指定时间就默认在午夜
#             'formatter': 'standard',
#             'encoding': 'utf-8',
#         },
#         'error': {
#             'level': 'ERROR',
#             'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
#             'filename': os.path.join(BASE_LOG_DIR, "xxx_err.log"),  # 日志文件
#             'maxBytes': 1024 * 1024 * 5,  # 日志大小 50M
#             'backupCount': 5,
#             'formatter': 'standard',
#             'encoding': 'utf-8',
#         },
#         'collect': {
#             'level': 'INFO',
#             'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
#             'filename': os.path.join(BASE_LOG_DIR, "xxx_collect.log"),
#             'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
#             'backupCount': 5,
#             'formatter': 'collect',
#             'encoding': "utf-8"
#         }
#     },
#     'loggers': {
#         '': {  # 默认的logger应用如下配置
#             'handlers': ['SF', 'console', 'error'],  # 上线之后可以把'console'移除
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#         'collect': {  # 名为 'collect'的logger还单独处理
#             'handlers': ['console', 'collect'],
#             'level': 'INFO',
#         }
#     },
# }

STATIC_ROOT = os.path.join(BASE_DIR, 'front_ends/static')