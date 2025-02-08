#!/bin/bash
set -eu
export REPOROOT="$( cd -P "$( dirname "${BASH_SOURCE[0]}" )/../../" && pwd )"
for notebookfile in `find "${REPOROOT}"/notebooks/ -name '*.ipynb'`; do
    echo
    echo '------------------------------------------------------'
    bn=$(basename "${notebookfile}")
    echo "Testing ${bn}"
    echo "${notebookfile}"
    #if [[ -v VIRTUAL_ENV ]]; then
    #    type -t deactivate && deactivate
    #fi
    rm -rf "${REPOROOT}/test_tmp_rundir"
    mkdir "${REPOROOT}/test_tmp_rundir"
    cd "${REPOROOT}/test_tmp_rundir"
    python3 -mvenv create ./venv
    . ./venv/bin/activate
    python3 -mpip install jupyter ipython
    echo "   .. converting to script"
    cat "${notebookfile}" | \
        sed 's#always_do_pip_installs = False#always_do_pip_installs = True#' \
        > ./thenotebook.ipynb
    jupyter nbconvert --to script ./thenotebook.ipynb --output="${PWD}/thenotebook_converted"
    test -f ./thenotebook_converted.py
    #For now, the texture plugin notebook should only be run on linux and not in
    #NCrystal 4 before it has been ported:
    DO_RUN_PLUGIN_NOTEBOOKS=0
    if [ -e /proc -a "x${NCNOTEBOOKS_FORCE_SKIP_PLUGIN_NB:-}" != "x1" ]; then
        DO_RUN_PLUGIN_NOTEBOOKS=1
    fi
    if [ "x${bn}" == "xNEUWAVE_12_Examples_Installing_Plugins_Texture_exercise.ipynb" -a "${DO_RUN_PLUGIN_NOTEBOOKS}" == "1" ]; then
        echo
        echo
        echo "WARNING: SKIPPING NOTEBOOK ABOUT PLUGIN ON OSX!!!"
        echo
        echo
    elif [ "x${bn}" == "xNEUWAVE_12_Examples_Transmission_with_NCrystal_and_McStas.ipynb" ]; then
        echo
        echo
        echo "WARNING: SKIPPING CONDA BASED NOTEBOOK!!!"
        echo
        echo
    else
        echo "   .. executing script"
        time ipython ./thenotebook_converted.py | cat
        if [ ${PIPESTATUS[0]} != 0 ]; then
            echo "DETECTED ERROR IN: ${bn}"
            exit 1
        fi
    fi
    deactivate
done
