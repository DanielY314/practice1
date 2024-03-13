import argparse
import requests
from threading import Thread
import os
import time

def download_file(url, folder="C:\Users\USER\School\Term4\Networking\Lab\Lab5"):
    # Ensure the download folder exists
    if not os.path.exists(folder):
        os.makedirs(folder)
    # Extract the file name from the URL
    file_name = url.split("/")[-1]
    file_path = os.path.join(folder, file_name)
    # Download the file
    print(f"Downloading {file_name} to {folder}")
    response = requests.get(url)
    with open(file_path, 'wb') as file:
        file.write(response.content)
    print(f"Finished downloading {file_name}")

def download_files_sequential(urls, folder):
    for url in urls:
        download_file(url, folder)

def download_files_threaded(urls, folder):
    threads = []
    for url in urls:
        thread = Thread(target=download_file, args=(url, folder))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

def main():
    parser = argparse.ArgumentParser(description="Download files using sequential or threaded method.")
    parser.add_argument("mode", choices=['sequential', 'threaded'], help="Download mode.")
    parser.add_argument("--folder", default="downloads", help="Folder to download the files to.")
    args = parser.parse_args()

    urls = [
'https://th.bing.com/th/id/OIP.z-dkECmUFma29zYrb27JkwAAAA?w=264&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.MhwSzfXnBG1MpuuA6IFi-AAAAA?w=218&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.m8b7Y9-81Q4UMCBMaFkw2QAAAA?w=198&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.XN9D7tH47WNJ8h214YgqTwAAAA?w=220&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.cFvfW8dARmuVtR3zOxfTSAHaE9?w=274&h=183&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.wcEy7Ow-TaAohBCz6USqCAAAAA?w=265&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.9FWt0sWpi4UOee5o3WdI-QHaFj?w=224&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.JYXSCIpGskpiOxYTw1vuwgAAAA?w=252&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.QjWOHkojgYSz1LhaypSB-gAAAA?w=190&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.Wlfm_lF4VWlYLiPNfbmbDwHaHa?w=181&h=181&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.ZquJ_NwCCyWfvpAEeU-vngAAAA?w=142&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.C6q29lesR7-Ork5YKuI6LwAAAA?w=257&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.A7o1Bm-XNr9A_4pLPCCujgAAAA?w=252&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.oSjt2rY3YUScDY7pw3b1WAHaFj?w=236&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.AroTG9KnmisPIhICyGjoDAHaFj?w=223&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.zSyHBN9_rn_O9XBkdPx-agAAAA?w=189&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.pGTxkbwreLj7l2ORZrtA8gAAAA?w=147&h=184&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.5SaLUh616MU7KDIP2_0VCwAAAA?w=204&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.S-lrZd2TFhSEpI3VRQyKqQAAAA?w=173&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.sDmZWxXBrF329vZvDu2HrAAAAA?w=266&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.5umgRLykyWn-v_5HmOS0NAHaE7?w=243&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.MPayRq2bYdhfVUj5O9BCnwAAAA?w=125&h=184&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.OeLv1q1dEfGkl1bRHfM5awHaFj?w=240&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.MksSZEmu5Cgly2HNvRp4NQAAAA?w=180&h=163&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.HCpPn-IRV8SVidBlRoBRUwHaE7?w=287&h=191&c=7&r=0&o=5&pid=1.7'
]


    start_time = time.time()

    if args.mode == "sequential":
        download_files_sequential(urls, args.folder)
    else:
        download_files_threaded(urls, args.folder)

    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()
