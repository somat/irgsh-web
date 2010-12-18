from django.conf.urls.defaults import *

TASK_ID_PATTERN = '(?P<task_id>[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})'

urlpatterns = patterns('irgsh_web.build.views',
    url(r'^%s/info/' % TASK_ID, 'debian_info', name='build_debian_info'),
    url(r'^%s/built/' % TASK_ID, 'report_built', name='build_report_built'),
    url(r'^%s/uploaded/' % TASK_ID, 'report_uploaded', name='build_report_uploaded'),
    url(r'^%s/' % TASK_ID, 'show', name='build_show'),
    url(r'^$', 'index', name='build_index'),
)

