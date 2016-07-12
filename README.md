#addrobots_proto

The Google Protocol Buffers to encode sensor and motor commands over the various interfaces.

## Java message generation

>cd ~/git/addrobots_proto/

>protoc -I=./VehicleDriveProto/SourceMessages/ --java_out=./VehicleDriveProto/Production/Java/ ./VehicleDriveProto/SourceMessages/VcuCmdMsg.proto

## Javascript message generation

>cd ~/git/addrobots_proto/

>protoc -I=./VehicleDriveProto/SourceMessages/ --js_out=./VehicleDriveProto/Production/Javascript/ ./VehicleDriveProto/SourceMessages/VcuCmdMsg.proto

## Python message generation

>cd ~/git/addrobots_proto/VehicleDriveProto/Production

>protoc -I=../SourceMessages/ --python_out=./Python/ ../SourceMessages/VcuCmdMsg.proto

>protoc -I=../SourceMessages/ --python_out=./Python/ ../SourceMessages/McuCmdMsg.proto

## NanoPB message generation 

>cd ~/git/addrobots_proto/VehicleDriveProto/Production

>protoc --plugin=nanopb=~/git/nanopb/generator/protoc-gen-nanopb --include_imports=~/git/nanopb/generator/proto/nanopb.proto --proto_path=../SourceMessages -o./McuCmdMsg.pb ../SourceMessages/McuCmdMsg.proto

>python ~/git/nanopb/generator/nanopb_generator.py -f ../SourceMessages/McuCmdMsg.options --output-dir=./NanoPB McuCmdMsg.pb
