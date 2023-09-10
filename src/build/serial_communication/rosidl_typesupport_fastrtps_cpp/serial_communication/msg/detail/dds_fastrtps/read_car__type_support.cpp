// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from serial_communication:msg/ReadCar.idl
// generated code does not contain a copyright notice
#include "serial_communication/msg/detail/read_car__rosidl_typesupport_fastrtps_cpp.hpp"
#include "serial_communication/msg/detail/read_car__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions

namespace serial_communication
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_serial_communication
cdr_serialize(
  const serial_communication::msg::ReadCar & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: read_aorm
  cdr << (ros_message.read_aorm ? true : false);
  // Member: read_e_stop
  cdr << (ros_message.read_e_stop ? true : false);
  // Member: read_gear
  cdr << ros_message.read_gear;
  // Member: read_speed
  cdr << ros_message.read_speed;
  // Member: read_brake
  cdr << ros_message.read_brake;
  // Member: read_enc
  cdr << ros_message.read_enc;
  // Member: read_steer
  cdr << ros_message.read_steer;
  // Member: read_s
  cdr << ros_message.read_s;
  // Member: read_l
  cdr << ros_message.read_l;
  // Member: read_yaw
  cdr << ros_message.read_yaw;
  // Member: read_velocity
  cdr << ros_message.read_velocity;
  // Member: read_accel
  cdr << ros_message.read_accel;
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_serial_communication
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  serial_communication::msg::ReadCar & ros_message)
{
  // Member: read_aorm
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.read_aorm = tmp ? true : false;
  }

  // Member: read_e_stop
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.read_e_stop = tmp ? true : false;
  }

  // Member: read_gear
  cdr >> ros_message.read_gear;

  // Member: read_speed
  cdr >> ros_message.read_speed;

  // Member: read_brake
  cdr >> ros_message.read_brake;

  // Member: read_enc
  cdr >> ros_message.read_enc;

  // Member: read_steer
  cdr >> ros_message.read_steer;

  // Member: read_s
  cdr >> ros_message.read_s;

  // Member: read_l
  cdr >> ros_message.read_l;

  // Member: read_yaw
  cdr >> ros_message.read_yaw;

  // Member: read_velocity
  cdr >> ros_message.read_velocity;

  // Member: read_accel
  cdr >> ros_message.read_accel;

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_serial_communication
get_serialized_size(
  const serial_communication::msg::ReadCar & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: read_aorm
  {
    size_t item_size = sizeof(ros_message.read_aorm);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: read_e_stop
  {
    size_t item_size = sizeof(ros_message.read_e_stop);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: read_gear
  {
    size_t item_size = sizeof(ros_message.read_gear);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: read_speed
  {
    size_t item_size = sizeof(ros_message.read_speed);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: read_brake
  {
    size_t item_size = sizeof(ros_message.read_brake);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: read_enc
  {
    size_t item_size = sizeof(ros_message.read_enc);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: read_steer
  {
    size_t item_size = sizeof(ros_message.read_steer);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: read_s
  {
    size_t item_size = sizeof(ros_message.read_s);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: read_l
  {
    size_t item_size = sizeof(ros_message.read_l);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: read_yaw
  {
    size_t item_size = sizeof(ros_message.read_yaw);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: read_velocity
  {
    size_t item_size = sizeof(ros_message.read_velocity);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: read_accel
  {
    size_t item_size = sizeof(ros_message.read_accel);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_serial_communication
max_serialized_size_ReadCar(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;


  // Member: read_aorm
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: read_e_stop
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: read_gear
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: read_speed
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint16_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint16_t));
  }

  // Member: read_brake
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint16_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint16_t));
  }

  // Member: read_enc
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: read_steer
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: read_s
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: read_l
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: read_yaw
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: read_velocity
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: read_accel
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  return current_alignment - initial_alignment;
}

static bool _ReadCar__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const serial_communication::msg::ReadCar *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _ReadCar__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<serial_communication::msg::ReadCar *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _ReadCar__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const serial_communication::msg::ReadCar *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _ReadCar__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_ReadCar(full_bounded, 0);
}

static message_type_support_callbacks_t _ReadCar__callbacks = {
  "serial_communication::msg",
  "ReadCar",
  _ReadCar__cdr_serialize,
  _ReadCar__cdr_deserialize,
  _ReadCar__get_serialized_size,
  _ReadCar__max_serialized_size
};

static rosidl_message_type_support_t _ReadCar__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_ReadCar__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace serial_communication

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_serial_communication
const rosidl_message_type_support_t *
get_message_type_support_handle<serial_communication::msg::ReadCar>()
{
  return &serial_communication::msg::typesupport_fastrtps_cpp::_ReadCar__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, serial_communication, msg, ReadCar)() {
  return &serial_communication::msg::typesupport_fastrtps_cpp::_ReadCar__handle;
}

#ifdef __cplusplus
}
#endif
