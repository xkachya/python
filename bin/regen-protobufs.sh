#!/bin/bash

#Uncomment to run hack
#gsed -i 's/import "\//import ".\//g' ./protobufs/meshtastic/*
#gsed -i 's/package meshtastic;//g' ./protobufs/meshtastic/*

# protoc looks for mypy plugin in the python path
source $(poetry env info --path)/bin/activate

./nanopb-0.4.8/generator-bin/protoc -I=protobufs --python_out ./ --mypy_out ./ ./protobufs/meshtastic/*.proto
./nanopb-0.4.8/generator-bin/protoc -I=protobufs --python_out ./meshtastic/ --mypy_out ./meshtastic/ ./protobufs/nanopb.proto

# workaround for import bug in protoc https://github.com/protocolbuffers/protobuf/issues/1491#issuecomment-690618628

if [[ $OSTYPE == 'darwin'* ]]; then
	sed -i '' -E 's/^(import.*_pb2)/from . \1/' meshtastic/*.py
	# automate the current workaround (may be related to Meshtastic-protobufs issue #27 https://github.com/meshtastic/protobufs/issues/27)
	sed -i '' -E "s/^None = 0/globals()['None'] = 0/" meshtastic/mesh_pb2.py
else
	sed -i -e 's/^import.*_pb2/from . \0/' meshtastic/*.py
	# automate the current workaround (may be related to Meshtastic-protobufs issue #27 https://github.com/meshtastic/protobufs/issues/27)
	sed -i -e "s/^None = 0/globals()['None'] = 0/" meshtastic/mesh_pb2.py
fi
