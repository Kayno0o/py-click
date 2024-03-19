from datetime import datetime
import os


def get_reports_dir():
    user = os.environ.get("USER")
    if user is None:
        raise EnvironmentError("USER environment variable is not set")

    directory = f"/home/{user}/reports/"
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory


def get_log_file_name():
    now = datetime.now()
    directory = get_reports_dir()

    return os.path.join(directory, now.strftime("%Y-%m-%d") + ".json")
