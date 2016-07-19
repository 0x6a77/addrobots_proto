#addrobots_proto

The Google Protocol Buffers to encode sensor and motor commands over the various interfaces.

## Java message generation

>cd ~/git/addrobots_proto/VehicleControlProto/

>protoc -I=./SourceMessages/ --java_out=./Production/Java/ ./SourceMessages/VcuCmdMsg.proto

>protoc -I=./SourceMessages/ --java_out=./Production/Java/ ./SourceMessages/McuCmdMsg.proto

## Javascript message generation

>cd ~/git/addrobots_proto/

>protoc -I=./SourceMessages/ --js_out=./Production/Javascript/ ./SourceMessages/VcuCmdMsg.proto

## Python message generation

>cd ~/git/addrobots_proto/VehicleControlProto/

>protoc -I=../SourceMessages/ --python_out=./Production/Python/ ../SourceMessages/VcuCmdMsg.proto

>protoc -I=../SourceMessages/ --python_out=./Production/Python/ ../SourceMessages/McuCmdMsg.proto

## NanoPB message generation (C code for firmware)

>cd ~/git/addrobots_proto/VehicleControlProto/Production

>protoc --plugin=nanopb=~/git/nanopb/generator/protoc-gen-nanopb --include_imports=~/git/nanopb/generator/proto/nanopb.proto --proto_path=../SourceMessages -o./McuCmdMsg.pb ../SourceMessages/McuCmdMsg.proto

>python ~/git/nanopb/generator/nanopb_generator.py -f ../SourceMessages/McuCmdMsg.options --output-dir=./NanoPB McuCmdMsg.pb
