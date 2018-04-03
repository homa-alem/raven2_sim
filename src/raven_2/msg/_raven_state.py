# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from raven_2/raven_state.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import genpy
import std_msgs.msg

class raven_state(genpy.Message):
  _md5sum = "f0370e49caffda1d79af0d5849568123"
  _type = "raven_2/raven_state"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """Header      hdr
int32       runlevel
int32       sublevel
int32       last_seq
int32[2]    type
int32[6]    pos
float32[18]   ori
float32[18]   ori_d
int32[6]    pos_d
duration    dt
int32[16]   encVals
int32[16]   dac_val	
float32[16] tau
float32[16] mpos
float32[16] jpos
float32[16] mvel
float32[16] mvel_d
float32[16] jvel
float32[16] mpos_d
float32[16] jpos_d
float32[2]  grasp_d
float32[16] encoffsets
int32[16] current_cmd
float32[3] sim_mpos
float32[3] sim_mvel
float32[3] sim_jpos
char[1024] err_msg

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id
"""
  __slots__ = ['hdr','runlevel','sublevel','last_seq','type','pos','ori','ori_d','pos_d','dt','encVals','dac_val','tau','mpos','jpos','mvel','mvel_d','jvel','mpos_d','jpos_d','grasp_d','encoffsets','current_cmd','sim_mpos','sim_mvel','sim_jpos','err_msg']
  _slot_types = ['std_msgs/Header','int32','int32','int32','int32[2]','int32[6]','float32[18]','float32[18]','int32[6]','duration','int32[16]','int32[16]','float32[16]','float32[16]','float32[16]','float32[16]','float32[16]','float32[16]','float32[16]','float32[16]','float32[2]','float32[16]','int32[16]','float32[3]','float32[3]','float32[3]','char[1024]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       hdr,runlevel,sublevel,last_seq,type,pos,ori,ori_d,pos_d,dt,encVals,dac_val,tau,mpos,jpos,mvel,mvel_d,jvel,mpos_d,jpos_d,grasp_d,encoffsets,current_cmd,sim_mpos,sim_mvel,sim_jpos,err_msg

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(raven_state, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.hdr is None:
        self.hdr = std_msgs.msg.Header()
      if self.runlevel is None:
        self.runlevel = 0
      if self.sublevel is None:
        self.sublevel = 0
      if self.last_seq is None:
        self.last_seq = 0
      if self.type is None:
        self.type = [0] * 2
      if self.pos is None:
        self.pos = [0] * 6
      if self.ori is None:
        self.ori = [0.] * 18
      if self.ori_d is None:
        self.ori_d = [0.] * 18
      if self.pos_d is None:
        self.pos_d = [0] * 6
      if self.dt is None:
        self.dt = genpy.Duration()
      if self.encVals is None:
        self.encVals = [0] * 16
      if self.dac_val is None:
        self.dac_val = [0] * 16
      if self.tau is None:
        self.tau = [0.] * 16
      if self.mpos is None:
        self.mpos = [0.] * 16
      if self.jpos is None:
        self.jpos = [0.] * 16
      if self.mvel is None:
        self.mvel = [0.] * 16
      if self.mvel_d is None:
        self.mvel_d = [0.] * 16
      if self.jvel is None:
        self.jvel = [0.] * 16
      if self.mpos_d is None:
        self.mpos_d = [0.] * 16
      if self.jpos_d is None:
        self.jpos_d = [0.] * 16
      if self.grasp_d is None:
        self.grasp_d = [0.] * 2
      if self.encoffsets is None:
        self.encoffsets = [0.] * 16
      if self.current_cmd is None:
        self.current_cmd = [0] * 16
      if self.sim_mpos is None:
        self.sim_mpos = [0.] * 3
      if self.sim_mvel is None:
        self.sim_mvel = [0.] * 3
      if self.sim_jpos is None:
        self.sim_jpos = [0.] * 3
      if self.err_msg is None:
        self.err_msg = b'\0'*1024
    else:
      self.hdr = std_msgs.msg.Header()
      self.runlevel = 0
      self.sublevel = 0
      self.last_seq = 0
      self.type = [0] * 2
      self.pos = [0] * 6
      self.ori = [0.] * 18
      self.ori_d = [0.] * 18
      self.pos_d = [0] * 6
      self.dt = genpy.Duration()
      self.encVals = [0] * 16
      self.dac_val = [0] * 16
      self.tau = [0.] * 16
      self.mpos = [0.] * 16
      self.jpos = [0.] * 16
      self.mvel = [0.] * 16
      self.mvel_d = [0.] * 16
      self.jvel = [0.] * 16
      self.mpos_d = [0.] * 16
      self.jpos_d = [0.] * 16
      self.grasp_d = [0.] * 2
      self.encoffsets = [0.] * 16
      self.current_cmd = [0] * 16
      self.sim_mpos = [0.] * 3
      self.sim_mvel = [0.] * 3
      self.sim_jpos = [0.] * 3
      self.err_msg = b'\0'*1024

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.hdr.seq, _x.hdr.stamp.secs, _x.hdr.stamp.nsecs))
      _x = self.hdr.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_3i().pack(_x.runlevel, _x.sublevel, _x.last_seq))
      buff.write(_get_struct_2i().pack(*self.type))
      buff.write(_get_struct_6i().pack(*self.pos))
      buff.write(_get_struct_18f().pack(*self.ori))
      buff.write(_get_struct_18f().pack(*self.ori_d))
      buff.write(_get_struct_6i().pack(*self.pos_d))
      _x = self
      buff.write(_get_struct_2i().pack(_x.dt.secs, _x.dt.nsecs))
      buff.write(_get_struct_16i().pack(*self.encVals))
      buff.write(_get_struct_16i().pack(*self.dac_val))
      buff.write(_get_struct_16f().pack(*self.tau))
      buff.write(_get_struct_16f().pack(*self.mpos))
      buff.write(_get_struct_16f().pack(*self.jpos))
      buff.write(_get_struct_16f().pack(*self.mvel))
      buff.write(_get_struct_16f().pack(*self.mvel_d))
      buff.write(_get_struct_16f().pack(*self.jvel))
      buff.write(_get_struct_16f().pack(*self.mpos_d))
      buff.write(_get_struct_16f().pack(*self.jpos_d))
      buff.write(_get_struct_2f().pack(*self.grasp_d))
      buff.write(_get_struct_16f().pack(*self.encoffsets))
      buff.write(_get_struct_16i().pack(*self.current_cmd))
      buff.write(_get_struct_3f().pack(*self.sim_mpos))
      buff.write(_get_struct_3f().pack(*self.sim_mvel))
      buff.write(_get_struct_3f().pack(*self.sim_jpos))
      _x = self.err_msg
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_get_struct_1024B().pack(*_x))
      else:
        buff.write(_get_struct_1024s().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.hdr is None:
        self.hdr = std_msgs.msg.Header()
      if self.dt is None:
        self.dt = genpy.Duration()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.hdr.seq, _x.hdr.stamp.secs, _x.hdr.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.hdr.frame_id = str[start:end].decode('utf-8')
      else:
        self.hdr.frame_id = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.runlevel, _x.sublevel, _x.last_seq,) = _get_struct_3i().unpack(str[start:end])
      start = end
      end += 8
      self.type = _get_struct_2i().unpack(str[start:end])
      start = end
      end += 24
      self.pos = _get_struct_6i().unpack(str[start:end])
      start = end
      end += 72
      self.ori = _get_struct_18f().unpack(str[start:end])
      start = end
      end += 72
      self.ori_d = _get_struct_18f().unpack(str[start:end])
      start = end
      end += 24
      self.pos_d = _get_struct_6i().unpack(str[start:end])
      _x = self
      start = end
      end += 8
      (_x.dt.secs, _x.dt.nsecs,) = _get_struct_2i().unpack(str[start:end])
      start = end
      end += 64
      self.encVals = _get_struct_16i().unpack(str[start:end])
      start = end
      end += 64
      self.dac_val = _get_struct_16i().unpack(str[start:end])
      start = end
      end += 64
      self.tau = _get_struct_16f().unpack(str[start:end])
      start = end
      end += 64
      self.mpos = _get_struct_16f().unpack(str[start:end])
      start = end
      end += 64
      self.jpos = _get_struct_16f().unpack(str[start:end])
      start = end
      end += 64
      self.mvel = _get_struct_16f().unpack(str[start:end])
      start = end
      end += 64
      self.mvel_d = _get_struct_16f().unpack(str[start:end])
      start = end
      end += 64
      self.jvel = _get_struct_16f().unpack(str[start:end])
      start = end
      end += 64
      self.mpos_d = _get_struct_16f().unpack(str[start:end])
      start = end
      end += 64
      self.jpos_d = _get_struct_16f().unpack(str[start:end])
      start = end
      end += 8
      self.grasp_d = _get_struct_2f().unpack(str[start:end])
      start = end
      end += 64
      self.encoffsets = _get_struct_16f().unpack(str[start:end])
      start = end
      end += 64
      self.current_cmd = _get_struct_16i().unpack(str[start:end])
      start = end
      end += 12
      self.sim_mpos = _get_struct_3f().unpack(str[start:end])
      start = end
      end += 12
      self.sim_mvel = _get_struct_3f().unpack(str[start:end])
      start = end
      end += 12
      self.sim_jpos = _get_struct_3f().unpack(str[start:end])
      start = end
      end += 1024
      self.err_msg = str[start:end]
      self.dt.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.hdr.seq, _x.hdr.stamp.secs, _x.hdr.stamp.nsecs))
      _x = self.hdr.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_3i().pack(_x.runlevel, _x.sublevel, _x.last_seq))
      buff.write(self.type.tostring())
      buff.write(self.pos.tostring())
      buff.write(self.ori.tostring())
      buff.write(self.ori_d.tostring())
      buff.write(self.pos_d.tostring())
      _x = self
      buff.write(_get_struct_2i().pack(_x.dt.secs, _x.dt.nsecs))
      buff.write(self.encVals.tostring())
      buff.write(self.dac_val.tostring())
      buff.write(self.tau.tostring())
      buff.write(self.mpos.tostring())
      buff.write(self.jpos.tostring())
      buff.write(self.mvel.tostring())
      buff.write(self.mvel_d.tostring())
      buff.write(self.jvel.tostring())
      buff.write(self.mpos_d.tostring())
      buff.write(self.jpos_d.tostring())
      buff.write(self.grasp_d.tostring())
      buff.write(self.encoffsets.tostring())
      buff.write(self.current_cmd.tostring())
      buff.write(self.sim_mpos.tostring())
      buff.write(self.sim_mvel.tostring())
      buff.write(self.sim_jpos.tostring())
      _x = self.err_msg
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_get_struct_1024B().pack(*_x))
      else:
        buff.write(_get_struct_1024s().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.hdr is None:
        self.hdr = std_msgs.msg.Header()
      if self.dt is None:
        self.dt = genpy.Duration()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.hdr.seq, _x.hdr.stamp.secs, _x.hdr.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.hdr.frame_id = str[start:end].decode('utf-8')
      else:
        self.hdr.frame_id = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.runlevel, _x.sublevel, _x.last_seq,) = _get_struct_3i().unpack(str[start:end])
      start = end
      end += 8
      self.type = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=2)
      start = end
      end += 24
      self.pos = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=6)
      start = end
      end += 72
      self.ori = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=18)
      start = end
      end += 72
      self.ori_d = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=18)
      start = end
      end += 24
      self.pos_d = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=6)
      _x = self
      start = end
      end += 8
      (_x.dt.secs, _x.dt.nsecs,) = _get_struct_2i().unpack(str[start:end])
      start = end
      end += 64
      self.encVals = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=16)
      start = end
      end += 64
      self.dac_val = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=16)
      start = end
      end += 64
      self.tau = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=16)
      start = end
      end += 64
      self.mpos = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=16)
      start = end
      end += 64
      self.jpos = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=16)
      start = end
      end += 64
      self.mvel = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=16)
      start = end
      end += 64
      self.mvel_d = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=16)
      start = end
      end += 64
      self.jvel = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=16)
      start = end
      end += 64
      self.mpos_d = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=16)
      start = end
      end += 64
      self.jpos_d = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=16)
      start = end
      end += 8
      self.grasp_d = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=2)
      start = end
      end += 64
      self.encoffsets = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=16)
      start = end
      end += 64
      self.current_cmd = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=16)
      start = end
      end += 12
      self.sim_mpos = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=3)
      start = end
      end += 12
      self.sim_mvel = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=3)
      start = end
      end += 12
      self.sim_jpos = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=3)
      start = end
      end += 1024
      self.err_msg = str[start:end]
      self.dt.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_18f = None
def _get_struct_18f():
    global _struct_18f
    if _struct_18f is None:
        _struct_18f = struct.Struct("<18f")
    return _struct_18f
_struct_16i = None
def _get_struct_16i():
    global _struct_16i
    if _struct_16i is None:
        _struct_16i = struct.Struct("<16i")
    return _struct_16i
_struct_1024B = None
def _get_struct_1024B():
    global _struct_1024B
    if _struct_1024B is None:
        _struct_1024B = struct.Struct("<1024B")
    return _struct_1024B
_struct_6i = None
def _get_struct_6i():
    global _struct_6i
    if _struct_6i is None:
        _struct_6i = struct.Struct("<6i")
    return _struct_6i
_struct_16f = None
def _get_struct_16f():
    global _struct_16f
    if _struct_16f is None:
        _struct_16f = struct.Struct("<16f")
    return _struct_16f
_struct_3i = None
def _get_struct_3i():
    global _struct_3i
    if _struct_3i is None:
        _struct_3i = struct.Struct("<3i")
    return _struct_3i
_struct_3f = None
def _get_struct_3f():
    global _struct_3f
    if _struct_3f is None:
        _struct_3f = struct.Struct("<3f")
    return _struct_3f
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_2f = None
def _get_struct_2f():
    global _struct_2f
    if _struct_2f is None:
        _struct_2f = struct.Struct("<2f")
    return _struct_2f
_struct_1024s = None
def _get_struct_1024s():
    global _struct_1024s
    if _struct_1024s is None:
        _struct_1024s = struct.Struct("<1024s")
    return _struct_1024s
_struct_2i = None
def _get_struct_2i():
    global _struct_2i
    if _struct_2i is None:
        _struct_2i = struct.Struct("<2i")
    return _struct_2i
