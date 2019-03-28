from __future__ import absolute_import

import json
import os

from celery import shared_task
from docker import APIClient

from topic.models import Topic

# celery worker -A topic -l info

@shared_task
def build_images(id):
    # Dockerfile
    t = Topic.objects.get(id=id)
    docker_file_dir = os.path.join(os.path.dirname(t.zip_file.path), t.build_name)
    docker_client = APIClient(base_url='tcp://127.0.0.1:2375')
    generator = docker_client.build(path=docker_file_dir,
                                    tag=t.build_name, rm=True)
    t.build_log = ""
    t.build_status = "building"
    t.save()
    status = True
    for g in generator:
        g = str(g, encoding="utf-8")
        g = json.loads(g)
        if 'stream' in g:
            g = g['stream']
        elif 'errorDetail' in g:
            status = False
            g = g['errorDetail']
        elif 'aux' in g:
            # 容器ＩＤ
            g = g['aux']['ID']
        t.build_log += g
        t.save()
    if status:
        t.build_status = 'success'
    else:
        t.build_status = 'fail'
    t.save()
