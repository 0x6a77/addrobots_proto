#!/usr/bin/env bash

echo 'java'
protoc --proto_path=./SourceMessages/ --java_out=./Production/Java/ ./SourceMessages/VehicleMsg.proto
protoc --proto_path=./SourceMessages/ --java_out=./Production/Java/ ./SourceMessages/MotorMsg.proto

echo 'javascript'
protoc --proto_path=./SourceMessages/ --js_out=import_style=commonjs,binary:./Production/Javascript/ ./SourceMessages/VehicleMsg.proto
protoc --proto_path=./SourceMessages/ --js_out=import_style=commonjs,binary:./Production/Javascript/ ./SourceMessages/MotorMsg.proto

echo 'python'
protoc --proto_path=./SourceMessages/ --python_out=./Production/Python/ ./SourceMessages/VehicleMsg.proto
protoc --proto_path=./SourceMessages/ --python_out=./Production/Python/ ./SourceMessages/MotorMsg.proto

echo 'embedded-c'
cd Production
protoc --plugin=nanopb=~/git/nanopb/dist/nanopb-0.3.8-28-g14efb1a-macosx-x86/generator/protoc-gen-nanopb --include_imports=~/git/nanopb/dist/nanopb-0.3.8-28-g14efb1a-macosx-x86/generator/proto/nanopb.proto --proto_path=../SourceMessages -o./MotorMsg.pb ../SourceMessages/MotorMsg.proto
python ~/git/nanopb/dist/nanopb-0.3.8-28-g14efb1a-macosx-x86/generator/nanopb_generator.py -f ../SourceMessages/MotorMsg.options --output-dir=../Production/NanoPB MotorMsg.pb
