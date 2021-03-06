import os
import zipfile
import socket

from random import randint
from docker import DockerClient

# from topic.dockerManager.DockerFileController import DockerFileController

# from .models import Topic
from docker.errors import NotFound

from topic.models import Topic
from accounts.models import TopicInstance


def un_zip(file_name, project_name):
    """unzip zip file"""
    zip_file = zipfile.ZipFile(file_name)
    zip_dir = os.path.join(os.path.dirname(file_name), project_name)
    if os.path.isdir(zip_dir):
        pass
    else:
        os.mkdir(zip_dir)
    for names in zip_file.namelist():
        zip_file.extract(names, zip_dir)
    zip_file.close()


def getContainerStatus(container_id):
    try:
        result = DockerClient(base_url='tcp://127.0.0.1:2375').containers.get(container_id).status
    except NotFound as e:
        result = "容器运行失败"
    return result


def runContainerFromDockerFile(topic: Topic, team=None):
    result = {'tile': topic.title, 'status': '题目开启成功'}
    instance = TopicInstance()
    port = randint(10240, 65534)
    while is_used(port):
        port = randint(10240, 65534)
    instance.team = team
    instance.port = port
    instance.topic = topic
    client = DockerClient(base_url='tcp://127.0.0.1:2375')
    container = client.containers.run(image=topic.build_name, ports={f'{topic.port}/tcp': instance.port},
                                      name=topic.build_name, command=topic.exec_command, detach=True)
    instance.container_id = container.short_id
    instance.flag = topic.flag
    instance.save()
    result['message'] = f"{topic.title} 已成功开启，端口为{port}"
    return result


def removeContainerFromDockerFile(topic_id: int):
    client = DockerClient(base_url='tcp://127.0.0.1:2375')
    instances = TopicInstance.objects.filter(topic_id=topic_id)
    for instance in instances:
        try:
            client.containers.get(instance.container_id).remove(force=True)
        except NotFound as e:
            print("容器不存在")
        instance.delete()


def is_used(port):
    ip = '127.0.0.1'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, int(port)))
        s.shutdown(2)
        return True
    except:
        return False


if __name__ == '__main__':
    is_used(80)
    # print(123)
    # un_zip('storage/docker/fb1b3bdc-4fc8-11e9-9fc2-b025aa148d03/qq.zip', 'tt')
    # t = Topic.objects.get(id=1)
    # print(t)
    # build_images('13')
