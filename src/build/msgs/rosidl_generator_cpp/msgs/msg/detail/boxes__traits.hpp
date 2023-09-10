// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from msgs:msg/Boxes.idl
// generated code does not contain a copyright notice

#ifndef MSGS__MSG__DETAIL__BOXES__TRAITS_HPP_
#define MSGS__MSG__DETAIL__BOXES__TRAITS_HPP_

#include "msgs/msg/detail/boxes__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<msgs::msg::Boxes>()
{
  return "msgs::msg::Boxes";
}

template<>
inline const char * name<msgs::msg::Boxes>()
{
  return "msgs/msg/Boxes";
}

template<>
struct has_fixed_size<msgs::msg::Boxes>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<msgs::msg::Boxes>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<msgs::msg::Boxes>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // MSGS__MSG__DETAIL__BOXES__TRAITS_HPP_
