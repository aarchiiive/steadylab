// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__rosidl_typesupport_fastrtps_cpp.hpp.em
// with input from serial_communication:msg/WriteCar.idl
// generated code does not contain a copyright notice

#ifndef SERIAL_COMMUNICATION__MSG__DETAIL__WRITE_CAR__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
#define SERIAL_COMMUNICATION__MSG__DETAIL__WRITE_CAR__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_

#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "serial_communication/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"
#include "serial_communication/msg/detail/write_car__struct.hpp"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

#include "fastcdr/Cdr.h"

namespace serial_communication
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_serial_communication
cdr_serialize(
  const serial_communication::msg::WriteCar & ros_message,
  eprosima::fastcdr::Cdr & cdr);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_serial_communication
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  serial_communication::msg::WriteCar & ros_message);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_serial_communication
get_serialized_size(
  const serial_communication::msg::WriteCar & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_serial_communication
max_serialized_size_WriteCar(
  bool & full_bounded,
  size_t current_alignment);

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace serial_communication

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_serial_communication
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, serial_communication, msg, WriteCar)();

#ifdef __cplusplus
}
#endif

#endif  // SERIAL_COMMUNICATION__MSG__DETAIL__WRITE_CAR__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
