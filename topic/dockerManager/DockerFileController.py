import json
import os
from docker import DockerClient, APIClient


class DockerFileController:
    def __init__(self):
        self.client = DockerClient(base_url='tcp://127.0.0.1:2375')

    def showRunningContainers(self):
        return self.client.containers()

    def buildImage(self, path, tag):
        # path = os.path.join(os.getcwd(), 'files', dir_name)
        self.client.build(path=path, tag=tag)

    def showImages(self):
        return self.client.images()

    def runContainer(self, image, build_name, command=None):
        container = self.client.containers.run(image=image, ports={'8000/tcp': 3333},
                                               name=build_name, command=command, detach=True)

        print(container.logs)
        # print(container.short_id)
        # container = self.client.create_container(
        #     tag_name, ports=[1111, 2222],
        #     host_config=self.client.create_host_config(
        #         port_bindings={
        #             1111: 4567,
        #             2222: None
        #         }
        #     )
        # )
        # print(self.client.logs(container))
        # print(container.log)
        # print(container)

    def getContainerStatus(self, container_id):
        return self.client.containers.get(container_id).status


if __name__ == '__main__':
    d = DockerFileController()
    # d.runContainer()
    # print(d.getContainerStatus('17b2884cbd10'))
    # d.runContainers('django:1.9.1-python3')
    # d.runContainersWithId('123', '123', 'python /usr/src/nuckaggle/manage.py runserver 0.0.0.0:8000')
    # d.buildImageWithLog()
