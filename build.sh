#!/usr/bin/env bash

echo 'java'
protoc --proto_path=./src/protobuf/ --java_out=./generated/Java/ ./src/protobuf/VehicleMsg.proto
protoc --proto_path=./src/protobuf/ --java_out=./generated/Java/ ./src/protobuf/MotorMsg.proto

echo 'javascript'
protoc --proto_path=./src/protobuf/ --js_out=import_style=commonjs,binary:./generated/Javascript/ ./src/protobuf/VehicleMsg.proto
protoc --proto_path=./src/protobuf/ --js_out=import_style=commonjs,binary:./generated/Javascript/ ./src/protobuf/MotorMsg.proto

echo 'python'
protoc --proto_path=./src/protobuf/ --python_out=./generated/Python/ ./src/protobuf/VehicleMsg.proto
protoc --proto_path=./src/protobuf/ --python_out=./generated/Python/ ./src/protobuf/MotorMsg.proto

echo 'embedded-c'
cd generated
protoc --plugin=nanopb=~/git/nanopb/dist/nanopb-0.3.8-28-g14efb1a-macosx-x86/generator/protoc-gen-nanopb --include_imports=~/git/nanopb/dist/nanopb-0.3.8-28-g14efb1a-macosx-x86/generator/proto/nanopb.proto --proto_path=../src/protobuf -o./MotorMsg.pb ../src/protobuf/MotorMsg.proto
python ~/git/nanopb/dist/nanopb-0.3.8-28-g14efb1a-macosx-x86/generator/nanopb_generator.py -f ../src/protobuf/MotorMsg.options --output-dir=../generated/NanoPB MotorMsg.pb
