# ImageNet-downloader
Imagenet fetcher with its http APIs
I borrowed the code from https://github.com/dusty-nv/jetson-inference and modified a few lines to make it goes in python3.

```
$ wget --no-check-certificate https://nvidia.box.com/shared/static/gzr5iewf5aouhc5exhp3higw6lzhcysj.gz -O ilsvrc12_urls.tar.gz
$ tar -xzvf ilsvrc12_urls.tar.gz
$ python imagenet-download.py ilsvrc12_urls.txt #DOWNLOAD_TO_DIR# --jobs 100 --retry 3 --sleep 0
```

## ~~Prepare `wnid` list file~~

Full synet list can be found here http://www.image-net.org/api/text/imagenet.synset.obtain_synset_list

Select a subset of your own and write them to some file like `wnid_list.txt` 

```
n02119789
n02478875
n02473983
n02100735
n02390258
n02110185
n02338449
n02431976
...
n02066245
n02427032
```

