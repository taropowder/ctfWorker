import os
import subprocess


class DockerComposeController:
    def __init__(self, path, uuid=None):
        self.topic_dir = os.path.join(os.getcwd(), 'files', path)
        print(self.topic_dir)
        yml_file = f"-f {self.topic_dir}/docker-compose.yml"
        project_name = f"-p {uuid}"
        directory = f"--project-directory {self.topic_dir}/"
        cmd1 = "cd ~"
        if uuid:
            cmd2 = f"docker-compose {yml_file} {project_name} {directory} "
        else:
            cmd2 = f"docker-compose {yml_file} {directory} "
        self.base_cmd = cmd1 + " && " + cmd2


    def docker_compose_ps(self):
        cmd = self.base_cmd + 'ps'
        result = self._exec_docker_compose(cmd)
        print(result.split(b'   '))

    def docker_compose_up(self, port):
        with open(os.path.join(self.topic_dir, '.env'), 'w') as f:
            f.write(f'ports={port}')

        cmd = self.base_cmd + 'up -d'
        p = self._exec_docker_compose(cmd)
        print(p)

    def docker_compose_down(self):
        cmd = self.base_cmd + 'down'
        p = self._exec_docker_compose(cmd)
        print(p)

    def _exec_docker_compose(self, cmd):
        p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        return p.stdout.read()


if __name__ == '__main__':
    dc = DockerComposeController('nucKaggle', 'uuid')
    # dc.docker_compose_up(2333)
    dc.docker_compose_ps()
    dc.docker_compose_down()
