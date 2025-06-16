def download_file( url,
                   tgt_path = None,
                   skip_if_exists = False,
                   quiet = False ):
    import requests
    import pathlib
    tgt_path = pathlib.Path( tgt_path or url.split('/')[-1] )
    if tgt_path.is_file():
        if skip_if_exists:
            if not quiet:
                print(f"File already downloaded: {tgt_path.name}")
            return tgt_path
        tgt_path.unlink()
    if not quiet:
        print(f"Downloading: {tgt_path.name}")
    with requests.get(url, stream=True) as rh:
        rh.raise_for_status()
        with pathlib.Path(tgt_path).open('wb') as fh:
            for chunk in rh.iter_content(chunk_size=131072):
                fh.write(chunk)
    return tgt_path

def extract_archive( archive_path, dest, quiet = False ):
    import tarfile
    import sys
    import pathlib
    dest = pathlib.Path(dest)
    if not quiet:
        print(f"Extracting {archive_path.name}")
    dest.mkdir( exist_ok = True, parents = True )
    kw = {'filter':'data'} if sys.version_info[0:2]>=(3,12) else {}
    with tarfile.open(archive_path, 'r') as th:
        th.extractall(path=dest,**kw)
