// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from msgs:msg/Boxes.idl
// generated code does not contain a copyright notice

#ifndef MSGS__MSG__DETAIL__BOXES__BUILDER_HPP_
#define MSGS__MSG__DETAIL__BOXES__BUILDER_HPP_

#include "msgs/msg/detail/boxes__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace msgs
{

namespace msg
{

namespace builder
{

class Init_Boxes_a
{
public:
  Init_Boxes_a()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::msgs::msg::Boxes a(::msgs::msg::Boxes::_a_type arg)
  {
    msg_.a = std::move(arg);
    return std::move(msg_);
  }

private:
  ::msgs::msg::Boxes msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::msgs::msg::Boxes>()
{
  return msgs::msg::builder::Init_Boxes_a();
}

}  // namespace msgs

#endif  // MSGS__MSG__DETAIL__BOXES__BUILDER_HPP_
