#!/usr/bin/env python3

#
# TODO:
# - process automatically all temperatures and generate a single file
#

"""Script for processing ENDF-6 TSL files into ACE files using NJOY.
"""

def convert_endf_tsl_to_ace(endf_tsl, material_name=None, ace_name=None,
                            suffix='.00', ace_filename=None, temp=None,
                            emax=None, zaids=None, njoy_exec='njoy'):
    import os
    import subprocess
    import shutil
    import pathlib
    import endf_parserpy

    natural_isotopes={
    1000: "1000 1001 1002",
    2000: "2000 2003 2004",
    3000: "3000 3006 3007",
    4000: "4000 4009",
    5000: "5000 5010 5011",
    6000: "6000 6012 6013",
    7000: "7000 7014 7015",
    8000: "8000 8016 8017 8018",
    9000: "9000 9019",
    10000: "10000 10020 10021 10022",
    11000: "11000 11023",
    12000: "12000 12024 12025 12026",
    13000: "13000 13027",
    14000: "14000 14028 14029 14030",
    15000: "15000 15031",
    16000: "16000 16032 16033 16034 16036",
    17000: "17000 17035 17037",
    18000: "18000 18036 18038 18040",
    19000: "19000 19039 19040 19040 19041",
    20000: "20000 20040 20042 20043 20044 20046 20048",
    21000: "21000 21045",
    22000: "22000 22046 22047 22048 22049 22050",
    23000: "23000 23050 23050 23051",
    24000: "24000 24050 24052 24053 24054",
    25000: "25000 25055",
    26000: "26000 26054 26056 26057 26058",
    27000: "27000 27059",
    28000: "28000 28058 28060 28061 28062 28064",
    29000: "29000 29063 29065",
    30000: "30000 30064 30066 30067 30068 30070",
    31000: "31000 31069 31071",
    32000: "32000 32070 32072 32073 32074 32076",
    33000: "33000 33075",
    34000: "34000 34074 34076 34077 34078 34080 34082",
    35000: "35000 35079 35081",
    36000: "36000 36078 36080 36082 36083 36084 36086",
    37000: "37000 37085 37087",
    38000: "38000 38084 38086 38087 38088",
    39000: "39000 39089",
    40000: "40000 40090 40091 40092 40094 40096",
    41000: "41000 41093",
    42000: "42000 42092 42094 42095 42096 42097 42098 42100",
    44000: "44000 44096 44098 44099 44100 44101 44102 44104",
    45000: "45000 45103",
    46000: "46000 46102 46104 46105 46106 46108 46110",
    47000: "47000 47107 47109",
    48000: "48000 48106 48108 48110 48111 48112 48113 48114 48116",
    49000: "49000 49113 49115",
    50000: "50000 50112 50114 50115 50116 50117 50118 50119 50120 50122 50124",
    51000: "51000 51121 51123",
    52000: "52000 52120 52122 52123 52124 52125 52126 52128 52130",
    53000: "53000 53127",
    54000: "54000 54124 54126 54128 54129 54130 54131 54132 54134 54136",
    55000: "55000 55133",
    56000: "56000 56130 56132 56134 56135 56136 56137 56138",
    57000: "57000 57138 57138 57139",
    58000: "58000 58136 58138 58140 58142",
    59000: "59000 59141",
    60000: "60000 60142 60143 60144 60145 60146 60148 60150",
    62000: "62000 62144 62147 62148 62149 62150 62152 62154",
    63000: "63000 63151 63153",
    64000: "64000 64152 64154 64155 64156 64157 64158 64160",
    65000: "65000 65159",
    66000: "66000 66156 66158 66160 66161 66162 66163 66164",
    67000: "67000 67165",
    68000: "68000 68162 68164 68166 68167 68168 68170",
    69000: "69000 69169",
    70000: "70000 70168 70170 70171 70172 70173 70174 70176",
    71000: "71000 71175 71176",
    72000: "72000 72174 72176 72177 72178 72179 72180",
    73000: "73000 73180 73180 73181",
    74000: "74000 74180 74182 74183 74184 74186",
    75000: "75000 75185 75187 75187",
    76000: "76000 76184 76186 76187 76188 76189 76190 76192",
    77000: "77000 77191 77193",
    78000: "78000 78190 78192 78194 78195 78196 78198 78198",
    79000: "79000 79197",
    80000: "80000 80196 80198 80199 80200 80201 80202 80204",
    81000: "81000 81203 81205",
    82000: "82000 82204 82206 82207 82208",
    83000: "83000 83209",
    90000: "90000 90232",
    92000: "92000 92234 92235 92238"}

    def create_dummy_endf_file(filename):
        parser = endf_parserpy.EndfParser( print_cache_info=False,
                                           cache_dir=False )
        endf_dict = endf_parserpy.EndfDict()
        endf_dict['1/451'] = {}
        p = endf_dict['1/451']
        p['MAT'] = 10
        p['ZA'] = 1
        p['AWR'] = 1.0
        p['LRP'] = 2
        p['LFI'] = 0
        p['NLIB'] = 0
        p['NMOD'] = 1
        p['ELIS'] = 0.0
        p['STA'] = 0
        p['LIS'] = 0
        p['LISO'] = 0
        p['NFOR'] = 6
        p['AWI'] = 1.0
        p['EMAX'] = 2e8
        p['LREL'] = 0
        p['NSUB'] = 10
        p['NVER'] = 1
        p['TEMP'] = 0.0
        p['LDRV'] = 0
        p['NWD'] = 7
        p['NXC'] = 1
        p['ZSYMAM'] = '           '
        p['ALAB'] = 'ESS'.ljust(11)
        p['EDATE'] = 'EVAL-SEP24'
        p['AUTH'] = ''.ljust(33)
        p['EMAX'] = 100.0
        p['REF'] = ''.ljust(21)
        p['DDATE'] = ''.ljust(10)
        p['RDATE'] = ''.ljust(10)
        p['ENDATE'] = ''.ljust(8)
        p['HSUB/1'] = ('----DUMMYLIB'.ljust(22) + f'MATERIAL {p["MAT"]}').ljust(66)
        p['HSUB/2'] = '-----INCIDENT NEUTRON DATA'.ljust(66)
        p['HSUB/3'] = '------ENDF-6 FORMAT'.ljust(66)
        p['DESCRIPTION/1'] = 'Dummy neutron library.'.ljust(66)
        p['DESCRIPTION/2'] = 'This library does not represent any real isotope.'.ljust(66)
        p['MFx/1'] = 1
        p['MTx/1'] = 451
        p['NCx/1'] = 5
        p['MOD/1'] = p['NMOD']
        endf_dict['0/0/MAT'] = endf_dict['1/451/MAT']
        endf_dict['0/0/TAPEDESCR'] = ''
        endf_dict['3/1/MAT'] = endf_dict['1/451/MAT']
        endf_dict['3/1/AWR'] = endf_dict['1/451/AWR']
        endf_dict['3/1/ZA'] = endf_dict['1/451/ZA']
        endf_dict['3/1/QM'] = 0.0
        endf_dict['3/1/QI'] = 0.0
        endf_dict['3/1/LR'] = 0
        endf_dict['3/1/xstable/NBT'] = [8]
        endf_dict['3/1/xstable/INT'] = [2]
        endf_dict['3/1/xstable/E'] = [1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1.0, 10.0, 100]
        endf_dict['3/1/xstable/xs'] = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
        endf_dict['3/2/MAT'] = endf_dict['1/451/MAT']
        endf_dict['3/2/AWR'] = endf_dict['1/451/AWR']
        endf_dict['3/2/ZA'] = endf_dict['1/451/ZA']
        endf_dict['3/2/QM'] = 0.0
        endf_dict['3/2/QI'] = 0.0
        endf_dict['3/2/LR'] = 0
        endf_dict['3/2/xstable/NBT'] = [8]
        endf_dict['3/2/xstable/INT'] = [2]
        endf_dict['3/2/xstable/E'] = [1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1.0, 10.0, 100]
        endf_dict['3/2/xstable/xs'] = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
        endf_parserpy.update_directory(endf_dict, parser)
        parser.writefile(filename, endf_dict, overwrite=True)

    def delete_tapes():
        for fn in ['tape20', 'tape22', 'tape23', 'tape31',
                   'tape41', 'tape51', 'tape61', 'output']:
            try:
                os.remove(fn)
            except OSError:
                pass

    parser = endf_parserpy.EndfParser(print_cache_info=False, cache_dir=False)
    endf_dic = parser.parsefile(endf_tsl)
    temperatures = endf_dic[7][4]['teff0_table']['Tint']
    assert ( (len(suffix) == 3
              and suffix[0]=='.'
              and suffix[1:] == f'{int(suffix[1:]):02d}')
             or (len(suffix) == 2
                 and suffix == f'{int(suffix):02d}') ), 'Wrong suffix'
    if len(suffix) == 2:
        suffix = f'.{int(suffix):02d}'
    if temp is None:
        temp = temperatures[0]
    else:
        assert temp in temperatures, f'{temp} K not found in ENDF-6 file'
    has_elastic = (2 in endf_dic[7].keys())
    za = int(endf_dic[1][451]['ZA'])
    endf_tsl_mat = endf_dic[1][451]['MAT']
    natom = int(endf_dic[7][4]['B'][6])
    #
    # Get elastic options for THERMR and ACER
    #
    icoh = 0
    ielas = 0
    elas_mat = 0
    if has_elastic:
        elas_mat = 238
        lthr = endf_dic[7][2]['LTHR']
        ielas = lthr - 1
        icoh = 1 if lthr == 1 or lthr == 3 else 0
    if zaids is None:
        if (451 in endf_dic[7].keys()):
            # If MF=7/MT=451 is present, use the isotopic decomposition
            isotope_list = [ str(int(v2))
                             for k1,v1 in endf_dic[7][451]['ZAI'].items()
                             for k2,v2 in v1.items() ]
            zaids = ' '.join(isotope_list)
        else:
            # If not, use the decomposition in natural isotopes
            zaids = ( natural_isotopes[za]
                      if za in natural_isotopes.keys()
                      else f"{za}" )
    if emax is None:
        emax = endf_dic[1][451]['EMAX']
        if emax <= 0:
            emax = 5.0
    no_zaids=len(zaids.split(" "))
    ace_name = f'{za}' if ace_name is None else ace_name
    ace_filename = ( f"{ace_name}-{temp}K.ace"
                     if ace_filename is None
                     else ace_filename )
    xsdir_filename = ( ace_filename[:-4]+'.xsdir'
                       if ace_filename[-4:] == '.ace'
                       else ace_filename+'.xsdir' )
    material_name = endf_tsl if material_name is None else material_name
    txt=f"""reconr
20 22 /
'Dummy ENDF-6 tape' /
10 0 /
.01 /
0/
broadr
20 22 23 /
10 1 /
0.01 /
{temp} /
0/
thermr
31 23 41 /
{endf_tsl_mat} 10 32 1 2 {icoh} 0 {natom} 237  0 /
{temp} /
0.001 {emax} /
acer
20 41 0 51 61 /
 2  1  1  {suffix} 0/
' {material_name} at {temp}K' /
 10 {temp} {ace_name} {no_zaids} /
 {zaids} /
 237 200 {elas_mat} {ielas} 1 {emax} 2/
stop
"""
    delete_tapes()
    create_dummy_endf_file('tape20')
    shutil.copyfile(endf_tsl, 'tape31')
    result = subprocess.run([njoy_exec], input=txt, capture_output=True,
                            text=True)
    assert result.stdout.find('error')==-1, f'Error in NJOY:\n{result.stdout}'
    assert result.returncode == 0, ( 'NJOY not executed correctly\n'
                                    f'{result.stderr}')
    assert ( os.path.isfile('tape51')
             and os.path.isfile('tape61')), ('NJOY could not produce'
                                             ' the ACE file')

    shutil.move('tape51', ace_filename)
    txt = pathlib.Path('tape61').read_text()
    txt = txt.replace('filename', ace_filename)
    txt = txt.replace('route', '0')
    pathlib.Path(xsdir_filename).write_text(txt)
    delete_tapes()
    return ace_filename, xsdir_filename

if __name__ == '__main__':
    import sys
    import argparse
    class CustomFormatter(argparse.RawDescriptionHelpFormatter,
                          argparse.ArgumentDefaultsHelpFormatter):
        pass

    def parse_args(args=sys.argv[1:]):
        '''Parse arguments.'''
        parser = argparse.ArgumentParser(
            description=sys.modules[__name__].__doc__,
            formatter_class=CustomFormatter)
        parser.add_argument('input', type=str,
                            help='ENDF-6 TSL to convert')
        parser.add_argument('-n', '--name', type=str,
                            help='Name of the compound')
        parser.add_argument('-s', '--suffix', type=str,
                            help='Suffix for the ACE identifier')
        parser.add_argument('--acefile', type=str,
                            help='ACE filename')
        parser.add_argument('--acename', type=str,
                            help='ACE identifier')
        parser.add_argument('--njoy_exec', type=str,
                            help='NJOY executable', default='njoy')
        parser.add_argument('-t', '--temperature',
                            help='Temperature to process the ENDF-6 file.'
                                 ' If none is given, it will process the'
                                 ' first temperature of the file', type=float)
        parser.add_argument('--zaids',
                            nargs='+',
                            help='ZAIDs to assign the ACE file', type=int)
        return parser.parse_args(args)
    options = parse_args()
    endf_tsl = options.input
    material_name = options.name
    ace_name = options.acename
    ace_filename = options.acefile
    suffix = options.suffix if options.suffix is not None else '.00'
    temp = options.temperature
    njoy_exec = options.njoy_exec
    zaids = (" ".join(str(x) for x in options.zaids )
                     if options.zaids is not None else None )
    ace_filename, xsdir_filename = convert_endf_tsl_to_ace(endf_tsl=endf_tsl,
                                    material_name=material_name,
                                    ace_name=ace_name, suffix=suffix,
                                    ace_filename=ace_filename, temp=temp,
                                    zaids=zaids, njoy_exec=njoy_exec)
    print(f'Wrote {ace_filename}, {xsdir_filename}')
    sys.exit(0)
