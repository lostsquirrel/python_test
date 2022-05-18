
import subprocess


if __name__ == '__main__':
    result = subprocess.run(
        ['tail', '-f', "/tmp/test"], capture_output=True, text=True).stdout
    print(result)
