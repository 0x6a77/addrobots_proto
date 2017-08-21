/**
 * @fileoverview
 * @enhanceable
 * @public
 */
// GENERATED CODE -- DO NOT EDIT!

goog.provide('proto.MotorCmd');

goog.require('jspb.Message');
goog.require('jspb.BinaryReader');
goog.require('jspb.BinaryWriter');
goog.require('proto.CmdParam');

goog.forwardDeclare('proto.MotorAction');

/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.MotorCmd = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.MotorCmd.repeatedFields_, null);
};
goog.inherits(proto.MotorCmd, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.MotorCmd.displayName = 'proto.MotorCmd';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.MotorCmd.repeatedFields_ = [2];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.MotorCmd.prototype.toObject = function(opt_includeInstance) {
  return proto.MotorCmd.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.MotorCmd} msg The msg instance to transform.
 * @return {!Object}
 */
proto.MotorCmd.toObject = function(includeInstance, msg) {
  var f, obj = {
    action: jspb.Message.getFieldWithDefault(msg, 1, 0),
    paramsList: jspb.Message.toObjectList(msg.getParamsList(),
    proto.CmdParam.toObject, includeInstance)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.MotorCmd}
 */
proto.MotorCmd.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.MotorCmd;
  return proto.MotorCmd.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.MotorCmd} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.MotorCmd}
 */
proto.MotorCmd.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {!proto.MotorAction} */ (reader.readEnum());
      msg.setAction(value);
      break;
    case 2:
      var value = new proto.CmdParam;
      reader.readMessage(value,proto.CmdParam.deserializeBinaryFromReader);
      msg.addParams(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.MotorCmd.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.MotorCmd.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.MotorCmd} message
 * @param {!jspb.BinaryWriter} writer
 */
proto.MotorCmd.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getAction();
  if (f !== 0.0) {
    writer.writeEnum(
      1,
      f
    );
  }
  f = message.getParamsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      2,
      f,
      proto.CmdParam.serializeBinaryToWriter
    );
  }
};


/**
 * optional MotorAction action = 1;
 * @return {!proto.MotorAction}
 */
proto.MotorCmd.prototype.getAction = function() {
  return /** @type {!proto.MotorAction} */ (jspb.Message.getFieldWithDefault(this, 1, 0));
};


/** @param {!proto.MotorAction} value */
proto.MotorCmd.prototype.setAction = function(value) {
  jspb.Message.setField(this, 1, value);
};


/**
 * repeated CmdParam params = 2;
 * If you change this array by adding, removing or replacing elements, or if you
 * replace the array itself, then you must call the setter to update it.
 * @return {!Array.<!proto.CmdParam>}
 */
proto.MotorCmd.prototype.getParamsList = function() {
  return /** @type{!Array.<!proto.CmdParam>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.CmdParam, 2));
};


/** @param {!Array.<!proto.CmdParam>} value */
proto.MotorCmd.prototype.setParamsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 2, value);
};


/**
 * @param {!proto.CmdParam=} opt_value
 * @param {number=} opt_index
 * @return {!proto.CmdParam}
 */
proto.MotorCmd.prototype.addParams = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 2, opt_value, proto.CmdParam, opt_index);
};


proto.MotorCmd.prototype.clearParamsList = function() {
  this.setParamsList([]);
};


