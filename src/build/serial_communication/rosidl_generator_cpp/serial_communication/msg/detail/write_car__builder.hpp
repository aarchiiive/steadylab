// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from serial_communication:msg/WriteCar.idl
// generated code does not contain a copyright notice

#ifndef SERIAL_COMMUNICATION__MSG__DETAIL__WRITE_CAR__BUILDER_HPP_
#define SERIAL_COMMUNICATION__MSG__DETAIL__WRITE_CAR__BUILDER_HPP_

#include "serial_communication/msg/detail/write_car__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace serial_communication
{

namespace msg
{

namespace builder
{

class Init_WriteCar_write_steer
{
public:
  explicit Init_WriteCar_write_steer(::serial_communication::msg::WriteCar & msg)
  : msg_(msg)
  {}
  ::serial_communication::msg::WriteCar write_steer(::serial_communication::msg::WriteCar::_write_steer_type arg)
  {
    msg_.write_steer = std::move(arg);
    return std::move(msg_);
  }

private:
  ::serial_communication::msg::WriteCar msg_;
};

class Init_WriteCar_write_brake
{
public:
  explicit Init_WriteCar_write_brake(::serial_communication::msg::WriteCar & msg)
  : msg_(msg)
  {}
  Init_WriteCar_write_steer write_brake(::serial_communication::msg::WriteCar::_write_brake_type arg)
  {
    msg_.write_brake = std::move(arg);
    return Init_WriteCar_write_steer(msg_);
  }

private:
  ::serial_communication::msg::WriteCar msg_;
};

class Init_WriteCar_write_speed
{
public:
  explicit Init_WriteCar_write_speed(::serial_communication::msg::WriteCar & msg)
  : msg_(msg)
  {}
  Init_WriteCar_write_brake write_speed(::serial_communication::msg::WriteCar::_write_speed_type arg)
  {
    msg_.write_speed = std::move(arg);
    return Init_WriteCar_write_brake(msg_);
  }

private:
  ::serial_communication::msg::WriteCar msg_;
};

class Init_WriteCar_write_gear
{
public:
  explicit Init_WriteCar_write_gear(::serial_communication::msg::WriteCar & msg)
  : msg_(msg)
  {}
  Init_WriteCar_write_speed write_gear(::serial_communication::msg::WriteCar::_write_gear_type arg)
  {
    msg_.write_gear = std::move(arg);
    return Init_WriteCar_write_speed(msg_);
  }

private:
  ::serial_communication::msg::WriteCar msg_;
};

class Init_WriteCar_write_e_stop
{
public:
  Init_WriteCar_write_e_stop()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_WriteCar_write_gear write_e_stop(::serial_communication::msg::WriteCar::_write_e_stop_type arg)
  {
    msg_.write_e_stop = std::move(arg);
    return Init_WriteCar_write_gear(msg_);
  }

private:
  ::serial_communication::msg::WriteCar msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::serial_communication::msg::WriteCar>()
{
  return serial_communication::msg::builder::Init_WriteCar_write_e_stop();
}

}  // namespace serial_communication

#endif  // SERIAL_COMMUNICATION__MSG__DETAIL__WRITE_CAR__BUILDER_HPP_
