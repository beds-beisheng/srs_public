"""autogenerated by genmsg_py from GraspConfiguration.msg. Do not edit."""
import roslib.message
import struct

import trajectory_msgs.msg
import geometry_msgs.msg
import roslib.rostime
import std_msgs.msg

class GraspConfiguration(roslib.message.Message):
  _md5sum = "f1e80ea7ab7da5c201d60456d8ca5421"
  _type = "srs_msgs/GraspConfiguration"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int32 object_id
string hand_type
trajectory_msgs/JointTrajectory sconfiguration
geometry_msgs/PoseStamped palm_pose
geometry_msgs/PoseStamped pre_grasp
string category
float32 score

================================================================================
MSG: trajectory_msgs/JointTrajectory
Header header
string[] joint_names
JointTrajectoryPoint[] points
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: trajectory_msgs/JointTrajectoryPoint
float64[] positions
float64[] velocities
float64[] accelerations
duration time_from_start
================================================================================
MSG: geometry_msgs/PoseStamped
# A Pose with reference coordinate frame and timestamp
Header header
Pose pose

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of postion and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

"""
  __slots__ = ['object_id','hand_type','sconfiguration','palm_pose','pre_grasp','category','score']
  _slot_types = ['int32','string','trajectory_msgs/JointTrajectory','geometry_msgs/PoseStamped','geometry_msgs/PoseStamped','string','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.
    
    The available fields are:
       object_id,hand_type,sconfiguration,palm_pose,pre_grasp,category,score
    
    @param args: complete set of field values, in .msg order
    @param kwds: use keyword arguments corresponding to message field names
    to set specific fields. 
    """
    if args or kwds:
      super(GraspConfiguration, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.object_id is None:
        self.object_id = 0
      if self.hand_type is None:
        self.hand_type = ''
      if self.sconfiguration is None:
        self.sconfiguration = trajectory_msgs.msg.JointTrajectory()
      if self.palm_pose is None:
        self.palm_pose = geometry_msgs.msg.PoseStamped()
      if self.pre_grasp is None:
        self.pre_grasp = geometry_msgs.msg.PoseStamped()
      if self.category is None:
        self.category = ''
      if self.score is None:
        self.score = 0.
    else:
      self.object_id = 0
      self.hand_type = ''
      self.sconfiguration = trajectory_msgs.msg.JointTrajectory()
      self.palm_pose = geometry_msgs.msg.PoseStamped()
      self.pre_grasp = geometry_msgs.msg.PoseStamped()
      self.category = ''
      self.score = 0.

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
      buff.write(_struct_i.pack(self.object_id))
      _x = self.hand_type
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x.encode()))
      _x = self
      buff.write(_struct_3I.pack(_x.sconfiguration.header.seq, _x.sconfiguration.header.stamp.secs, _x.sconfiguration.header.stamp.nsecs))
      _x = self.sconfiguration.header.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x.encode()))
      length = len(self.sconfiguration.joint_names)
      buff.write(_struct_I.pack(length))
      for val1 in self.sconfiguration.joint_names:
        length = len(val1)
        buff.write(struct.pack('<I%ss'%length, length, val1.encode()))
      length = len(self.sconfiguration.points)
      buff.write(_struct_I.pack(length))
      for val1 in self.sconfiguration.points:
        length = len(val1.positions)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(struct.pack(pattern, *val1.positions))
        length = len(val1.velocities)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(struct.pack(pattern, *val1.velocities))
        length = len(val1.accelerations)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(struct.pack(pattern, *val1.accelerations))
        _v1 = val1.time_from_start
        _x = _v1
        buff.write(_struct_2i.pack(_x.secs, _x.nsecs))
      _x = self
      buff.write(_struct_3I.pack(_x.palm_pose.header.seq, _x.palm_pose.header.stamp.secs, _x.palm_pose.header.stamp.nsecs))
      _x = self.palm_pose.header.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x.encode()))
      _x = self
      buff.write(_struct_7d3I.pack(_x.palm_pose.pose.position.x, _x.palm_pose.pose.position.y, _x.palm_pose.pose.position.z, _x.palm_pose.pose.orientation.x, _x.palm_pose.pose.orientation.y, _x.palm_pose.pose.orientation.z, _x.palm_pose.pose.orientation.w, _x.pre_grasp.header.seq, _x.pre_grasp.header.stamp.secs, _x.pre_grasp.header.stamp.nsecs))
      _x = self.pre_grasp.header.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x.encode()))
      _x = self
      buff.write(_struct_7d.pack(_x.pre_grasp.pose.position.x, _x.pre_grasp.pose.position.y, _x.pre_grasp.pose.position.z, _x.pre_grasp.pose.orientation.x, _x.pre_grasp.pose.orientation.y, _x.pre_grasp.pose.orientation.z, _x.pre_grasp.pose.orientation.w))
      _x = self.category
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x.encode()))
      buff.write(_struct_f.pack(self.score))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    @param str: byte array of serialized message
    @type  str: str
    """
    try:
      if self.sconfiguration is None:
        self.sconfiguration = trajectory_msgs.msg.JointTrajectory()
      if self.palm_pose is None:
        self.palm_pose = geometry_msgs.msg.PoseStamped()
      if self.pre_grasp is None:
        self.pre_grasp = geometry_msgs.msg.PoseStamped()
      end = 0
      start = end
      end += 4
      (self.object_id,) = _struct_i.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.hand_type = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.sconfiguration.header.seq, _x.sconfiguration.header.stamp.secs, _x.sconfiguration.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.sconfiguration.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.sconfiguration.joint_names = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        val1 = str[start:end]
        self.sconfiguration.joint_names.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.sconfiguration.points = []
      for i in range(0, length):
        val1 = trajectory_msgs.msg.JointTrajectoryPoint()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        val1.positions = struct.unpack(pattern, str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        val1.velocities = struct.unpack(pattern, str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        val1.accelerations = struct.unpack(pattern, str[start:end])
        _v2 = val1.time_from_start
        _x = _v2
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2i.unpack(str[start:end])
        self.sconfiguration.points.append(val1)
      _x = self
      start = end
      end += 12
      (_x.palm_pose.header.seq, _x.palm_pose.header.stamp.secs, _x.palm_pose.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.palm_pose.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 68
      (_x.palm_pose.pose.position.x, _x.palm_pose.pose.position.y, _x.palm_pose.pose.position.z, _x.palm_pose.pose.orientation.x, _x.palm_pose.pose.orientation.y, _x.palm_pose.pose.orientation.z, _x.palm_pose.pose.orientation.w, _x.pre_grasp.header.seq, _x.pre_grasp.header.stamp.secs, _x.pre_grasp.header.stamp.nsecs,) = _struct_7d3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.pre_grasp.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.pre_grasp.pose.position.x, _x.pre_grasp.pose.position.y, _x.pre_grasp.pose.position.z, _x.pre_grasp.pose.orientation.x, _x.pre_grasp.pose.orientation.y, _x.pre_grasp.pose.orientation.z, _x.pre_grasp.pose.orientation.w,) = _struct_7d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.category = str[start:end]
      start = end
      end += 4
      (self.score,) = _struct_f.unpack(str[start:end])
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
      buff.write(_struct_i.pack(self.object_id))
      _x = self.hand_type
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x.encode()))
      _x = self
      buff.write(_struct_3I.pack(_x.sconfiguration.header.seq, _x.sconfiguration.header.stamp.secs, _x.sconfiguration.header.stamp.nsecs))
      _x = self.sconfiguration.header.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x.encode()))
      length = len(self.sconfiguration.joint_names)
      buff.write(_struct_I.pack(length))
      for val1 in self.sconfiguration.joint_names:
        length = len(val1)
        buff.write(struct.pack('<I%ss'%length, length, val1.encode()))
      length = len(self.sconfiguration.points)
      buff.write(_struct_I.pack(length))
      for val1 in self.sconfiguration.points:
        length = len(val1.positions)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(val1.positions.tostring())
        length = len(val1.velocities)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(val1.velocities.tostring())
        length = len(val1.accelerations)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(val1.accelerations.tostring())
        _v3 = val1.time_from_start
        _x = _v3
        buff.write(_struct_2i.pack(_x.secs, _x.nsecs))
      _x = self
      buff.write(_struct_3I.pack(_x.palm_pose.header.seq, _x.palm_pose.header.stamp.secs, _x.palm_pose.header.stamp.nsecs))
      _x = self.palm_pose.header.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x.encode()))
      _x = self
      buff.write(_struct_7d3I.pack(_x.palm_pose.pose.position.x, _x.palm_pose.pose.position.y, _x.palm_pose.pose.position.z, _x.palm_pose.pose.orientation.x, _x.palm_pose.pose.orientation.y, _x.palm_pose.pose.orientation.z, _x.palm_pose.pose.orientation.w, _x.pre_grasp.header.seq, _x.pre_grasp.header.stamp.secs, _x.pre_grasp.header.stamp.nsecs))
      _x = self.pre_grasp.header.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x.encode()))
      _x = self
      buff.write(_struct_7d.pack(_x.pre_grasp.pose.position.x, _x.pre_grasp.pose.position.y, _x.pre_grasp.pose.position.z, _x.pre_grasp.pose.orientation.x, _x.pre_grasp.pose.orientation.y, _x.pre_grasp.pose.orientation.z, _x.pre_grasp.pose.orientation.w))
      _x = self.category
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x.encode()))
      buff.write(_struct_f.pack(self.score))
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
      if self.sconfiguration is None:
        self.sconfiguration = trajectory_msgs.msg.JointTrajectory()
      if self.palm_pose is None:
        self.palm_pose = geometry_msgs.msg.PoseStamped()
      if self.pre_grasp is None:
        self.pre_grasp = geometry_msgs.msg.PoseStamped()
      end = 0
      start = end
      end += 4
      (self.object_id,) = _struct_i.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.hand_type = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.sconfiguration.header.seq, _x.sconfiguration.header.stamp.secs, _x.sconfiguration.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.sconfiguration.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.sconfiguration.joint_names = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        val1 = str[start:end]
        self.sconfiguration.joint_names.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.sconfiguration.points = []
      for i in range(0, length):
        val1 = trajectory_msgs.msg.JointTrajectoryPoint()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        val1.positions = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        val1.velocities = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        val1.accelerations = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
        _v4 = val1.time_from_start
        _x = _v4
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2i.unpack(str[start:end])
        self.sconfiguration.points.append(val1)
      _x = self
      start = end
      end += 12
      (_x.palm_pose.header.seq, _x.palm_pose.header.stamp.secs, _x.palm_pose.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.palm_pose.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 68
      (_x.palm_pose.pose.position.x, _x.palm_pose.pose.position.y, _x.palm_pose.pose.position.z, _x.palm_pose.pose.orientation.x, _x.palm_pose.pose.orientation.y, _x.palm_pose.pose.orientation.z, _x.palm_pose.pose.orientation.w, _x.pre_grasp.header.seq, _x.pre_grasp.header.stamp.secs, _x.pre_grasp.header.stamp.nsecs,) = _struct_7d3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.pre_grasp.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.pre_grasp.pose.position.x, _x.pre_grasp.pose.position.y, _x.pre_grasp.pose.position.z, _x.pre_grasp.pose.orientation.x, _x.pre_grasp.pose.orientation.y, _x.pre_grasp.pose.orientation.z, _x.pre_grasp.pose.orientation.w,) = _struct_7d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.category = str[start:end]
      start = end
      end += 4
      (self.score,) = _struct_f.unpack(str[start:end])
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

_struct_I = roslib.message.struct_I
_struct_7d = struct.Struct("<7d")
_struct_f = struct.Struct("<f")
_struct_i = struct.Struct("<i")
_struct_7d3I = struct.Struct("<7d3I")
_struct_3I = struct.Struct("<3I")
_struct_2i = struct.Struct("<2i")
