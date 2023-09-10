// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from serial_communication:msg/ReadCar.idl
// generated code does not contain a copyright notice

#ifndef SERIAL_COMMUNICATION__MSG__DETAIL__READ_CAR__STRUCT_HPP_
#define SERIAL_COMMUNICATION__MSG__DETAIL__READ_CAR__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__serial_communication__msg__ReadCar __attribute__((deprecated))
#else
# define DEPRECATED__serial_communication__msg__ReadCar __declspec(deprecated)
#endif

namespace serial_communication
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct ReadCar_
{
  using Type = ReadCar_<ContainerAllocator>;

  explicit ReadCar_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->read_aorm = false;
      this->read_e_stop = false;
      this->read_gear = 0;
      this->read_speed = 0;
      this->read_brake = 0;
      this->read_enc = 0ll;
      this->read_steer = 0l;
      this->read_s = 0.0;
      this->read_l = 0.0;
      this->read_yaw = 0.0;
      this->read_velocity = 0.0;
      this->read_accel = 0.0;
    }
  }

  explicit ReadCar_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->read_aorm = false;
      this->read_e_stop = false;
      this->read_gear = 0;
      this->read_speed = 0;
      this->read_brake = 0;
      this->read_enc = 0ll;
      this->read_steer = 0l;
      this->read_s = 0.0;
      this->read_l = 0.0;
      this->read_yaw = 0.0;
      this->read_velocity = 0.0;
      this->read_accel = 0.0;
    }
  }

  // field types and members
  using _read_aorm_type =
    bool;
  _read_aorm_type read_aorm;
  using _read_e_stop_type =
    bool;
  _read_e_stop_type read_e_stop;
  using _read_gear_type =
    int8_t;
  _read_gear_type read_gear;
  using _read_speed_type =
    int16_t;
  _read_speed_type read_speed;
  using _read_brake_type =
    int16_t;
  _read_brake_type read_brake;
  using _read_enc_type =
    int64_t;
  _read_enc_type read_enc;
  using _read_steer_type =
    int32_t;
  _read_steer_type read_steer;
  using _read_s_type =
    double;
  _read_s_type read_s;
  using _read_l_type =
    double;
  _read_l_type read_l;
  using _read_yaw_type =
    double;
  _read_yaw_type read_yaw;
  using _read_velocity_type =
    double;
  _read_velocity_type read_velocity;
  using _read_accel_type =
    double;
  _read_accel_type read_accel;

  // setters for named parameter idiom
  Type & set__read_aorm(
    const bool & _arg)
  {
    this->read_aorm = _arg;
    return *this;
  }
  Type & set__read_e_stop(
    const bool & _arg)
  {
    this->read_e_stop = _arg;
    return *this;
  }
  Type & set__read_gear(
    const int8_t & _arg)
  {
    this->read_gear = _arg;
    return *this;
  }
  Type & set__read_speed(
    const int16_t & _arg)
  {
    this->read_speed = _arg;
    return *this;
  }
  Type & set__read_brake(
    const int16_t & _arg)
  {
    this->read_brake = _arg;
    return *this;
  }
  Type & set__read_enc(
    const int64_t & _arg)
  {
    this->read_enc = _arg;
    return *this;
  }
  Type & set__read_steer(
    const int32_t & _arg)
  {
    this->read_steer = _arg;
    return *this;
  }
  Type & set__read_s(
    const double & _arg)
  {
    this->read_s = _arg;
    return *this;
  }
  Type & set__read_l(
    const double & _arg)
  {
    this->read_l = _arg;
    return *this;
  }
  Type & set__read_yaw(
    const double & _arg)
  {
    this->read_yaw = _arg;
    return *this;
  }
  Type & set__read_velocity(
    const double & _arg)
  {
    this->read_velocity = _arg;
    return *this;
  }
  Type & set__read_accel(
    const double & _arg)
  {
    this->read_accel = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    serial_communication::msg::ReadCar_<ContainerAllocator> *;
  using ConstRawPtr =
    const serial_communication::msg::ReadCar_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<serial_communication::msg::ReadCar_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<serial_communication::msg::ReadCar_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      serial_communication::msg::ReadCar_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<serial_communication::msg::ReadCar_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      serial_communication::msg::ReadCar_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<serial_communication::msg::ReadCar_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<serial_communication::msg::ReadCar_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<serial_communication::msg::ReadCar_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__serial_communication__msg__ReadCar
    std::shared_ptr<serial_communication::msg::ReadCar_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__serial_communication__msg__ReadCar
    std::shared_ptr<serial_communication::msg::ReadCar_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ReadCar_ & other) const
  {
    if (this->read_aorm != other.read_aorm) {
      return false;
    }
    if (this->read_e_stop != other.read_e_stop) {
      return false;
    }
    if (this->read_gear != other.read_gear) {
      return false;
    }
    if (this->read_speed != other.read_speed) {
      return false;
    }
    if (this->read_brake != other.read_brake) {
      return false;
    }
    if (this->read_enc != other.read_enc) {
      return false;
    }
    if (this->read_steer != other.read_steer) {
      return false;
    }
    if (this->read_s != other.read_s) {
      return false;
    }
    if (this->read_l != other.read_l) {
      return false;
    }
    if (this->read_yaw != other.read_yaw) {
      return false;
    }
    if (this->read_velocity != other.read_velocity) {
      return false;
    }
    if (this->read_accel != other.read_accel) {
      return false;
    }
    return true;
  }
  bool operator!=(const ReadCar_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ReadCar_

// alias to use template instance with default allocator
using ReadCar =
  serial_communication::msg::ReadCar_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace serial_communication

#endif  // SERIAL_COMMUNICATION__MSG__DETAIL__READ_CAR__STRUCT_HPP_
