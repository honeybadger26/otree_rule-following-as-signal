#!/bin/sh

case "$@" in
    "")
        docker build -t otree-rfas-dev .
        docker run -it --rm -p 8000:8000 -e OTREE_PRODUCTION=0 -v $(pwd):/usr/src/app otree-rfas-dev
        ;;
    -p)
        docker build -f Dockerfile.prod -t otree-rfas-prod .
        docker run -it --rm -p 8000:8000 -e OTREE_PRODUCTION=1 otree-rfas-prod
        ;;
    -t*)
        shift
        docker build -t otree-rfas-test .
        docker run -it --rm -v $(pwd):/usr/src/app otree-rfas-test otree test "$@"
        ;;
    *)
        echo 'Error: Incorrect usage'
        ;;
esac