#!/bin/sh

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
        docker build -t otree-rfas-dev .
        docker run -it --rm -p 8000:8000 -e OTREE_PRODUCTION=0 -v "$CURRENT_DIR":/usr/src/app otree-rfas-dev
        ;;
    -p)
        docker build -f Dockerfile.prod -t otree-rfas-prod .
        docker run -d -it --restart always -p 8000:8000 -e OTREE_PRODUCTION=1 otree-rfas-prod
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