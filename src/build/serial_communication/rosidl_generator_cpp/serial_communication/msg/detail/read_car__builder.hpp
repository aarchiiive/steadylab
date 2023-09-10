// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from serial_communication:msg/ReadCar.idl
// generated code does not contain a copyright notice

#ifndef SERIAL_COMMUNICATION__MSG__DETAIL__READ_CAR__BUILDER_HPP_
#define SERIAL_COMMUNICATION__MSG__DETAIL__READ_CAR__BUILDER_HPP_

#include "serial_communication/msg/detail/read_car__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace serial_communication
{

namespace msg
{

namespace builder
{

class Init_ReadCar_read_accel
{
public:
  explicit Init_ReadCar_read_accel(::serial_communication::msg::ReadCar & msg)
  : msg_(msg)
  {}
  ::serial_communication::msg::ReadCar read_accel(::serial_communication::msg::ReadCar::_read_accel_type arg)
  {
    msg_.read_accel = std::move(arg);
    return std::move(msg_);
  }

private:
  ::serial_communication::msg::ReadCar msg_;
};

class Init_ReadCar_read_velocity
{
public:
  explicit Init_ReadCar_read_velocity(::serial_communication::msg::ReadCar & msg)
  : msg_(msg)
  {}
  Init_ReadCar_read_accel read_velocity(::serial_communication::msg::ReadCar::_read_velocity_type arg)
  {
    msg_.read_velocity = std::move(arg);
    return Init_ReadCar_read_accel(msg_);
  }

private:
  ::serial_communication::msg::ReadCar msg_;
};

class Init_ReadCar_read_yaw
{
public:
  explicit Init_ReadCar_read_yaw(::serial_communication::msg::ReadCar & msg)
  : msg_(msg)
  {}
  Init_ReadCar_read_velocity read_yaw(::serial_communication::msg::ReadCar::_read_yaw_type arg)
  {
    msg_.read_yaw = std::move(arg);
    return Init_ReadCar_read_velocity(msg_);
  }

private:
  ::serial_communication::msg::ReadCar msg_;
};

class Init_ReadCar_read_l
{
public:
  explicit Init_ReadCar_read_l(::serial_communication::msg::ReadCar & msg)
  : msg_(msg)
  {}
  Init_ReadCar_read_yaw read_l(::serial_communication::msg::ReadCar::_read_l_type arg)
  {
    msg_.read_l = std::move(arg);
    return Init_ReadCar_read_yaw(msg_);
  }

private:
  ::serial_communication::msg::ReadCar msg_;
};

class Init_ReadCar_read_s
{
public:
  explicit Init_ReadCar_read_s(::serial_communication::msg::ReadCar & msg)
  : msg_(msg)
  {}
  Init_ReadCar_read_l read_s(::serial_communication::msg::ReadCar::_read_s_type arg)
  {
    msg_.read_s = std::move(arg);
    return Init_ReadCar_read_l(msg_);
  }

private:
  ::serial_communication::msg::ReadCar msg_;
};

class Init_ReadCar_read_steer
{
public:
  explicit Init_ReadCar_read_steer(::serial_communication::msg::ReadCar & msg)
  : msg_(msg)
  {}
  Init_ReadCar_read_s read_steer(::serial_communication::msg::ReadCar::_read_steer_type arg)
  {
    msg_.read_steer = std::move(arg);
    return Init_ReadCar_read_s(msg_);
  }

private:
  ::serial_communication::msg::ReadCar msg_;
};

class Init_ReadCar_read_enc
{
public:
  explicit Init_ReadCar_read_enc(::serial_communication::msg::ReadCar & msg)
  : msg_(msg)
  {}
  Init_ReadCar_read_steer read_enc(::serial_communication::msg::ReadCar::_read_enc_type arg)
  {
    msg_.read_enc = std::move(arg);
    return Init_ReadCar_read_steer(msg_);
  }

private:
  ::serial_communication::msg::ReadCar msg_;
};

class Init_ReadCar_read_brake
{
public:
  explicit Init_ReadCar_read_brake(::serial_communication::msg::ReadCar & msg)
  : msg_(msg)
  {}
  Init_ReadCar_read_enc read_brake(::serial_communication::msg::ReadCar::_read_brake_type arg)
  {
    msg_.read_brake = std::move(arg);
    return Init_ReadCar_read_enc(msg_);
  }

private:
  ::serial_communication::msg::ReadCar msg_;
};

class Init_ReadCar_read_speed
{
public:
  explicit Init_ReadCar_read_speed(::serial_communication::msg::ReadCar & msg)
  : msg_(msg)
  {}
  Init_ReadCar_read_brake read_speed(::serial_communication::msg::ReadCar::_read_speed_type arg)
  {
    msg_.read_speed = std::move(arg);
    return Init_ReadCar_read_brake(msg_);
  }

private:
  ::serial_communication::msg::ReadCar msg_;
};

class Init_ReadCar_read_gear
{
public:
  explicit Init_ReadCar_read_gear(::serial_communication::msg::ReadCar & msg)
  : msg_(msg)
  {}
  Init_ReadCar_read_speed read_gear(::serial_communication::msg::ReadCar::_read_gear_type arg)
  {
    msg_.read_gear = std::move(arg);
    return Init_ReadCar_read_speed(msg_);
  }

private:
  ::serial_communication::msg::ReadCar msg_;
};

class Init_ReadCar_read_e_stop
{
public:
  explicit Init_ReadCar_read_e_stop(::serial_communication::msg::ReadCar & msg)
  : msg_(msg)
  {}
  Init_ReadCar_read_gear read_e_stop(::serial_communication::msg::ReadCar::_read_e_stop_type arg)
  {
    msg_.read_e_stop = std::move(arg);
    return Init_ReadCar_read_gear(msg_);
  }

private:
  ::serial_communication::msg::ReadCar msg_;
};

class Init_ReadCar_read_aorm
{
public:
  Init_ReadCar_read_aorm()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ReadCar_read_e_stop read_aorm(::serial_communication::msg::ReadCar::_read_aorm_type arg)
  {
    msg_.read_aorm = std::move(arg);
    return Init_ReadCar_read_e_stop(msg_);
  }

private:
  ::serial_communication::msg::ReadCar msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::serial_communication::msg::ReadCar>()
{
  return serial_communication::msg::builder::Init_ReadCar_read_aorm();
}

}  // namespace serial_communication

#endif  // SERIAL_COMMUNICATION__MSG__DETAIL__READ_CAR__BUILDER_HPP_
