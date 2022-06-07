#!/bin/sh

# Usage: run.sh [OPTION]
#
# Options:
#     -t                run all tests
#     -t [TEST_NAME]    run test with name=TEST_NAME only
#     -p                build and run for production             

HOST_PORT=8000

CURRENT_DIR=""
case "$(uname)" in
    MINGW*)
        CURRENT_DIR="$(cygpath -w "$(pwd)")"
        ;;
    *)
        CURRENT_DIR="$(pwd)"
        ;;
esac

case "$@" in
    "")
        docker build -f Dockerfile.dev -t otree-rfas-dev .
        docker run -it --rm -p "$HOST_PORT":8000 -e OTREE_PRODUCTION=0 -v "$CURRENT_DIR":/usr/src/app otree-rfas-dev
        ;;
    -p)
        docker build -t otree-rfas-prod .
        docker run -d -it --restart always -p "$HOST_PORT":8000 otree-rfas-prod
        ;;
    -t*)
        shift
        docker build -t otree-rfas-test .
        docker run -it --rm -v "$CURRENT_DIR":/usr/src/app otree-rfas-test otree test "$@"
        ;;
    *)
        echo 'Error: Incorrect usage'
        ;;
esac