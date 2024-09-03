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
    if [ ! -f ./thenotebook_converted.py -a -f ./thenotebook_converted.txt ]; then
        #weird, this happens sometimes?!?
        echo "For some reason the conversion resulting in a .txt file!"
        echo "FILE BEGIN:"
        head -10 ./thenotebook_converted.txt
        echo "..."
        tail -10 ./thenotebook_converted.txt
        echo "FILE END:"
        echo "Trying to rename to .py"
        mv ./thenotebook_converted.txt ./thenotebook_converted.py
    fi
    test -f ./thenotebook_converted.py
    echo "   .. executing script"
    time ipython ./thenotebook_converted.py | cat
    if [ ${PIPESTATUS[0]} != 0 ]; then
        echo "DETECTED ERROR IN: ${bn}"
        exit 1
    fi
    deactivate
done
