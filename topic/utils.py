import os
import zipfile
import asyncio

from docker import DockerClient

from topic.dockerManager.DockerFileController import DockerFileController

# from .models import Topic
from topic.models import Topic


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
    return DockerClient(base_url='tcp://127.0.0.1:2375').containers.get(container_id).status


def build_images(topic: Topic):
    # Dockerfile

    d = DockerFileController()
    docker_file_dir = os.path.join(os.path.dirname(topic.zip_file.path), topic.build_name)
    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)
    # loop.run_until_complete(d.buildImageWithLog())
    # loop.close()
    d.buildImageWithLog()
    # d.buildImage(docker_file_dir, topic.build_name)


async def test():
    print(123)


if __name__ == '__main__':
    print(123)
    # un_zip('storage/docker/fb1b3bdc-4fc8-11e9-9fc2-b025aa148d03/qq.zip', 'tt')
    # t = Topic.objects.get(id=1)
    # print(t)
    # build_images('13')
