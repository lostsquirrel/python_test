import os


def exec_cmd(cmd):
    print(cmd)
    os.system(cmd)


def main():
    with open("images.txt") as fh:
        for image in fh:
            image = image.strip()
            cmd = f"docker pull {image}"
            exec_cmd(cmd)

            target_image = image.replace("k8s.gcr.io", "registry.lisong.pub:28500/sunrise")
            cmd2 = f"docker tag {image} {target_image}"
            exec_cmd(cmd2)

            cmd3 = f"docker push {target_image}"
            exec_cmd(cmd3)


if __name__ == '__main__':
    main()