// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from serial_communication:msg/ReadCar.idl
// generated code does not contain a copyright notice

#ifndef SERIAL_COMMUNICATION__MSG__DETAIL__READ_CAR__TRAITS_HPP_
#define SERIAL_COMMUNICATION__MSG__DETAIL__READ_CAR__TRAITS_HPP_

#include "serial_communication/msg/detail/read_car__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<serial_communication::msg::ReadCar>()
{
  return "serial_communication::msg::ReadCar";
}

template<>
inline const char * name<serial_communication::msg::ReadCar>()
{
  return "serial_communication/msg/ReadCar";
}

template<>
struct has_fixed_size<serial_communication::msg::ReadCar>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<serial_communication::msg::ReadCar>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<serial_communication::msg::ReadCar>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // SERIAL_COMMUNICATION__MSG__DETAIL__READ_CAR__TRAITS_HPP_
