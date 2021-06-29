import django


major, minor, _ = (int(i) for i in django.__version__.split('.'))

if major < 3 or (major == 3 and minor < 2):
    # this is deprecated in 3.2 and removed in 4.1
    default_app_config = "oauth2_provider_jwt.apps.AppConfig"
