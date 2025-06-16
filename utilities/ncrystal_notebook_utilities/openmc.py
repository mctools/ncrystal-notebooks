def download_and_prepare_nndc_data():
    import pathlib
    source = 'https://anl.box.com/shared/static/teaup95cqv8s9nn56hfn7ku8mmelr95p.xz'
    print( 'Getting NNDX data for OpenMC from source:')
    print(f'  {source}')
    openmc_xsfile = pathlib.Path('./nndc_hdf5/cross_sections.xml')
    if openmc_xsfile.is_file():
        print("... Already downloaded and extracted!")
    else:
        from .download import extract_archive, download_file
        print("... Downloading (this might take a minute)...")
        f = download_file(source, skip_if_exists = True, quiet = True )
        print("... Extracting (this might take a minute)...")
        extract_archive( f, '.', quiet = True )
    if not openmc_xsfile.is_file():
        raise RuntimeError(f"Did not find expected file: {openmc_xsfile}")
    print(f"OpenMC cross section file prepared in {openmc_xsfile}")
    return openmc_xsfile
