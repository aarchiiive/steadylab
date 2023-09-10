// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from serial_communication:msg/WriteCar.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "serial_communication/msg/detail/write_car__rosidl_typesupport_introspection_c.h"
#include "serial_communication/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "serial_communication/msg/detail/write_car__functions.h"
#include "serial_communication/msg/detail/write_car__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void WriteCar__rosidl_typesupport_introspection_c__WriteCar_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  serial_communication__msg__WriteCar__init(message_memory);
}

void WriteCar__rosidl_typesupport_introspection_c__WriteCar_fini_function(void * message_memory)
{
  serial_communication__msg__WriteCar__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember WriteCar__rosidl_typesupport_introspection_c__WriteCar_message_member_array[5] = {
  {
    "write_e_stop",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(serial_communication__msg__WriteCar, write_e_stop),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "write_gear",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(serial_communication__msg__WriteCar, write_gear),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "write_speed",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT16,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(serial_communication__msg__WriteCar, write_speed),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "write_brake",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT16,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(serial_communication__msg__WriteCar, write_brake),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "write_steer",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(serial_communication__msg__WriteCar, write_steer),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers WriteCar__rosidl_typesupport_introspection_c__WriteCar_message_members = {
  "serial_communication__msg",  // message namespace
  "WriteCar",  // message name
  5,  // number of fields
  sizeof(serial_communication__msg__WriteCar),
  WriteCar__rosidl_typesupport_introspection_c__WriteCar_message_member_array,  // message members
  WriteCar__rosidl_typesupport_introspection_c__WriteCar_init_function,  // function to initialize message memory (memory has to be allocated)
  WriteCar__rosidl_typesupport_introspection_c__WriteCar_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t WriteCar__rosidl_typesupport_introspection_c__WriteCar_message_type_support_handle = {
  0,
  &WriteCar__rosidl_typesupport_introspection_c__WriteCar_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_serial_communication
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, serial_communication, msg, WriteCar)() {
  if (!WriteCar__rosidl_typesupport_introspection_c__WriteCar_message_type_support_handle.typesupport_identifier) {
    WriteCar__rosidl_typesupport_introspection_c__WriteCar_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &WriteCar__rosidl_typesupport_introspection_c__WriteCar_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
