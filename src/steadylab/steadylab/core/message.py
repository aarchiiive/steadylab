from std_msgs.msg import *
from sensor_msgs.msg import *
from geometry_msgs.msg import *
from nav_msgs.msg import *
from tf2_msgs.msg import *

_messages = [
    # std_msgs
    Bool,
    Byte,
    ByteMultiArray,
    Char,
    ColorRGBA,
    Empty,
    Float32,
    Float32MultiArray,
    Float64,
    Float64MultiArray,
    Header,
    Int16,
    Int16MultiArray,
    Int32,
    Int64MultiArray,
    Int8,
    Int8MultiArray,
    MultiArrayDimension,
    MultiArrayLayout,
    String,
    UInt16,
    UInt16MultiArray,
    UInt32,
    UInt32MultiArray,
    UInt64,
    UInt64MultiArray,
    UInt8,
    UInt8MultiArray,

    # sensor_msgs
    BatteryState,
    CameraInfo,
    ChannelFloat32,
    CompressedImage,
    FluidPressure,
    Illuminance,
    Image,
    Imu,
    JointState,
    Joy,
    JoyFeedback,
    JoyFeedbackArray,
    LaserEcho,
    LaserScan,
    MagneticField,
    MultiDOFJointState,
    MultiEchoLaserScan,
    NavSatFix,
    NavSatStatus,
    PointCloud,
    PointCloud2,
    PointField,
    Range,
    RegionOfInterest,
    RelativeHumidity,
    Temperature,
    TimeReference,

    # geometry_msgs
    Accel,
    AccelStamped,
    AccelWithCovariance,
    AccelWithCovarianceStamped,
    Inertia,
    InertiaStamped,
    Point,
    Point32,
    PointStamped,
    Polygon,
    PolygonStamped,
    Pose,
    Pose2D,
    PoseArray,
    PoseStamped,
    PoseWithCovariance,
    PoseWithCovarianceStamped,
    Quaternion,
    QuaternionStamped,
    Transform,
    TransformStamped,
    Twist,
    TwistStamped,
    TwistWithCovariance,
    TwistWithCovarianceStamped,
    Vector3,
    Vector3Stamped,
    Wrench,
    WrenchStamped,

    # nav_msgs
    GridCells,
    MapMetaData,
    OccupancyGrid,
    Odometry,
    Path,

    # tf2_msgs
    TF2Error,
    TFMessage,
]


def is_compatible_msg(msg_type):
    global _messages
    return msg_type in _messages


class Message:
    def __init__(self, name, topic, msg_type, processor, device=None) -> None:
        self.name = name 
        self.topic = topic 
        self.msg_type = msg_type 
        self.processor = processor
        self.device = device
        self.node_name = f"{device}_{name}" if device else f"/{name}"

        assert self.node_name != None, f"node name has {self.node_name}"

    def __str__(self) -> str:
        return self.topic