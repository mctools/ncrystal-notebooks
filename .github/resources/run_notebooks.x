#!/bin/bash
set -eu
export REPOROOT="$( cd -P "$( dirname "${BASH_SOURCE[0]}" )/../../" && pwd )"
for notebookfile in `find "${REPOROOT}"/notebooks/ -name '*.ipynb'`; do
    echo
    echo '------------------------------------------------------'
    bn=$(basename "${notebookfile}")
    echo "Testing ${bn}"
    echo "${notebookfile}"
    rm -rf "${REPOROOT}/test_tmp_rundir"
    mkdir "${REPOROOT}/test_tmp_rundir"
    cd "${REPOROOT}/test_tmp_rundir"
    echo "   .. converting to script"
    cp "${notebookfile}" thenotebook.ipynb
    jupyter nbconvert --to script ./thenotebook.ipynb --output="${PWD}/thenotebook_converted"
    test -f ./thenotebook_converted.py
    echo "   .. executing script"
    time ipython ./thenotebook_converted.py | cat
    if [ ${PIPESTATUS[0]} != 0 ]; then
        echo "DETECTED ERROR IN: ${bn}"
        exit 1
    fi
done
