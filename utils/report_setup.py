import os

import __root__


def report():
    pass
    log_path = os.path.join(__root__.path(), "Reports/LatestResults/Logs.log")
    if os.path.exists(log_path):
        print("true")
        os.remove(log_path)
    dir = os.path.join(__root__.path(), "tmp/allure_results")
    for root, dirs, files in os.walk(dir):
        for file in files:
            path = os.path.join(dir, file)
            os.remove(path)


if __name__ == '__main__':
    report()
