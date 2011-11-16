"""autogenerated by genmsg_py from UI_DMresp.msg. Do not edit."""
import roslib.message
import struct


class UI_DMresp(roslib.message.Message):
  _md5sum = "8a6185ebbeac9cd1ebbaa1b88e853b6f"
  _type = "srs_msgs/UI_DMresp"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# this message contains information to define the comunication between the Decision making (DM) and UI_Pri when an unexpected error has occured in the execution of an previously issued command

string solution   # currently supported comands from the user are: continue,give_up,move  
string parameter   # used when the command is move to carry the position. Possible vaues are:kitchen, home, order, [1.2, 3.4, 0.8] which are the coordinates from user click on the map
uint32 responseID  # the uniqie ID used by DM to distinguish which responce corresponds to which command. Note: the responceID MUST be the same as the requestID of the corresponding command

"""
  __slots__ = ['solution','parameter','responseID']
  _slot_types = ['string','string','uint32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.
    
    The available fields are:
       solution,parameter,responseID
    
    @param args: complete set of field values, in .msg order
    @param kwds: use keyword arguments corresponding to message field names
    to set specific fields. 
    """
    if args or kwds:
      super(UI_DMresp, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.solution is None:
        self.solution = ''
      if self.parameter is None:
        self.parameter = ''
      if self.responseID is None:
        self.responseID = 0
    else:
      self.solution = ''
      self.parameter = ''
      self.responseID = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    @param buff: buffer
    @type  buff: StringIO
    """
    try:
      _x = self.solution
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x.encode()))
      _x = self.parameter
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x.encode()))
      buff.write(_struct_I.pack(self.responseID))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    @param str: byte array of serialized message
    @type  str: str
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.solution = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.parameter = str[start:end]
      start = end
      end += 4
      (self.responseID,) = _struct_I.unpack(str[start:end])
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    @param buff: buffer
    @type  buff: StringIO
    @param numpy: numpy python module
    @type  numpy module
    """
    try:
      _x = self.solution
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x.encode()))
      _x = self.parameter
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x.encode()))
      buff.write(_struct_I.pack(self.responseID))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    @param str: byte array of serialized message
    @type  str: str
    @param numpy: numpy python module
    @type  numpy: module
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.solution = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.parameter = str[start:end]
      start = end
      end += 4
      (self.responseID,) = _struct_I.unpack(str[start:end])
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

_struct_I = roslib.message.struct_I
