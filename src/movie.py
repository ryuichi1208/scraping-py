from concurrent.futures import ProcessPoolExecutor, as_completed
import os
import shutil
import requests


def download(url):
    file_name = os.path.basename(url)
    print("{0}のダウンロードを開始します。".format(file_name))

    res = requests.get(url, stream=True)
    with open(file_name, "wb") as file:
        shutil.copyfileobj(res.raw, file)

    return "{0}のダウンロードが完了".format(file_name)


if __name__ == "__main__":
    with ProcessPoolExecutor() as executor:
        all_process = []
        while True:
            input_url = input()
            if input_url == "exit":
                break
            else:
                process = executor.submit(download, input_url)
                all_process.append(process)

        for process in as_completed(all_process):
            print(process.result())
