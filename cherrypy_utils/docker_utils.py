import os
import pathlib
import datetime


def get_version_number():
    return datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")


def build_docker_container(
    container_name,
    version_number,
    mount=True,
    mount_source="/home/mraUser/online_experiments_data",
    mount_folder="",
    mount_destination="/online_experiments_data",
    restart_policy="always",
    port_mappings=None,
):
    os.system("docker stop {0}".format(container_name))
    os.system("docker rm {0}".format(container_name))
    os.system("docker container prune --force")
    os.system("docker image prune --all --force --filter until=700h")
    os.system("docker build --network=host -t {1}:{0} .".format(version_number, container_name.replace("_", "-")))
    run_args = [
        "docker",
        "run",
        # '--mount type=bind,source="{0}",target={1}'.format(pathlib.Path(mount_source, mount_folder), mount_destination),
        "-d",
        "--restart {0}".format(restart_policy),
        "--name {0}".format(container_name),
        "{1}:{0}".format(version_number, container_name.replace("_", "-")),
    ]

    if mount:
        run_args.insert(
            2,
            '--mount type=bind,source="{0}",target={1}'.format(
                pathlib.Path(mount_source, mount_folder), mount_destination
            ),
        )

    if port_mappings:
        mapping = " ".join(
            [
                "{0}:{1}".format(source_port, destination_port)
                for (source_port, destination_port) in port_mappings.items()
            ]
        )
        run_args.insert(3, "-p {0}".format(mapping))

    print("docker run command:")
    print(run_args)

    os.system(" ".join(run_args))
