import os
import subprocess
import time
import pandas as csv
command = f"aws s3 ls s3://commoncrawl/crawl-data/ >main_cc.txt"

def getmain_cc():
    command1 = f"aws s3 ls s3://commoncrawl/crawl-data/ >main_cc.txt"
    os.system(command1)
    time.sleep(10)

def read_cc_from_files(file_path="main_cc.txt"):
    with open(file_path,"r") as f:
        cc = f.readlines()
    data = []
    for c in cc:
        split = c.split()
        if "MAIN" in split[1]:
            data.append(split[1].replace("/",""))
    return data
def get_segments(cc):
    command2 = f"aws s3 ls s3://commoncrawl/crawl-data/{cc}/segments/ > segments.txt"
    os.system(command2)
    time.sleep(10)
    with open("segments.txt","r") as f:
        segments = f.readlines()
    return_ = []
    for s in segments:
        split = s.split()
        return_.append(split[1].replace("/",""))
    return return_

def get_file_list(cc, segment):
    command3 = f"aws s3 ls s3://commoncrawl/crawl-data/{cc}/segments/{segment}/wet/ > files.txt"
    os.system(command3)
    time.sleep(10)
    with open("files.txt","r") as f:
        files = f.readlines()
    return_ = []
    for f in files:
        split = f.split()
        return_.append(split[3])
        print()
    return return_

def do_all():
    full_path = "s3://commoncrawl/crawl-data/{}/segments/{}/wet/{}"
    cc = read_cc_from_files()
    for c in cc:
        segments = get_segments(c)
        for s in segments:
            files = get_file_list(c, s)
            for f in files:
                file_path = full_path.format(c,s,f)
                print()
copy ="aws s3 cp s3://commoncrawl/crawl-data/{cc}/segments/{segment}/wet/{file} {local_path}"
copy2 = "aws s3 cp {remote_path} {local_path}"
# do_all()


def download(remote="", local =""):
    command = f"aws s3 cp {remote} {local}"
    file_path = local
    while(not os.path.isfile(file_path)):
        os.system(command)
        time.sleep(1)
# cc = "CC-MAIN-2013-20"
# s = ""
# f ="CC-MAIN-20130516092621-00011-ip-10-60-113-184.ec2.internal.warc.wet.gz"
remote = "s3://commoncrawl/crawl-data/CC-MAIN-2013-20/segments/1368696381249/wet/CC-MAIN-20130516092621-00000-ip-10-60-113-184.ec2.internal.warc.wet.gz"
local = r"temp_dir\abc.gz"
download(remote, local)
