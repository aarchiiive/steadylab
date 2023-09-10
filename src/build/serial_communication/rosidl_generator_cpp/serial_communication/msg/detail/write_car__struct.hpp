// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from serial_communication:msg/WriteCar.idl
// generated code does not contain a copyright notice

#ifndef SERIAL_COMMUNICATION__MSG__DETAIL__WRITE_CAR__STRUCT_HPP_
#define SERIAL_COMMUNICATION__MSG__DETAIL__WRITE_CAR__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__serial_communication__msg__WriteCar __attribute__((deprecated))
#else
# define DEPRECATED__serial_communication__msg__WriteCar __declspec(deprecated)
#endif

namespace serial_communication
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct WriteCar_
{
  using Type = WriteCar_<ContainerAllocator>;

  explicit WriteCar_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->write_e_stop = false;
      this->write_gear = 0;
      this->write_speed = 0;
      this->write_brake = 0;
      this->write_steer = 0l;
    }
  }

  explicit WriteCar_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->write_e_stop = false;
      this->write_gear = 0;
      this->write_speed = 0;
      this->write_brake = 0;
      this->write_steer = 0l;
    }
  }

  // field types and members
  using _write_e_stop_type =
    bool;
  _write_e_stop_type write_e_stop;
  using _write_gear_type =
    int8_t;
  _write_gear_type write_gear;
  using _write_speed_type =
    int16_t;
  _write_speed_type write_speed;
  using _write_brake_type =
    int16_t;
  _write_brake_type write_brake;
  using _write_steer_type =
    int32_t;
  _write_steer_type write_steer;

  // setters for named parameter idiom
  Type & set__write_e_stop(
    const bool & _arg)
  {
    this->write_e_stop = _arg;
    return *this;
  }
  Type & set__write_gear(
    const int8_t & _arg)
  {
    this->write_gear = _arg;
    return *this;
  }
  Type & set__write_speed(
    const int16_t & _arg)
  {
    this->write_speed = _arg;
    return *this;
  }
  Type & set__write_brake(
    const int16_t & _arg)
  {
    this->write_brake = _arg;
    return *this;
  }
  Type & set__write_steer(
    const int32_t & _arg)
  {
    this->write_steer = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    serial_communication::msg::WriteCar_<ContainerAllocator> *;
  using ConstRawPtr =
    const serial_communication::msg::WriteCar_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<serial_communication::msg::WriteCar_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<serial_communication::msg::WriteCar_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      serial_communication::msg::WriteCar_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<serial_communication::msg::WriteCar_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      serial_communication::msg::WriteCar_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<serial_communication::msg::WriteCar_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<serial_communication::msg::WriteCar_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<serial_communication::msg::WriteCar_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__serial_communication__msg__WriteCar
    std::shared_ptr<serial_communication::msg::WriteCar_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__serial_communication__msg__WriteCar
    std::shared_ptr<serial_communication::msg::WriteCar_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const WriteCar_ & other) const
  {
    if (this->write_e_stop != other.write_e_stop) {
      return false;
    }
    if (this->write_gear != other.write_gear) {
      return false;
    }
    if (this->write_speed != other.write_speed) {
      return false;
    }
    if (this->write_brake != other.write_brake) {
      return false;
    }
    if (this->write_steer != other.write_steer) {
      return false;
    }
    return true;
  }
  bool operator!=(const WriteCar_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct WriteCar_

// alias to use template instance with default allocator
using WriteCar =
  serial_communication::msg::WriteCar_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace serial_communication

#endif  // SERIAL_COMMUNICATION__MSG__DETAIL__WRITE_CAR__STRUCT_HPP_
