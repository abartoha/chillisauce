from tqdm import tqdm
from os import listdir, mkdir, path
import os
import requests

# def download_to_folder(sauce, count):
#     if sauce not in listdir:
#         makedir(sauce)
#     url2, name = episode
#     if not list_dir.__contains__(f"{name}.jpg"):
#         print("[bold red]NEW Photo![/bold red]\t"+name)
#         print("[italic green]Downloading....[/italic green]")
#         url = f"https://episodebd.com/file/download/{url2}.html"

#         response = requests.get(url, stream=True, headers = headers)
#         total_size_in_bytes= int(response.headers.get('content-length', 0))
#         block_size = 1024 #1 Kibibyte
#         progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
#         with open(f'Files/{name}.mp3', 'wb') as file:
#             for data in response.iter_content(block_size):
#                 progress_bar.update(len(data))
#                 file.write(data)
#         progress_bar.close()
#         if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
#             print("[red]ERROR, something went wrong[/red]")
#         global j
#         j += 1
#     else:
#         console.print("Already downloaded\t[yellow]"+i[1]+"[/yellow]", style=already_downloaded_style)

def download(code, count, photoCode, x):
    if x > 10:
        return -1
    headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
    url = f"https://t.dogehls.xyz/galleries/{str(photoCode)}/{str(count)}.jpg"
    response = requests.get(url, stream=True, headers = headers)
    total_size_in_bytes= int(response.headers.get('content-length', 0))
    if str(code) not in listdir():
        mkdir(str(code))
    if f'{addZeros(count)}.jpg' in listdir(str(code))and os.path.getsize(f"{code}/{addZeros(count)}.jpg") == total_size_in_bytes:
        print("Same size, photo already downloaded")
        return 0
    if os.path.getsize(f"{code}/{addZeros(count)}.jpg") < total_size_in_bytes:
        print("Existing file not in proper shape, redownloading")
    if total_size_in_bytes < 662:
        # NOTE: this possible recursion hell is pretty nasty
        # better find a fix fast
        print(f"Retrying photo no. {count}, attempt no. {x}")
        download(code, count, photoCode, x+1)
        return 3
    block_size = 1024 #1 Kibibyte
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
    with open(f'{code}/{addZeros(count)}.jpg', 'wb') as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
    progress_bar.close()
    if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
        print("DOWNLOAD ERROR, something went wrong")
        download(code, count, photoCode, x+1)
        return 3
    x = 0
    return 0

def addZeros(number):
    if number < 10:
        return f"000{number}"
    if number < 100:
        return f"00{number}"
    if number < 1000:
        return f"0{number}"

def addZeros2(number, lim):
    return (10**lim) // number

if __name__ == "__main__":
    print(addZeros2(1, 4))