// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from serial_communication:msg/ReadCar.idl
// generated code does not contain a copyright notice
#include "serial_communication/msg/detail/read_car__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "serial_communication/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "serial_communication/msg/detail/read_car__struct.h"
#include "serial_communication/msg/detail/read_car__functions.h"
#include "fastcdr/Cdr.h"

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

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _ReadCar__ros_msg_type = serial_communication__msg__ReadCar;

static bool _ReadCar__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _ReadCar__ros_msg_type * ros_message = static_cast<const _ReadCar__ros_msg_type *>(untyped_ros_message);
  // Field name: read_aorm
  {
    cdr << (ros_message->read_aorm ? true : false);
  }

  // Field name: read_e_stop
  {
    cdr << (ros_message->read_e_stop ? true : false);
  }

  // Field name: read_gear
  {
    cdr << ros_message->read_gear;
  }

  // Field name: read_speed
  {
    cdr << ros_message->read_speed;
  }

  // Field name: read_brake
  {
    cdr << ros_message->read_brake;
  }

  // Field name: read_enc
  {
    cdr << ros_message->read_enc;
  }

  // Field name: read_steer
  {
    cdr << ros_message->read_steer;
  }

  // Field name: read_s
  {
    cdr << ros_message->read_s;
  }

  // Field name: read_l
  {
    cdr << ros_message->read_l;
  }

  // Field name: read_yaw
  {
    cdr << ros_message->read_yaw;
  }

  // Field name: read_velocity
  {
    cdr << ros_message->read_velocity;
  }

  // Field name: read_accel
  {
    cdr << ros_message->read_accel;
  }

  return true;
}

static bool _ReadCar__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _ReadCar__ros_msg_type * ros_message = static_cast<_ReadCar__ros_msg_type *>(untyped_ros_message);
  // Field name: read_aorm
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->read_aorm = tmp ? true : false;
  }

  // Field name: read_e_stop
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->read_e_stop = tmp ? true : false;
  }

  // Field name: read_gear
  {
    cdr >> ros_message->read_gear;
  }

  // Field name: read_speed
  {
    cdr >> ros_message->read_speed;
  }

  // Field name: read_brake
  {
    cdr >> ros_message->read_brake;
  }

  // Field name: read_enc
  {
    cdr >> ros_message->read_enc;
  }

  // Field name: read_steer
  {
    cdr >> ros_message->read_steer;
  }

  // Field name: read_s
  {
    cdr >> ros_message->read_s;
  }

  // Field name: read_l
  {
    cdr >> ros_message->read_l;
  }

  // Field name: read_yaw
  {
    cdr >> ros_message->read_yaw;
  }

  // Field name: read_velocity
  {
    cdr >> ros_message->read_velocity;
  }

  // Field name: read_accel
  {
    cdr >> ros_message->read_accel;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_serial_communication
size_t get_serialized_size_serial_communication__msg__ReadCar(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _ReadCar__ros_msg_type * ros_message = static_cast<const _ReadCar__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name read_aorm
  {
    size_t item_size = sizeof(ros_message->read_aorm);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name read_e_stop
  {
    size_t item_size = sizeof(ros_message->read_e_stop);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name read_gear
  {
    size_t item_size = sizeof(ros_message->read_gear);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name read_speed
  {
    size_t item_size = sizeof(ros_message->read_speed);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name read_brake
  {
    size_t item_size = sizeof(ros_message->read_brake);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name read_enc
  {
    size_t item_size = sizeof(ros_message->read_enc);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name read_steer
  {
    size_t item_size = sizeof(ros_message->read_steer);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name read_s
  {
    size_t item_size = sizeof(ros_message->read_s);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name read_l
  {
    size_t item_size = sizeof(ros_message->read_l);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name read_yaw
  {
    size_t item_size = sizeof(ros_message->read_yaw);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name read_velocity
  {
    size_t item_size = sizeof(ros_message->read_velocity);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name read_accel
  {
    size_t item_size = sizeof(ros_message->read_accel);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _ReadCar__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_serial_communication__msg__ReadCar(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_serial_communication
size_t max_serialized_size_serial_communication__msg__ReadCar(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: read_aorm
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: read_e_stop
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: read_gear
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: read_speed
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint16_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint16_t));
  }
  // member: read_brake
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint16_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint16_t));
  }
  // member: read_enc
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: read_steer
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: read_s
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: read_l
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: read_yaw
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: read_velocity
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: read_accel
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  return current_alignment - initial_alignment;
}

static size_t _ReadCar__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_serial_communication__msg__ReadCar(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_ReadCar = {
  "serial_communication::msg",
  "ReadCar",
  _ReadCar__cdr_serialize,
  _ReadCar__cdr_deserialize,
  _ReadCar__get_serialized_size,
  _ReadCar__max_serialized_size
};

static rosidl_message_type_support_t _ReadCar__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_ReadCar,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, serial_communication, msg, ReadCar)() {
  return &_ReadCar__type_support;
}

#if defined(__cplusplus)
}
#endif
