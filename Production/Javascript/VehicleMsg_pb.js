/**
 * @fileoverview
 * @enhanceable
 * @suppress {messageConventions} JS Compiler reports an error if a variable or
 *     field starts with 'MSG_' and isn't a translatable message.
 * @public
 */
// GENERATED CODE -- DO NOT EDIT!

var jspb = require('google-protobuf');
var goog = jspb;
var global = Function('return this')();

goog.exportSymbol('proto.Drive', null, global);
goog.exportSymbol('proto.Halt', null, global);
goog.exportSymbol('proto.Orbit', null, global);
goog.exportSymbol('proto.VcuWrapperMessage', null, global);

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
proto.Drive = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.Drive, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.Drive.displayName = 'proto.Drive';
}


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
proto.Drive.prototype.toObject = function(opt_includeInstance) {
  return proto.Drive.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.Drive} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.Drive.toObject = function(includeInstance, msg) {
  var f, obj = {
    velocity: +jspb.Message.getFieldWithDefault(msg, 1, 0.0),
    direction: jspb.Message.getFieldWithDefault(msg, 2, ""),
    acceleration: +jspb.Message.getFieldWithDefault(msg, 3, 0.0),
    distance: +jspb.Message.getFieldWithDefault(msg, 4, 0.0),
    edgedistance: +jspb.Message.getFieldWithDefault(msg, 5, 0.0),
    edgeside: jspb.Message.getFieldWithDefault(msg, 6, "")
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
 * @return {!proto.Drive}
 */
proto.Drive.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.Drive;
  return proto.Drive.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.Drive} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.Drive}
 */
proto.Drive.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {number} */ (reader.readDouble());
      msg.setVelocity(value);
      break;
    case 2:
      var value = /** @type {string} */ (reader.readString());
      msg.setDirection(value);
      break;
    case 3:
      var value = /** @type {number} */ (reader.readDouble());
      msg.setAcceleration(value);
      break;
    case 4:
      var value = /** @type {number} */ (reader.readDouble());
      msg.setDistance(value);
      break;
    case 5:
      var value = /** @type {number} */ (reader.readDouble());
      msg.setEdgedistance(value);
      break;
    case 6:
      var value = /** @type {string} */ (reader.readString());
      msg.setEdgeside(value);
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
proto.Drive.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.Drive.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.Drive} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.Drive.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getVelocity();
  if (f !== 0.0) {
    writer.writeDouble(
      1,
      f
    );
  }
  f = message.getDirection();
  if (f.length > 0) {
    writer.writeString(
      2,
      f
    );
  }
  f = message.getAcceleration();
  if (f !== 0.0) {
    writer.writeDouble(
      3,
      f
    );
  }
  f = message.getDistance();
  if (f !== 0.0) {
    writer.writeDouble(
      4,
      f
    );
  }
  f = message.getEdgedistance();
  if (f !== 0.0) {
    writer.writeDouble(
      5,
      f
    );
  }
  f = message.getEdgeside();
  if (f.length > 0) {
    writer.writeString(
      6,
      f
    );
  }
};


/**
 * optional double velocity = 1;
 * @return {number}
 */
proto.Drive.prototype.getVelocity = function() {
  return /** @type {number} */ (+jspb.Message.getFieldWithDefault(this, 1, 0.0));
};


/** @param {number} value */
proto.Drive.prototype.setVelocity = function(value) {
  jspb.Message.setProto3FloatField(this, 1, value);
};


/**
 * optional string direction = 2;
 * @return {string}
 */
proto.Drive.prototype.getDirection = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 2, ""));
};


/** @param {string} value */
proto.Drive.prototype.setDirection = function(value) {
  jspb.Message.setProto3StringField(this, 2, value);
};


/**
 * optional double acceleration = 3;
 * @return {number}
 */
proto.Drive.prototype.getAcceleration = function() {
  return /** @type {number} */ (+jspb.Message.getFieldWithDefault(this, 3, 0.0));
};


/** @param {number} value */
proto.Drive.prototype.setAcceleration = function(value) {
  jspb.Message.setProto3FloatField(this, 3, value);
};


/**
 * optional double distance = 4;
 * @return {number}
 */
proto.Drive.prototype.getDistance = function() {
  return /** @type {number} */ (+jspb.Message.getFieldWithDefault(this, 4, 0.0));
};


/** @param {number} value */
proto.Drive.prototype.setDistance = function(value) {
  jspb.Message.setProto3FloatField(this, 4, value);
};


/**
 * optional double edgeDistance = 5;
 * @return {number}
 */
proto.Drive.prototype.getEdgedistance = function() {
  return /** @type {number} */ (+jspb.Message.getFieldWithDefault(this, 5, 0.0));
};


/** @param {number} value */
proto.Drive.prototype.setEdgedistance = function(value) {
  jspb.Message.setProto3FloatField(this, 5, value);
};


/**
 * optional string edgeSide = 6;
 * @return {string}
 */
proto.Drive.prototype.getEdgeside = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 6, ""));
};


/** @param {string} value */
proto.Drive.prototype.setEdgeside = function(value) {
  jspb.Message.setProto3StringField(this, 6, value);
};



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
proto.Orbit = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.Orbit, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.Orbit.displayName = 'proto.Orbit';
}


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
proto.Orbit.prototype.toObject = function(opt_includeInstance) {
  return proto.Orbit.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.Orbit} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.Orbit.toObject = function(includeInstance, msg) {
  var f, obj = {
    velocity: +jspb.Message.getFieldWithDefault(msg, 1, 0.0),
    direction: jspb.Message.getFieldWithDefault(msg, 2, ""),
    acceleration: +jspb.Message.getFieldWithDefault(msg, 3, 0.0),
    degrees: +jspb.Message.getFieldWithDefault(msg, 4, 0.0)
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
 * @return {!proto.Orbit}
 */
proto.Orbit.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.Orbit;
  return proto.Orbit.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.Orbit} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.Orbit}
 */
proto.Orbit.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {number} */ (reader.readDouble());
      msg.setVelocity(value);
      break;
    case 2:
      var value = /** @type {string} */ (reader.readString());
      msg.setDirection(value);
      break;
    case 3:
      var value = /** @type {number} */ (reader.readDouble());
      msg.setAcceleration(value);
      break;
    case 4:
      var value = /** @type {number} */ (reader.readDouble());
      msg.setDegrees(value);
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
proto.Orbit.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.Orbit.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.Orbit} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.Orbit.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getVelocity();
  if (f !== 0.0) {
    writer.writeDouble(
      1,
      f
    );
  }
  f = message.getDirection();
  if (f.length > 0) {
    writer.writeString(
      2,
      f
    );
  }
  f = message.getAcceleration();
  if (f !== 0.0) {
    writer.writeDouble(
      3,
      f
    );
  }
  f = message.getDegrees();
  if (f !== 0.0) {
    writer.writeDouble(
      4,
      f
    );
  }
};


/**
 * optional double velocity = 1;
 * @return {number}
 */
proto.Orbit.prototype.getVelocity = function() {
  return /** @type {number} */ (+jspb.Message.getFieldWithDefault(this, 1, 0.0));
};


/** @param {number} value */
proto.Orbit.prototype.setVelocity = function(value) {
  jspb.Message.setProto3FloatField(this, 1, value);
};


/**
 * optional string direction = 2;
 * @return {string}
 */
proto.Orbit.prototype.getDirection = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 2, ""));
};


/** @param {string} value */
proto.Orbit.prototype.setDirection = function(value) {
  jspb.Message.setProto3StringField(this, 2, value);
};


/**
 * optional double acceleration = 3;
 * @return {number}
 */
proto.Orbit.prototype.getAcceleration = function() {
  return /** @type {number} */ (+jspb.Message.getFieldWithDefault(this, 3, 0.0));
};


/** @param {number} value */
proto.Orbit.prototype.setAcceleration = function(value) {
  jspb.Message.setProto3FloatField(this, 3, value);
};


/**
 * optional double degrees = 4;
 * @return {number}
 */
proto.Orbit.prototype.getDegrees = function() {
  return /** @type {number} */ (+jspb.Message.getFieldWithDefault(this, 4, 0.0));
};


/** @param {number} value */
proto.Orbit.prototype.setDegrees = function(value) {
  jspb.Message.setProto3FloatField(this, 4, value);
};



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
proto.Halt = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.Halt, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.Halt.displayName = 'proto.Halt';
}


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
proto.Halt.prototype.toObject = function(opt_includeInstance) {
  return proto.Halt.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.Halt} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.Halt.toObject = function(includeInstance, msg) {
  var f, obj = {
    acceleration: +jspb.Message.getFieldWithDefault(msg, 1, 0.0)
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
 * @return {!proto.Halt}
 */
proto.Halt.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.Halt;
  return proto.Halt.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.Halt} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.Halt}
 */
proto.Halt.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {number} */ (reader.readDouble());
      msg.setAcceleration(value);
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
proto.Halt.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.Halt.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.Halt} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.Halt.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getAcceleration();
  if (f !== 0.0) {
    writer.writeDouble(
      1,
      f
    );
  }
};


/**
 * optional double acceleration = 1;
 * @return {number}
 */
proto.Halt.prototype.getAcceleration = function() {
  return /** @type {number} */ (+jspb.Message.getFieldWithDefault(this, 1, 0.0));
};


/** @param {number} value */
proto.Halt.prototype.setAcceleration = function(value) {
  jspb.Message.setProto3FloatField(this, 1, value);
};



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
proto.VcuWrapperMessage = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, proto.VcuWrapperMessage.oneofGroups_);
};
goog.inherits(proto.VcuWrapperMessage, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.VcuWrapperMessage.displayName = 'proto.VcuWrapperMessage';
}
/**
 * Oneof group definitions for this message. Each group defines the field
 * numbers belonging to that group. When of these fields' value is set, all
 * other fields in the group are cleared. During deserialization, if multiple
 * fields are encountered for a group, only the last value seen will be kept.
 * @private {!Array<!Array<number>>}
 * @const
 */
proto.VcuWrapperMessage.oneofGroups_ = [[1,2,3]];

/**
 * @enum {number}
 */
proto.VcuWrapperMessage.MsgCase = {
  MSG_NOT_SET: 0,
  DRIVE: 1,
  ORBIT: 2,
  HALT: 3
};

/**
 * @return {proto.VcuWrapperMessage.MsgCase}
 */
proto.VcuWrapperMessage.prototype.getMsgCase = function() {
  return /** @type {proto.VcuWrapperMessage.MsgCase} */(jspb.Message.computeOneofCase(this, proto.VcuWrapperMessage.oneofGroups_[0]));
};



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
proto.VcuWrapperMessage.prototype.toObject = function(opt_includeInstance) {
  return proto.VcuWrapperMessage.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.VcuWrapperMessage} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.VcuWrapperMessage.toObject = function(includeInstance, msg) {
  var f, obj = {
    drive: (f = msg.getDrive()) && proto.Drive.toObject(includeInstance, f),
    orbit: (f = msg.getOrbit()) && proto.Orbit.toObject(includeInstance, f),
    halt: (f = msg.getHalt()) && proto.Halt.toObject(includeInstance, f)
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
 * @return {!proto.VcuWrapperMessage}
 */
proto.VcuWrapperMessage.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.VcuWrapperMessage;
  return proto.VcuWrapperMessage.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.VcuWrapperMessage} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.VcuWrapperMessage}
 */
proto.VcuWrapperMessage.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.Drive;
      reader.readMessage(value,proto.Drive.deserializeBinaryFromReader);
      msg.setDrive(value);
      break;
    case 2:
      var value = new proto.Orbit;
      reader.readMessage(value,proto.Orbit.deserializeBinaryFromReader);
      msg.setOrbit(value);
      break;
    case 3:
      var value = new proto.Halt;
      reader.readMessage(value,proto.Halt.deserializeBinaryFromReader);
      msg.setHalt(value);
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
proto.VcuWrapperMessage.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.VcuWrapperMessage.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.VcuWrapperMessage} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.VcuWrapperMessage.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getDrive();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.Drive.serializeBinaryToWriter
    );
  }
  f = message.getOrbit();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      proto.Orbit.serializeBinaryToWriter
    );
  }
  f = message.getHalt();
  if (f != null) {
    writer.writeMessage(
      3,
      f,
      proto.Halt.serializeBinaryToWriter
    );
  }
};


/**
 * optional Drive drive = 1;
 * @return {?proto.Drive}
 */
proto.VcuWrapperMessage.prototype.getDrive = function() {
  return /** @type{?proto.Drive} */ (
    jspb.Message.getWrapperField(this, proto.Drive, 1));
};


/** @param {?proto.Drive|undefined} value */
proto.VcuWrapperMessage.prototype.setDrive = function(value) {
  jspb.Message.setOneofWrapperField(this, 1, proto.VcuWrapperMessage.oneofGroups_[0], value);
};


proto.VcuWrapperMessage.prototype.clearDrive = function() {
  this.setDrive(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.VcuWrapperMessage.prototype.hasDrive = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional Orbit orbit = 2;
 * @return {?proto.Orbit}
 */
proto.VcuWrapperMessage.prototype.getOrbit = function() {
  return /** @type{?proto.Orbit} */ (
    jspb.Message.getWrapperField(this, proto.Orbit, 2));
};


/** @param {?proto.Orbit|undefined} value */
proto.VcuWrapperMessage.prototype.setOrbit = function(value) {
  jspb.Message.setOneofWrapperField(this, 2, proto.VcuWrapperMessage.oneofGroups_[0], value);
};


proto.VcuWrapperMessage.prototype.clearOrbit = function() {
  this.setOrbit(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.VcuWrapperMessage.prototype.hasOrbit = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional Halt halt = 3;
 * @return {?proto.Halt}
 */
proto.VcuWrapperMessage.prototype.getHalt = function() {
  return /** @type{?proto.Halt} */ (
    jspb.Message.getWrapperField(this, proto.Halt, 3));
};


/** @param {?proto.Halt|undefined} value */
proto.VcuWrapperMessage.prototype.setHalt = function(value) {
  jspb.Message.setOneofWrapperField(this, 3, proto.VcuWrapperMessage.oneofGroups_[0], value);
};


proto.VcuWrapperMessage.prototype.clearHalt = function() {
  this.setHalt(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.VcuWrapperMessage.prototype.hasHalt = function() {
  return jspb.Message.getField(this, 3) != null;
};


goog.object.extend(exports, proto);
